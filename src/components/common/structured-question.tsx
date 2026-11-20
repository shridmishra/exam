"use client";

import React, { useMemo } from "react";
import { RichMathText } from "@/components/common/math-renderer";

interface StructuredQuestionProps {
  content: string;
  isCompleted?: boolean;
  className?: string;
  qNo?: string;
}

interface ParsedBlock {
  type: "lead" | "section-header" | "list" | "params-box";
  title?: string;
  items?: Array<{ num?: string; text: string }>;
  text?: string;
}

function cleanMathInside(inner: string): string {
  return inner
    .replace(/&mu;/g, "\\mu")
    .replace(/&phi;/g, "\\phi")
    .replace(/&gamma;/g, "\\gamma")
    .replace(/&alpha;/g, "\\alpha")
    .replace(/&beta;/g, "\\beta")
    .replace(/&theta;/g, "\\theta")
    .replace(/&sigma;/g, "\\sigma")
    .replace(/&tau;/g, "\\tau")
    .replace(/&deg;/g, "^{\\circ}")
    .replace(/&sup2;/g, "^2")
    .replace(/&sup3;/g, "^3");
}

/**
 * Normalizes dense inline parenthetical lists, HTML entities, and bare LaTeX into structured markdown
 */
function normalizeQuestionText(raw: string): string {
  if (!raw) return "";
  let text = raw.trim();

  // 1. Sanitize any pre-existing isolated single-symbol display math like $$\phi$$ or $$\gamma$$ into inline $\phi$
  text = text.replace(
    /\$\$(\s*\\[a-zA-Z]+(?:\^\{?[^}]*\}?|_[a-zA-Z0-9{}]+)?\s*)\$\$/g,
    (_, symbol) => `$${symbol}$`
  );

  // 1a. Stash existing math blocks first so their contents are never corrupted
  const mathBlocks: string[] = [];
  const mathRegex = /(?:\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$(?:\\\$|[^\$\n])+\$)/g;
  text = text.replace(mathRegex, (match) => {
    let cleaned = match;
    if (match.startsWith("$") && match.endsWith("$")) {
      const isDisplay = match.startsWith("$$");
      const delim = isDisplay ? "$$" : "$";
      const inner = match.slice(delim.length, -delim.length);
      cleaned = delim + cleanMathInside(inner) + delim;
    }
    const token = `@@PRESERVED_MATH_${mathBlocks.length}@@`;
    mathBlocks.push(cleaned);
    return token;
  });

  // 2. Clean HTML entities in text mode
  // Numbers with degree entity: e.g. 10&deg; -> $10^{\circ}$
  text = text.replace(/(\d+(?:\.\d+)?)\s*&deg;/g, (_, num) => `$${num}^{\\circ}$`);
  text = text.replace(/&deg;/g, "°");

  // Superscripts in text mode: keep clean Unicode
  text = text.replace(/&sup2;/g, "²").replace(/&sup3;/g, "³");

  // Greek entities to inline LaTeX
  text = text
    .replace(/&phi;/g, "$\\phi$")
    .replace(/&gamma;/g, "$\\gamma$")
    .replace(/&mu;/g, "$\\mu$")
    .replace(/&alpha;/g, "$\\alpha$")
    .replace(/&beta;/g, "$\\beta$")
    .replace(/&theta;/g, "$\\theta$")
    .replace(/&sigma;/g, "$\\sigma$")
    .replace(/&tau;/g, "$\\tau$")
    .replace(/&Delta;/g, "$\\Delta$")
    .replace(/&delta;/g, "$\\delta$")
    .replace(/&epsilon;/g, "$\\epsilon$");

  // 3. Wrap bare LaTeX Greek letters & symbols in text mode ONLY if NOT already enclosed by $
  text = text.replace(
    /(?<![\$\\])\\(alpha|beta|gamma|delta|epsilon|theta|mu|phi|sigma|tau|omega|Delta)(?:_[a-zA-Z0-9]+)?(?![a-zA-Z\$])/g,
    (match) => `$${match}$`
  );

  // Also catch bare numbers with degree command: e.g. 10^\circ outside math
  text = text.replace(
    /(?<![\$\\])\b(\d+(?:\.\d+)?)\s*\^\\*circ\b(?!\$)/g,
    (_, num) => `$${num}^{\\circ}$`
  );

  // 4. Clean common engineering scientific notation: e.g. 6 x 10^-4 cm/sec -> $6 \times 10^{-4}\text{ cm/s}$
  text = text.replace(
    /(\d+(?:\.\d+)?)\s*(?:x|×)\s*10\^(-?\d+)\s*(cm\/s(?:ec)?|m\/s)/gi,
    (_, p1, p2, p3) => `$${p1} \\times 10^{${p2}}\\text{ ${p3}}$`
  );

  // 5. Restore preserved math blocks
  text = text.replace(/@@PRESERVED_MATH_(\d+)@@/g, (_, idx) => {
    return mathBlocks[parseInt(idx, 10)] || "";
  });

  // If already cleanly formatted with newlines and markdown headers/bullets, return
  if (text.includes("\n") && (text.includes("**") || text.includes("- ") || text.includes("• "))) {
    return text;
  }

  // 4. Separate figure details: e.g. (Figure-1: ...)
  text = text.replace(/\s*\((Figure[^\)]+)\)\.?\s*$/i, "\n\n**Given Geometry ($1):**\n");

  // 5. Separate "Calculate: (i) ...", "work out the following: ...", "Determine: ..."
  text = text.replace(
    /(?:and\s+)?(?:calculate|determine|find|work out the following|check the design)\s*:?\s*(?=(?:\(i\)|\([a-z]\)|\d+\.))/i,
    "\n\n**Calculate & Determine:**\n"
  );

  // 6. Separate "from the following data: (i)", "given: (i)", "given below: (i)"
  text = text.replace(
    /(?:from the following data|following data are given|given below|given that|has following data)\s*:?\s*(?=(?:\(i\)|\([a-z]\)|\d+\.))/i,
    "\n\n**Given Data & Parameters:**\n"
  );

  // 7. Split Roman numerals (i), (ii), (iii)... into vertical bullet list items
  text = text.replace(/\s*\(i\)\s*/gi, "\n- (i) ");
  text = text.replace(/\s*\(([ivx]+)\)\s*/gi, "\n- ($1) ");

  // 8. Split alpha enumerations (a), (b), (c)... if preceded by comma, colon, or semicolon
  text = text.replace(/(?:,|;|:)?\s*\(([a-d])\)\s*/gi, "\n- ($1) ");

  return text;
}

/**
 * Parses markdown question text into structured blocks
 */
function parseQuestionBlocks(rawText: string): ParsedBlock[] {
  const normalized = normalizeQuestionText(rawText);
  const rawLines = normalized.split("\n");
  const blocks: ParsedBlock[] = [];

  let currentBlock: ParsedBlock | null = null;

  for (let i = 0; i < rawLines.length; i++) {
    const line = rawLines[i].trim();
    if (!line) {
      if (currentBlock) {
        blocks.push(currentBlock);
        currentBlock = null;
      }
      continue;
    }

    // Check for section header like **Calculate:** or **Given Data (Figure-1):**
    const headerMatch = line.match(/^\*\*(.*?)\*\*:?$/);
    if (headerMatch) {
      if (currentBlock) {
        blocks.push(currentBlock);
        currentBlock = null;
      }
      const title = headerMatch[1].replace(/:$/, "").trim();
      const isParam = /given|data|parameter|constant|properties|dimension|geometry|level|details|limits/i.test(title);
      currentBlock = {
        type: isParam ? "params-box" : "list",
        title: title,
        items: [],
      };
      continue;
    }

    // Check for list item: "- ...", "• ...", "1. ...", "(i) ...", "(a) ...", "- (i) ..."
    const itemMatch = line.match(/^(?:[-*•]\s*)?(?:(\d+\.|\([a-z0-9]+\))\s*)?(.*)$/i);
    const isBulletOrNum =
      line.startsWith("-") ||
      line.startsWith("*") ||
      line.startsWith("•") ||
      /^(?:\d+\.|\([a-z0-9]+\))/i.test(line);

    if (isBulletOrNum && itemMatch) {
      const numLabel = itemMatch[1] ? itemMatch[1].trim() : undefined;
      const itemText = itemMatch[2].trim();
      if (!itemText) continue;

      if (!currentBlock || (currentBlock.type !== "list" && currentBlock.type !== "params-box")) {
        currentBlock = {
          type: "list",
          items: [],
        };
      }
      currentBlock.items?.push({
        num: numLabel,
        text: itemText,
      });
      continue;
    }

    // Regular text line
    if (!currentBlock) {
      currentBlock = {
        type: "lead",
        text: line,
      };
    } else if (currentBlock.type === "lead") {
      currentBlock.text += " " + line;
    } else if (currentBlock.type === "params-box" || currentBlock.type === "list") {
      currentBlock.items?.push({ text: line });
    }
  }

  if (currentBlock) {
    blocks.push(currentBlock);
  }

  return blocks;
}

const questionBlocksCache = new Map<string, ParsedBlock[]>();

function getParsedQuestionBlocks(content: string): ParsedBlock[] {
  if (!content) return [];
  const cached = questionBlocksCache.get(content);
  if (cached) return cached;
  const blocks = parseQuestionBlocks(content);
  questionBlocksCache.set(content, blocks);
  return blocks;
}

export const StructuredQuestion = React.memo(function StructuredQuestion({
  content,
  isCompleted = false,
  className = "",
  qNo,
}: StructuredQuestionProps) {
  const blocks = useMemo(() => getParsedQuestionBlocks(content), [content]);
  const hasLeadBlock = blocks.length > 0 && blocks[0].type === "lead";

  return (
    <div
      className={`structured-question space-y-2 text-foreground font-sans ${
        isCompleted ? "opacity-75" : ""
      } ${className}`}
    >
      {/* If there is no lead block (e.g. question starts directly with a list or params box), render qNo upfront */}
      {qNo && !hasLeadBlock && (
        <div
          className={`text-sm sm:text-[14.5px] font-bold tracking-tight ${
            isCompleted
              ? "line-through text-muted-foreground decoration-muted-foreground/40"
              : "text-foreground"
          }`}
        >
          {qNo}
        </div>
      )}

      {blocks.map((block, bIdx) => {
        if (block.type === "lead" && block.text) {
          return (
            <div
              key={bIdx}
              className={`text-sm sm:text-[14.5px] font-semibold leading-relaxed tracking-tight ${
                isCompleted
                  ? "line-through text-muted-foreground decoration-muted-foreground/40"
                  : "text-foreground"
              }`}
            >
              {bIdx === 0 && qNo && (
                <span
                  className={`font-bold mr-2 ${
                    isCompleted ? "text-muted-foreground" : "text-foreground"
                  }`}
                >
                  {qNo}
                </span>
              )}
              <RichMathText inline text={block.text} />
            </div>
          );
        }

        if (block.type === "params-box") {
          return (
            <div
              key={bIdx}
              className="my-2.5 rounded-lg border border-border/70 bg-secondary/35 p-3 sm:p-3.5 space-y-2 shadow-sm"
            >
              {block.title && (
                <div className="flex items-center gap-2 text-[11px] font-bold uppercase tracking-wider text-muted-foreground select-none">
                  <span className="h-1.5 w-1.5 rounded-full bg-primary/60" />
                  <span>{block.title}</span>
                </div>
              )}
              <div className="space-y-1.5 pl-1">
                {block.items?.map((item, iIdx) => (
                  <div
                    key={iIdx}
                    className="flex items-start gap-2 text-xs sm:text-[13.5px] leading-relaxed text-foreground/90"
                  >
                    <span className="text-muted-foreground select-none mt-0.5">•</span>
                    <div className="flex-1">
                      <RichMathText inline text={item.text} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          );
        }

        if (block.type === "list") {
          return (
            <div key={bIdx} className="my-2 space-y-1.5">
              {block.title && (
                <div className="text-xs font-bold uppercase tracking-wider text-muted-foreground mb-1.5 select-none">
                  {block.title}
                </div>
              )}
              <div className="space-y-1 pl-0.5">
                {block.items?.map((item, iIdx) => (
                  <div
                    key={iIdx}
                    className="flex items-start gap-2.5 py-0.5 text-sm sm:text-[14.5px] leading-relaxed text-foreground/95"
                  >
                    {item.num ? (
                      <span className="text-xs font-bold px-1.5 py-0.5 rounded bg-secondary/80 text-foreground/80 select-none shrink-0 mt-0.5">
                        {item.num}
                      </span>
                    ) : (
                      <span className="text-primary/70 font-semibold select-none mt-0.5 shrink-0">
                        •
                      </span>
                    )}
                    <div className="flex-1">
                      <RichMathText inline text={item.text} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          );
        }

        return null;
      })}
    </div>
  );
});
