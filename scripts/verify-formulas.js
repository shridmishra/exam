#!/usr/bin/env node
/**
 * Formula Verification & Anti-Regression Test Suite (Zero Dependency Node.js runner)
 *
 * Scans all questions, canonical clusters, master formulas, and subject datasets
 * across the entire application. Runs every equation, code block, and solution
 * through KaTeX to detect:
 *   - KaTeX syntax / parse errors (<span class="katex-error">, style="color:#cc0000")
 *   - Unconverted HTML entities (&beta;, &phi;, &radic;, &sup2;, etc.) in math
 *   - Broken square roots (\sqrt (...)) or missing braces
 *
 * Exits with status code 1 if any formula fault is detected.
 */

const fs = require("fs");
const path = require("path");
const katex = require("katex");

function cleanLatexString(raw) {
  if (!raw) return "";
  let clean = raw.trim();

  // 1. Convert HTML line breaks to LaTeX line breaks inside math
  clean = clean.replace(/<br\s*\/?>/gi, " \\\\ ");

  // 2. Unescape underscores from JSON or markdown
  clean = clean.replace(/\\_/g, "_");

  // 3. HTML formatting tags inside math
  clean = clean.replace(/<sub\b[^>]*>(.*?)<\/sub>/gi, "_{$1}");
  clean = clean.replace(/<sup\b[^>]*>(.*?)<\/sup>/gi, "^{$1}");
  clean = clean.replace(/<strong\b[^>]*>(.*?)<\/strong>/gi, "\\mathbf{$1}");
  clean = clean.replace(/<b\b[^>]*>(.*?)<\/b>/gi, "\\mathbf{$1}");
  clean = clean.replace(/<em\b[^>]*>(.*?)<\/em>/gi, "\\mathit{$1}");
  clean = clean.replace(/<i\b[^>]*>(.*?)<\/i>/gi, "\\mathit{$1}");
  clean = clean.replace(/<span\b[^>]*>(.*?)<\/span>/gi, "$1");
  clean = clean.replace(/<\/?[a-zA-Z][^>]*>/g, "");

  // 4. HTML Greek entities (lowercase)
  clean = clean
    .replace(/&alpha;/gi, "\\alpha ")
    .replace(/&beta;/gi, "\\beta ")
    .replace(/&gamma;/gi, "\\gamma ")
    .replace(/&delta;/gi, "\\delta ")
    .replace(/&epsilon;/gi, "\\epsilon ")
    .replace(/&varepsilon;/gi, "\\varepsilon ")
    .replace(/&zeta;/gi, "\\zeta ")
    .replace(/&eta;/gi, "\\eta ")
    .replace(/&theta;/gi, "\\theta ")
    .replace(/&vartheta;/gi, "\\vartheta ")
    .replace(/&iota;/gi, "\\iota ")
    .replace(/&kappa;/gi, "\\kappa ")
    .replace(/&lambda;/gi, "\\lambda ")
    .replace(/&mu;/gi, "\\mu ")
    .replace(/&nu;/gi, "\\nu ")
    .replace(/&xi;/gi, "\\xi ")
    .replace(/&pi;/gi, "\\pi ")
    .replace(/&varpi;/gi, "\\varpi ")
    .replace(/&rho;/gi, "\\rho ")
    .replace(/&varrho;/gi, "\\varrho ")
    .replace(/&sigma;/gi, "\\sigma ")
    .replace(/&varsigma;/gi, "\\varsigma ")
    .replace(/&tau;/gi, "\\tau ")
    .replace(/&upsilon;/gi, "\\upsilon ")
    .replace(/&phi;/gi, "\\phi ")
    .replace(/&varphi;/gi, "\\varphi ")
    .replace(/&chi;/gi, "\\chi ")
    .replace(/&psi;/gi, "\\psi ")
    .replace(/&omega;/gi, "\\omega ");

  // 5. HTML Greek entities (uppercase)
  clean = clean
    .replace(/&Gamma;/g, "\\Gamma ")
    .replace(/&Delta;/g, "\\Delta ")
    .replace(/&Theta;/g, "\\Theta ")
    .replace(/&Lambda;/g, "\\Lambda ")
    .replace(/&Xi;/g, "\\Xi ")
    .replace(/&Pi;/g, "\\Pi ")
    .replace(/&Sigma;/g, "\\Sigma ")
    .replace(/&Upsilon;/g, "\\Upsilon ")
    .replace(/&Phi;/g, "\\Phi ")
    .replace(/&Psi;/g, "\\Psi ")
    .replace(/&Omega;/g, "\\Omega ");

  // 6. Mathematical square roots & powers
  clean = clean.replace(/&radic;\s*\(([^)]+)\)/g, "\\sqrt{$1}");
  clean = clean.replace(/&radic;\s*\{([^}]+)\}/g, "\\sqrt{$1}");
  clean = clean.replace(/&radic;\s*([a-zA-Z0-9]+)/g, "\\sqrt{$1}");
  clean = clean.replace(/&radic;/g, "\\sqrt ");
  clean = clean.replace(/\\sqrt\s*\(([^)]+)\)/g, "\\sqrt{$1}");

  // Superscripts & exponents
  clean = clean
    .replace(/&sup0;/g, "^0")
    .replace(/&sup1;/g, "^1")
    .replace(/&sup2;/g, "^2")
    .replace(/&sup3;/g, "^3")
    .replace(/&sup4;/g, "^4")
    .replace(/&sup5;/g, "^5")
    .replace(/&sup6;/g, "^6")
    .replace(/&sup7;/g, "^7")
    .replace(/&sup8;/g, "^8")
    .replace(/&sup9;/g, "^9")
    .replace(/&deg;/g, "^{\\circ}")
    .replace(/\^\\*circ\b/g, "^{\\circ}");

  // Fractions
  clean = clean
    .replace(/&frac12;/g, "\\frac{1}{2}")
    .replace(/&frac14;/g, "\\frac{1}{4}")
    .replace(/&frac34;/g, "\\frac{3}{4}");

  // Strip checkmark in math mode
  clean = clean.replace(/✓/g, "");

  // Operators & comparison symbols
  clean = clean
    .replace(/&plusmn;|&pm;/g, "\\pm ")
    .replace(/&mp;/g, "\\mp ")
    .replace(/&times;/g, "\\times ")
    .replace(/&divide;/g, "\\div ")
    .replace(/&middot;|&sdot;/g, "\\cdot ")
    .replace(/&asymp;|&approx;/g, "\\approx ")
    .replace(/&equiv;/g, "\\equiv ")
    .replace(/&ne;|&neq;/g, "\\ne ")
    .replace(/&le;/g, "\\le ")
    .replace(/&ge;/g, "\\ge ")
    .replace(/&infin;/g, "\\infty ")
    .replace(/&prop;/g, "\\propto ")
    .replace(/&part;|&partial;/g, "\\partial ")
    .replace(/&nabla;/g, "\\nabla ")
    .replace(/&sim;/g, "\\sim ")
    .replace(/&cong;/g, "\\cong ")
    .replace(/&perp;/g, "\\perp ")
    .replace(/&sub;/g, "\\subset ")
    .replace(/&supe;/g, "\\subseteq ")
    .replace(/&isin;/g, "\\in ")
    .replace(/&notin;/g, "\\notin ")
    .replace(/&cup;/g, "\\cup ")
    .replace(/&cap;/g, "\\cap ")
    .replace(/&bull;/g, "\\bullet ")
    .replace(/&hellip;/g, "\\dots ")
    .replace(/&prime;/g, "'")
    .replace(/&Prime;/g, "''")
    .replace(/&minus;/g, "-");

  // Arrows & logic
  clean = clean
    .replace(/&implies;|&rArr;/g, "\\implies ")
    .replace(/&rarr;/g, "\\to ")
    .replace(/&larr;/g, "\\leftarrow ")
    .replace(/&harr;/g, "\\leftrightarrow ")
    .replace(/&iff;|&hArr;/g, "\\iff ")
    .replace(/&lArr;/g, "\\Leftarrow ");

  // Normal text entities
  clean = clean
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&nbsp;/g, " ")
    .replace(/&mdash;/g, " --- ")
    .replace(/&ndash;/g, " -- ");

  // Percent sign: escape unescaped %
  clean = clean.replace(/(?<!\\)%/g, "\\%");

  // Bare & outside alignment environments
  if (!/\\begin\{(?:matrix|pmatrix|bmatrix|aligned|align|array|cases)\}/.test(clean)) {
    clean = clean.replace(/&amp;/g, "\\&").replace(/&(?![a-zA-Z#0-9]+;)/g, "\\&");
  } else {
    clean = clean.replace(/&amp;/g, "&");
  }

  return clean;
}

function extractMathSafe(math) {
  let clean = math.trim();
  let trailingBadge = "";

  const htmlBadgeMatch = clean.match(
    /(?:\\quad|\s)*(?:\\text\{)?\s*(<span class="sol-badge-safe">[\s\S]*?<\/span>)\s*\}?\s*$/
  );
  if (htmlBadgeMatch) {
    clean = clean.slice(0, htmlBadgeMatch.index).trim();
    trailingBadge = htmlBadgeMatch[1];
    return { cleanMath: clean, trailingBadge };
  }

  const mathSafeMatch = clean.match(
    /(?:\\quad|\s)+\s*(?:\\text\{|\\mathbf\{)?\s*(\((?:\\text\{|\\mathbf\{)?\s*(?:(?![^)]*?\b(?:un|not|in)safe\b)(?:Safe|safe|OK|O\.K\.|Hence safe|Highly Safe|Extremely Safe)[^)]*?)\)|\[(?:\\text\{|\\mathbf\{)?\s*(?:(?![^\]]*?\b(?:un|not|in)safe\b)(?:Safe|safe|OK|O\.K\.|Hence safe|Highly Safe|Extremely Safe)[^\]]*?)\])\s*\}?\s*$/
  );

  if (mathSafeMatch) {
    clean = clean.slice(0, mathSafeMatch.index).trim();
    let badgeText = mathSafeMatch[1]
      .replace(/^[\(\[]|[\)\]]$/g, "")
      .replace(/\\text\{|\\mathbf\{|\}/g, "")
      .replace(/\\ /g, " ")
      .trim();
    if (badgeText.startsWith("safe")) badgeText = "Safe" + badgeText.slice(4);
    trailingBadge = `<span class="sol-badge-safe"><span class="sol-badge-check">✓</span> ${badgeText}</span>`;
  }
  return { cleanMath: clean, trailingBadge };
}

const mathCmdRegex =
  /\\(?:frac|sqrt|times|cdot|implies|to|rightarrow|leftarrow|partial|Delta|alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|circ|approx|pm|le|ge|ne|neq|sum|prod|int|sin|cos|tan)(?![a-zA-Z])|[=&]|\\left|\\right|\^|_|\b(?:kPa|kN|MPa)\b/;

function extractFormulas(html) {
  const list = [];
  const codeMatches = html.matchAll(/<code>([\s\S]*?)<\/code>/g);
  for (const m of codeMatches) {
    if (mathCmdRegex.test(m[1]) || /[+\-*\/=^_{}\\]/.test(m[1])) {
      list.push({ type: "code", raw: m[1] });
    }
  }
  const dispMatches = html.matchAll(/(?:\$\$|\\{1,2}\[)([\s\S]*?)(?:\$\$|\\{1,2}\])/g);
  for (const m of dispMatches) {
    list.push({ type: "display", raw: m[1] });
  }
  const inlineMatches = html.matchAll(/(?:(?<!\$)\$|\\{1,2}\()([^\$\n]+?)(?:\$|\\{1,2}\))/g);
  for (const m of inlineMatches) {
    list.push({ type: "inline", raw: m[1] });
  }
  return list;
}

let totalTested = 0;
let errors = [];

function checkText(text, source, id) {
  if (!text) return;
  const formulas = extractFormulas(text);
  for (const f of formulas) {
    totalTested++;
    const cleaned = cleanLatexString(f.raw);
    const { cleanMath } = extractMathSafe(cleaned);
    try {
      katex.renderToString(cleanMath, { throwOnError: true });
    } catch (err) {
      errors.push({
        source,
        id,
        type: f.type,
        raw: f.raw,
        cleaned: cleanMath,
        error: err.message,
      });
    }
  }
}

function scanDir(dir) {
  if (!fs.existsSync(dir)) return;
  const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"));
  for (const file of files) {
    const content = fs.readFileSync(path.join(dir, file), "utf-8");
    let data;
    try {
      data = JSON.parse(content);
    } catch {
      continue;
    }
    const items = Array.isArray(data)
      ? data
      : data.questions || Object.values(data);
    for (const item of items) {
      if (!item || typeof item !== "object") continue;
      const itemId = item.id || item.code || item.title || "item";
      checkText(item.question, file, itemId);
      checkText(item.solution, file, itemId);
      checkText(item.master_solution, file, itemId);
      checkText(item.formula, file, itemId);
      checkText(item.latex, file, itemId);
    }
  }
}

console.log("=================================================");
console.log("  Exam Platform Formula Verification Test Suite  ");
console.log("=================================================");
console.log("Scanning src/data...");
scanDir(path.join(process.cwd(), "src/data"));

console.log("Scanning subjects datasets...");
const subjectsDir = path.join(process.cwd(), "subjects");
if (fs.existsSync(subjectsDir)) {
  for (const sub of fs.readdirSync(subjectsDir)) {
    const subPath = path.join(subjectsDir, sub);
    if (fs.statSync(subPath).isDirectory()) {
      scanDir(subPath);
    }
  }
}

console.log(`\nVerification Complete:`);
console.log(`- Total Mathematical Formulas Verified:   ${totalTested}`);
console.log(`- Total Formula Faults / Red KaTeX Errors: ${errors.length}`);

if (errors.length > 0) {
  console.error("\n❌ FORMULA FAULTS DETECTED:\n");
  errors.forEach((e, idx) => {
    console.error(`[Fault ${idx + 1}] (${e.source} #${e.id}) [${e.type}]`);
    console.error(`  Raw:     ${e.raw}`);
    console.error(`  Cleaned: ${e.cleaned}`);
    console.error(`  Error:   ${e.error}\n`);
  });
  process.exit(1);
} else {
  console.log("\n✅ All formulas parsed and rendered cleanly with zero KaTeX errors!\n");
  process.exit(0);
}
