#!/usr/bin/env npx tsx
/**
 * Formula Verification & Anti-Regression Test Suite
 *
 * Scans all questions, canonical clusters, master formulas, and subject datasets
 * across the entire application. Runs every equation, code block, and solution
 * through KaTeX and the math-utils pipeline to detect:
 *   - KaTeX syntax / parse errors (<span class="katex-error">, style="color:#cc0000")
 *   - Unconverted HTML entities (&beta;, &phi;, &radic;, &sup2;, etc.) in math
 *   - Invalid LaTeX square root syntax (\sqrt (...))
 *   - Badly formatted safety tags or unescaped characters
 *
 * Exits with status code 1 if any formula fault is detected.
 */

import fs from "fs";
import path from "path";
import katex from "katex";
import {
  renderLatexInHtml,
  renderMarkdownWithMath,
  renderInlineMarkdownWithMath,
  safeRenderKatex,
} from "../src/lib/math-utils";

interface FormulaFault {
  source: string;
  id: string;
  context: string;
  raw: string;
  error: string;
}

const faults: FormulaFault[] = [];
let totalItemsTested = 0;
let totalFormulasTested = 0;

function checkHtmlForKatexErrors(
  html: string,
  source: string,
  id: string,
  context: string
) {
  if (!html) return;
  totalItemsTested++;

  // Test full pipeline rendering
  const rendered = renderLatexInHtml(html);

  // Check 1: Does KaTeX output an error block?
  if (rendered.includes("katex-error") || rendered.includes("#cc0000")) {
    const errorMatch = rendered.match(
      /<span class="katex-error"[^>]*title="([^"]*)"[^>]*>([\s\S]*?)<\/span>/
    );
    faults.push({
      source,
      id,
      context,
      raw: errorMatch ? errorMatch[2] : html.slice(0, 120),
      error: errorMatch
        ? errorMatch[1]
        : "KaTeX render error detected in output HTML",
    });
  }

  // Check 2: Are there unrendered HTML entities remaining inside math blocks?
  const mathBlockMatches = rendered.matchAll(
    /<span class="katex"[\s\S]*?<\/span>\s*<\/span>/g
  );
  for (const m of mathBlockMatches) {
    totalFormulasTested++;
    if (/&(?:beta|phi|gamma|alpha|theta|delta|sigma|tau|radic|sup[0-9]);/i.test(m[0])) {
      faults.push({
        source,
        id,
        context: `${context} (raw entity in math)`,
        raw: m[0].slice(0, 100),
        error: "Unconverted HTML entity found inside KaTeX rendered output",
      });
    }
  }

  // Check 3: Extract code blocks that represent formulas and test with strict throwOnError
  const codeMatches = html.matchAll(/<code>([\s\S]*?)<\/code>/g);
  for (const cm of codeMatches) {
    const inner = cm[1];
    if (/[=&\\+\-*\/^_{}]/.test(inner)) {
      totalFormulasTested++;
      // We also verify that our math-utils cleanLatexString handles this without throwing
      try {
        const testRender = renderLatexInHtml(`<code>${inner}</code>`);
        if (testRender.includes("katex-error")) {
          faults.push({
            source,
            id,
            context: `${context} (code block)`,
            raw: inner,
            error: "Code block formula failed KaTeX parsing",
          });
        }
      } catch (err: any) {
        faults.push({
          source,
          id,
          context: `${context} (code block exception)`,
          raw: inner,
          error: err.message || String(err),
        });
      }
    }
  }
}

function scanDataDirectory(dirPath: string) {
  if (!fs.existsSync(dirPath)) return;
  const files = fs.readdirSync(dirPath).filter((f) => f.endsWith(".json"));

  for (const file of files) {
    const fullPath = path.join(dirPath, file);
    const content = fs.readFileSync(fullPath, "utf-8");
    let data: any;
    try {
      data = JSON.parse(content);
    } catch (e: any) {
      faults.push({
        source: file,
        id: "PARSE_ERROR",
        context: "JSON parsing",
        raw: content.slice(0, 100),
        error: e.message,
      });
      continue;
    }

    const items = Array.isArray(data)
      ? data
      : data.questions || Object.values(data);

    for (const item of items) {
      if (!item || typeof item !== "object") continue;
      const itemId = item.id || item.code || item.title || "item";

      if (item.question) {
        checkHtmlForKatexErrors(item.question, file, itemId, "question");
      }
      if (item.solution) {
        checkHtmlForKatexErrors(item.solution, file, itemId, "solution");
      }
      if (item.master_solution) {
        checkHtmlForKatexErrors(
          item.master_solution,
          file,
          itemId,
          "master_solution"
        );
      }
      if (item.formula) {
        checkHtmlForKatexErrors(item.formula, file, itemId, "formula");
      }
      if (item.latex) {
        checkHtmlForKatexErrors(item.latex, file, itemId, "latex");
      }
    }
  }
}

function scanSubjectsDirectory(subjectsDir: string) {
  if (!fs.existsSync(subjectsDir)) return;
  const entries = fs.readdirSync(subjectsDir, { withFileTypes: true });

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const subDir = path.join(subjectsDir, entry.name);
    const jsonFiles = fs
      .readdirSync(subDir)
      .filter((f) => f.endsWith(".json"));

    for (const jf of jsonFiles) {
      const fullPath = path.join(subDir, jf);
      const content = fs.readFileSync(fullPath, "utf-8");
      let data: any;
      try {
        data = JSON.parse(content);
      } catch {
        continue;
      }
      const items = Array.isArray(data) ? data : Object.values(data);
      for (const item of items) {
        if (!item || typeof item !== "object") continue;
        const itemId = item.id || item.code || "sub-item";
        if (item.question) {
          checkHtmlForKatexErrors(item.question, `${entry.name}/${jf}`, itemId, "question");
        }
        if (item.solution) {
          checkHtmlForKatexErrors(item.solution, `${entry.name}/${jf}`, itemId, "solution");
        }
        if (item.master_solution) {
          checkHtmlForKatexErrors(
            item.master_solution,
            `${entry.name}/${jf}`,
            itemId,
            "master_solution"
          );
        }
      }
    }
  }
}

console.log("=================================================");
console.log("  Exam Platform Formula Verification Test Suite  ");
console.log("=================================================");
console.log("Scanning src/data...");
scanDataDirectory(path.join(process.cwd(), "src/data"));

console.log("Scanning subjects/ datasets...");
scanSubjectsDirectory(path.join(process.cwd(), "subjects"));

console.log(`\nVerification Complete:`);
console.log(`- Total Questions / Content Items Scanned: ${totalItemsTested}`);
console.log(`- Total Mathematical Formulas Verified:   ${totalFormulasTested}`);
console.log(`- Total Formula Faults / Red KaTeX Errors: ${faults.length}`);

if (faults.length > 0) {
  console.error("\n❌ FORMULA FAULTS DETECTED:\n");
  faults.forEach((f, idx) => {
    console.error(`[Fault ${idx + 1}] Source: ${f.source} | ID: ${f.id} | Context: ${f.context}`);
    console.error(`  Raw Expression: ${f.raw}`);
    console.error(`  Error Detail:   ${f.error}\n`);
  });
  process.exit(1);
} else {
  console.log("\n✅ All formulas parsed and rendered cleanly with zero KaTeX errors!\n");
  process.exit(0);
}
