import { NextRequest, NextResponse } from "next/server";
import fs from "fs/promises";
import path from "path";

export const dynamic = "force-dynamic";

interface FeedbackPayload {
  type?: "bug" | "suggestion" | "content" | "general";
  title?: string;
  message: string;
  contact?: string;
  context?: {
    subject?: string;
    subjectCode?: string;
    activeTab?: string;
    url?: string;
    userAgent?: string;
    screen?: string;
  };
}

// In-memory rate limiting to prevent spam (max 8 submissions per 10 minutes per IP)
const rateLimitMap = new Map<string, { count: number; resetTime: number }>();

function checkRateLimit(ip: string): boolean {
  const now = Date.now();
  const entry = rateLimitMap.get(ip);

  if (!entry || now > entry.resetTime) {
    rateLimitMap.set(ip, { count: 1, resetTime: now + 10 * 60 * 1000 });
    return true;
  }

  if (entry.count >= 8) {
    return false;
  }

  entry.count += 1;
  return true;
}

export async function POST(req: NextRequest) {
  try {
    const ip =
      req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ||
      req.headers.get("x-real-ip") ||
      "unknown-ip";

    if (!checkRateLimit(ip)) {
      return NextResponse.json(
        { error: "Too many feedback submissions. Please wait a few minutes." },
        { status: 429 }
      );
    }

    const body: FeedbackPayload = await req.json();

    if (!body || typeof body.message !== "string" || !body.message.trim()) {
      return NextResponse.json(
        { error: "Message is required." },
        { status: 400 }
      );
    }

    const timestamp = new Date().toISOString();
    const dateStr = timestamp.slice(0, 10);
    const uniqueSuffix = Math.random().toString(36).substring(2, 8);
    const id = `fb_${Date.now()}_${uniqueSuffix}`;
    const filename = `${dateStr}_${id}.json`;

    const record = {
      id,
      timestamp,
      type: body.type || "suggestion",
      title: (body.title || "").trim().slice(0, 150),
      message: body.message.trim().slice(0, 4000),
      contact: (body.contact || "").trim().slice(0, 100),
      status: "new",
      context: {
        subject: body.context?.subject || "Unknown",
        subjectCode: body.context?.subjectCode,
        activeTab: body.context?.activeTab,
        url: body.context?.url,
        userAgent: req.headers.get("user-agent") || body.context?.userAgent,
        screen: body.context?.screen,
      },
    };

    let savedToGithub = false;
    let savedLocally = false;
    let githubError: string | null = null;

    // 1. Direct GitHub Commit (Conflict-free: each feedback is an independent new file)
    const ghToken =
      process.env.GITHUB_TOKEN ||
      process.env.GH_TOKEN ||
      process.env.GITHUB_PAT;
    const ghOwner = process.env.GITHUB_REPO_OWNER || "shridmishra";
    const ghRepo = process.env.GITHUB_REPO_NAME || "exam";
    const ghBranch = process.env.GITHUB_BRANCH || "main";

    if (ghToken) {
      try {
        const ghUrl = `https://api.github.com/repos/${ghOwner}/${ghRepo}/contents/feedback/${filename}`;
        const base64Content = Buffer.from(
          JSON.stringify(record, null, 2),
          "utf8"
        ).toString("base64");

        const ghResponse = await fetch(ghUrl, {
          method: "PUT",
          headers: {
            Authorization: `Bearer ${ghToken}`,
            Accept: "application/vnd.github+json",
            "User-Agent": "Exam-Feedback-Collector",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: `feat(feedback): ${record.type} report - ${record.title || id}`,
            content: base64Content,
            branch: ghBranch,
          }),
        });

        if (ghResponse.ok) {
          savedToGithub = true;
        } else {
          const errText = await ghResponse.text();
          console.warn(`[GITHUB_COMMIT_FAILED] HTTP ${ghResponse.status}: ${errText}`);
          githubError = `GitHub HTTP ${ghResponse.status}`;
        }
      } catch (err: any) {
        console.warn("[GITHUB_COMMIT_ERROR]", err?.message || err);
        githubError = err?.message || "Failed to commit to GitHub";
      }
    }

    // 2. Local File System Storage (local development or server with writable disk)
    try {
      const feedbackDir = path.join(process.cwd(), "feedback");
      await fs.mkdir(feedbackDir, { recursive: true });
      await fs.writeFile(
        path.join(feedbackDir, filename),
        JSON.stringify(record, null, 2),
        "utf8"
      );
      savedLocally = true;

      // Update compiled local master file if writable
      try {
        const allFeedbacksPath = path.join(feedbackDir, "all_feedbacks.json");
        let allFeedbacks: any[] = [];
        try {
          const raw = await fs.readFile(allFeedbacksPath, "utf8");
          allFeedbacks = JSON.parse(raw);
          if (!Array.isArray(allFeedbacks)) allFeedbacks = [];
        } catch {
          allFeedbacks = [];
        }
        allFeedbacks.unshift(record);
        await fs.writeFile(
          allFeedbacksPath,
          JSON.stringify(allFeedbacks, null, 2),
          "utf8"
        );
      } catch {
        // Master file append non-fatal
      }
    } catch (fsErr: any) {
      // In read-only serverless environments without GitHub token, log record so it is not lost
      console.warn(
        `[USER_FEEDBACK_FALLBACK_RECORD] ${JSON.stringify(record)}`
      );
    }

    return NextResponse.json({
      success: true,
      id,
      timestamp,
      savedToGithub,
      savedLocally,
      message: "Feedback recorded successfully. Thank you!",
      ...(githubError && !savedToGithub ? { note: githubError } : {}),
    });
  } catch (error: any) {
    console.error("[FEEDBACK_API_ERROR]", error);
    return NextResponse.json(
      { error: "Internal server error saving feedback." },
      { status: 500 }
    );
  }
}

export async function GET(req: NextRequest) {
  try {
    const isDev = process.env.NODE_ENV !== "production";
    const authHeader = req.headers.get("authorization");
    const secretKey = req.nextUrl.searchParams.get("key");
    const devSecret = process.env.DEVELOPER_SECRET || process.env.GITHUB_TOKEN;

    const isAuthorized =
      isDev ||
      (devSecret && (secretKey === devSecret || authHeader === `Bearer ${devSecret}`));

    if (!isAuthorized) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const feedbackDir = path.join(process.cwd(), "feedback");
    try {
      const files = await fs.readdir(feedbackDir);
      const jsonFiles = files
        .filter((f) => f.endsWith(".json") && f !== "all_feedbacks.json")
        .sort()
        .reverse();

      const items = await Promise.all(
        jsonFiles.map(async (file) => {
          try {
            const raw = await fs.readFile(path.join(feedbackDir, file), "utf8");
            return JSON.parse(raw);
          } catch {
            return null;
          }
        })
      );

      return NextResponse.json({
        total: items.filter(Boolean).length,
        items: items.filter(Boolean),
      });
    } catch {
      return NextResponse.json({ total: 0, items: [] });
    }
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
