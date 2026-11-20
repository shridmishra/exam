#!/usr/bin/env node

/**
 * Developer helper script to view all user-submitted feedback, bugs, and suggestions.
 * Usage:
 *   node scripts/view-feedback.js
 *   npm run feedback
 */

const fs = require("fs");
const path = require("path");

const FEEDBACK_DIR = path.join(__dirname, "..", "feedback");

function viewFeedback() {
  if (!fs.existsSync(FEEDBACK_DIR)) {
    console.log("\x1b[33mNo feedback directory found yet.\x1b[0m");
    return;
  }

  const files = fs
    .readdirSync(FEEDBACK_DIR)
    .filter((f) => f.endsWith(".json") && f !== "all_feedbacks.json")
    .sort()
    .reverse();

  if (files.length === 0) {
    console.log("\n\x1b[36mℹ No user feedback submitted yet.\x1b[0m\n");
    return;
  }

  console.log(`\n\x1b[32m══════════════════════════════════════════════════════════════════\x1b[0m`);
  console.log(`\x1b[1m\x1b[32m  EXAM INTELLIGENCE — USER FEEDBACK & SUGGESTIONS (${files.length} items)\x1b[0m`);
  console.log(`\x1b[32m══════════════════════════════════════════════════════════════════\x1b[0m\n`);

  files.forEach((file, idx) => {
    try {
      const content = JSON.parse(
        fs.readFileSync(path.join(FEEDBACK_DIR, file), "utf8")
      );

      const typeColors = {
        bug: "\x1b[31m[BUG]\x1b[0m",
        suggestion: "\x1b[34m[SUGGESTION]\x1b[0m",
        content: "\x1b[33m[CONTENT / TYPO]\x1b[0m",
        general: "\x1b[35m[GENERAL]\x1b[0m",
      };

      const tag = typeColors[content.type] || `[${content.type.toUpperCase()}]`;
      const date = content.timestamp
        ? new Date(content.timestamp).toLocaleString()
        : file;

      console.log(`\x1b[1m#${files.length - idx}\x1b[0m ${tag} \x1b[1m${content.title || "Untitled"}\x1b[0m`);
      console.log(`  \x1b[90mDate:    ${date} | ID: ${content.id || file}\x1b[0m`);
      if (content.contact) {
        console.log(`  \x1b[90mContact: ${content.contact}\x1b[0m`);
      }
      if (content.context) {
        const ctxParts = [];
        if (content.context.subject) ctxParts.push(`Subject: ${content.context.subject}`);
        if (content.context.activeTab) ctxParts.push(`Tab: ${content.context.activeTab}`);
        if (ctxParts.length > 0) {
          console.log(`  \x1b[90mContext: ${ctxParts.join(" | ")}\x1b[0m`);
        }
      }
      console.log(`  \x1b[37mMessage:\x1b[0m`);
      const indented = content.message
        .split("\n")
        .map((l) => `    ${l}`)
        .join("\n");
      console.log(indented);
      console.log(`\x1b[90m──────────────────────────────────────────────────────────────────\x1b[0m\n`);
    } catch (e) {
      console.error(`Error reading ${file}:`, e.message);
    }
  });
}

viewFeedback();
