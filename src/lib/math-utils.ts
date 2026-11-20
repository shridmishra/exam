import katex from "katex";

/**
 * Sanitizes math content before passing to KaTeX.
 * Handles escaped characters, HTML entities, and degree symbols.
 */
function cleanLatexString(raw: string): string {
  if (!raw) return "";
  let clean = raw.trim();
  // Unescape underscores from JSON or markdown
  clean = clean.replace(/\\_/g, "_");
  // Normalize HTML entities that might have been escaped
  clean = clean
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&amp;/g, "&")
    .replace(/&nbsp;/g, " ")
    .replace(/&mdash;/g, " --- ")
    .replace(/&ndash;/g, " -- ")
    .replace(/&radic;/g, "\\sqrt ")
    .replace(/&times;/g, "\\times ")
    .replace(/&middot;/g, "\\cdot ")
    .replace(/&implies;/g, "\\implies ")
    .replace(/&rarr;/g, "\\to ")
    .replace(/&Delta;/g, "\\Delta ")
    .replace(/&deg;/g, "^{\\circ}")
    .replace(/&sup2;/g, "^2")
    .replace(/&sup3;/g, "^3");

  clean = clean.replace(/<strong>(.*?)<\/strong>/g, "\\mathbf{$1}");
  // Fix escaped circ like ^\\circ or ^\circ into ^{\circ}
  clean = clean.replace(/\^\\*circ\b/g, "^{\\circ}");

  return clean;
}

/**
 * Synchronously renders all LaTeX formulas ($...$, $$...$$, \[...\], \(...\))
 * inside an HTML string using KaTeX.
 *
 * Designed to run cleanly both during Server-Side Rendering (SSR) and Client-Side
 * rendering, with ZERO hydration mismatches, ZERO flash of unrendered math, and
 * ZERO fragile useEffect DOM mutations.
 */
export function renderLatexInHtml(html: string): string {
  if (!html) return "";

  const preserved: string[] = [];

  // Protect any already-rendered KaTeX math or blocks so inner MathML is never re-parsed
  let s = html.replace(/<span class="katex"[\s\S]*?<\/span>\s*<\/span>/g, (m) => {
    const token = `@@PRESERVED_MATH_${preserved.length}@@`;
    preserved.push(m);
    return token;
  });

  const mathCmdRegex =
    /\\(?:frac|sqrt|times|cdot|implies|to|rightarrow|leftarrow|partial|Delta|alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|circ|approx|pm|le|ge|ne|neq|sum|prod|int|sin|cos|tan)(?![a-zA-Z])|[=&]|\\left|\\right|\^|_|\b(?:kPa|kN|MPa)\b/;

  // 0. Transform <code> blocks that contain LaTeX math or formulas into KaTeX
  s = s.replace(/<code>([\s\S]*?)<\/code>/g, (orig, codeContent) => {
    if (!mathCmdRegex.test(codeContent) && !/[+\-*\/=^_{}\\]/.test(codeContent)) {
      return orig;
    }
    const clean = cleanLatexString(codeContent);
    const isDisplay =
      clean.includes("=") ||
      clean.length > 20 ||
      clean.includes("\\frac") ||
      clean.includes("\\sqrt");
    try {
      const rendered = katex.renderToString(clean, {
        displayMode: isDisplay,
        throwOnError: false,
      });
      const token = `@@PRESERVED_MATH_${preserved.length}@@`;
      preserved.push(
        isDisplay
          ? `<div class="sol-math-block">${rendered}</div>`
          : `<span class="sol-math-inline">${rendered}</span>`
      );
      return token;
    } catch {
      return orig;
    }
  });

  // 1. Extract and render display math blocks ($$...$$ and \[...\])
  s = s.replace(
    /(?:\$\$|\\{1,2}\[)([\s\S]*?)(?:\$\$|\\{1,2}\])/g,
    (_, math) => {
      try {
        const clean = cleanLatexString(math);
        const rendered = katex.renderToString(clean, {
          displayMode: true,
          throwOnError: false,
        });
        const token = `@@PRESERVED_MATH_${preserved.length}@@`;
        preserved.push(`<div class="sol-math-block">${rendered}</div>`);
        return token;
      } catch (e) {
        console.warn("KaTeX display math error:", e);
        const token = `@@PRESERVED_MATH_${preserved.length}@@`;
        preserved.push(`<div class="sol-math-block">$$${math}$$</div>`);
        return token;
      }
    }
  );

  // 2. Tokenize by HTML tags so inline formulas never cross tags like <li>...</li>
  const parts = s.split(/(<\/?[a-zA-Z][^>]*>)/g);
  for (let i = 0; i < parts.length; i++) {
    // If it is an HTML tag, leave it untouched
    if (parts[i].startsWith("<") && parts[i].endsWith(">")) {
      continue;
    }

    // Inside text between tags, parse inline math $...$ and \(...\)
    parts[i] = parts[i].replace(
      /(?:(?<!\$)\$|\\{1,2}\()([^\$\n]+?)(?:\$|\\{1,2}\))/g,
      (_, math) => {
        try {
          const clean = cleanLatexString(math);
          return katex.renderToString(clean, {
            displayMode: false,
            throwOnError: false,
          });
        } catch (e) {
          console.warn("KaTeX inline math error:", e);
          return `$${math}$`;
        }
      }
    );

    // Also parse any bare LaTeX Greek letters or math symbols in text mode
    parts[i] = parts[i].replace(
      /(?<![\$\\])\\(alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|Delta)(?:_[a-zA-Z0-9{}]+)?(?![a-zA-Z\$])/g,
      (match) => {
        try {
          const clean = cleanLatexString(match);
          return katex.renderToString(clean, {
            displayMode: false,
            throwOnError: false,
          });
        } catch {
          return match;
        }
      }
    );
  }

  s = parts.join("");

  // 3. Restore all preserved math and KaTeX blocks
  s = s.replace(/@@PRESERVED_MATH_(\d+)@@/g, (_, idx) => {
    return preserved[parseInt(idx, 10)] || "";
  });

  return s;
}

/**
 * Automatically recognizes and wraps bare LaTeX equations, formulas,
 * and parenthesized mathematical expressions in Markdown text.
 */
function autoWrapLatexInMarkdown(text: string): string {
  if (!text) return "";
  const mathCmdRegex =
    /\\(?:frac|sqrt|times|cdot|implies|to|rightarrow|leftarrow|partial|Delta|alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|circ|approx|pm|le|ge|ne|neq|sum|prod|int|sin|cos|tan)(?![a-zA-Z])/;

  const mathUnitsAndFuncs =
    /^(?:sin|cos|tan|cot|sec|csc|log|ln|exp|max|min|kPa|MPa|GPa|kN|kN\/m|kN\/m\^2|kN\/m²|kN\/m\^3|kN\/m³|N|N\/m\^2|N\/m²|m|mm|cm|kg|sec|rad|deg)$/i;

  function hasProseWords(str: string): boolean {
    const withoutCmds = str.replace(/\\[a-zA-Z]+/g, " ");
    const words = withoutCmds.match(/\b[A-Za-z]{3,}\b/g) || [];
    return words.some((w) => !mathUnitsAndFuncs.test(w));
  }

  const lines = text.split("\n");
  const processed = lines.map((line) => {
    let l = line;
    const trimmed = l.trim();
    if (!trimmed) return l;

    if (
      !mathCmdRegex.test(trimmed) &&
      !/\\(?:[a-zA-Z]+)/.test(trimmed) &&
      !/^[a-zA-Z]_[0-9a-zA-Z]/.test(trimmed)
    ) {
      return l;
    }

    // Pattern 1: Standalone equation line (no label)
    if (
      !trimmed.includes(": ") &&
      (trimmed.includes("=") || trimmed.includes("\\implies") || trimmed.startsWith("\\")) &&
      !hasProseWords(trimmed)
    ) {
      let expr = trimmed;
      let trailing = "";
      if (expr.endsWith(".")) {
        expr = expr.slice(0, -1).trim();
        trailing = ".";
      }
      return `$${expr}$${trailing}`;
    }

    // Pattern 2: Labeled pure equation, e.g. "Initial area: A_0 = \frac..." or "3. Mohr-Coulomb: \sigma_1 = ..."
    const labelMatch = trimmed.match(/^((?:(?:\d+\.|[a-zA-Z]\))\s*)?[^:]+:\s*)(.+)$/);
    if (labelMatch) {
      const prefix = labelMatch[1];
      const rest = labelMatch[2].trim();

      if (!hasProseWords(rest) && (mathCmdRegex.test(rest) || rest.includes("="))) {
        let expr = rest;
        let trailing = "";
        if (expr.endsWith(".")) {
          expr = expr.slice(0, -1).trim();
          trailing = ".";
        }
        return `${prefix}$${expr}$${trailing}`;
      }
    }

    // Pattern 3: Mixed text with multiple inline formulas
    // 3a. Parentheses containing LaTeX: (\sigma_3 = 100 kPa)
    l = l.replace(/\(([^\)]*\\[a-zA-Z]+[^\)]*)\)/g, (m, inner) => `($${inner.trim()}$)`);

    // 3b. Formulas with = or math operators: \Delta L_1 = 2.0 mm or \epsilon_1 = \frac{2.0}{76} = 0.0263
    l = l.replace(
      /(?<!\$)((\\[a-zA-Z]+(?:\s*[a-zA-Z0-9_{}]+)?(?:\^\{?[^}]*\}?)?)\s*=\s*.*?(?=(?:\s*\\to\b|[,;]|\.(?:\s|$)|$)))/g,
      (m) => `$${m.trim()}$`
    );

    // 3c. Standalone arrows: \to, \implies
    l = l.replace(/(?<!\$)\\(to|implies|rightarrow)(?!\$)/g, (m, cmd) => `$\\${cmd}$`);

    // 3d. Any remaining bare \commands
    l = l.replace(
      /(?<![\$\\])\\(alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|Delta)(?:_[a-zA-Z0-9{}]+)?(?![a-zA-Z\$])/g,
      (match) => `$${match}$`
    );

    return l;
  });

  return processed.join("\n");
}

/**
 * Synchronously renders freeform Markdown text (such as personal notes,
 * study scratchpad, comparison tables, and formula notes) into rich HTML
 * with full KaTeX mathematical typesetting.
 */
export function renderMarkdownWithMath(raw: string): string {
  if (!raw) return "";

  // 1. Auto-wrap bare LaTeX equations and expressions
  let s = autoWrapLatexInMarkdown(raw);

  // 1a. Extract block display math first so internal newlines and pipes are protected
  const mathBlocks: string[] = [];

  const displayMathRegex =
    /(\$\$[\s\S]*?\$\$|\\{1,2}[[](?:[\s\S]*?)\\{1,2}[\]])/g;
  s = s.replace(displayMathRegex, (match) => {
    let inner = match.trim();
    if (inner.startsWith("$$") && inner.endsWith("$$")) {
      inner = inner.slice(2, -2);
    } else {
      if (inner.startsWith("\\\\[")) inner = inner.slice(3);
      else if (inner.startsWith("\\[")) inner = inner.slice(2);
      if (inner.endsWith("\\\\]")) inner = inner.slice(0, -3);
      else if (inner.endsWith("\\]")) inner = inner.slice(0, -2);
    }
    const clean = cleanLatexString(inner);
    let rendered = "";
    try {
      rendered = katex.renderToString(clean, {
        displayMode: true,
        throwOnError: false,
      });
    } catch {
      rendered = `$$${clean}$$`;
    }
    const token = `@@MATH_BLOCK_${mathBlocks.length}@@`;
    mathBlocks.push(`<div class="sol-math-block">${rendered}</div>`);
    return `\n\n${token}\n\n`;
  });

  // 2. Extract inline math
  const inlineMath: string[] = [];
  s = s.replace(
    /(?:\\{1,2}[(]([\s\S]*?)\\{1,2}[)]|(?<!\$)\$([^\$\n]+)\$(?!\$))/g,
    (_, p1, p2) => {
      const c = p1 !== undefined ? p1 : p2;
      const clean = cleanLatexString(c);
      let rendered = "";
      try {
        rendered = katex.renderToString(clean, {
          displayMode: false,
          throwOnError: false,
        });
      } catch {
        rendered = `$${clean}$`;
      }
      const token = `@@INLINE_MATH_${inlineMath.length}@@`;
      inlineMath.push(rendered);
      return token;
    }
  );

  // 3. Process lines (headings, tables, lists, paragraphs)
  const lines = s.replace(/\r/g, "").split("\n");
  const out: string[] = [];

  function splitRow(line: string): string[] {
    let t = line.trim();
    if (t.startsWith("|")) t = t.slice(1);
    if (t.endsWith("|")) t = t.slice(0, -1);
    return t.split("|").map((c) => c.trim());
  }

  function isTableDelimiter(line: string): boolean {
    const trimmed = line.trim();
    if (!trimmed.includes("-")) return false;
    const cells = splitRow(trimmed);
    if (cells.length === 0) return false;
    return cells.every((c) => /^\s*:?-{2,}:?\s*$/.test(c));
  }

  function formatInline(text: string): string {
    let t = text;
    t = t.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    t = t.replace(/__(.*?)__/g, "<strong>$1</strong>");
    t = t.replace(/(^|[^\*])\*([^\*]+)\*([^\*]|$)/g, "$1<em>$2</em>$3");
    t = t.replace(
      /`([^`]+)`/g,
      '<code class="text-xs bg-secondary px-1 py-0.5 rounded">$1</code>'
    );
    return t;
  }

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();

    if (!trimmed) {
      i++;
      continue;
    }

    // Check for math block token
    if (trimmed.startsWith("@@MATH_BLOCK_") && trimmed.endsWith("@@")) {
      out.push(trimmed);
      i++;
      continue;
    }

    // Headings
    const mHead = trimmed.match(/^(#{1,6})\s+(.*)$/);
    if (mHead) {
      const level = mHead[1].length;
      const text = formatInline(mHead[2]);
      out.push(
        `<h${level + 2} class="font-bold my-2 text-foreground">${text}</h${
          level + 2
        }>`
      );
      i++;
      continue;
    }

    // Markdown Table
    if (
      trimmed.includes("|") &&
      !trimmed.startsWith("#") &&
      i + 1 < lines.length &&
      isTableDelimiter(lines[i + 1])
    ) {
      const headers = splitRow(trimmed);
      i += 2; // skip header and delimiter
      const rows: string[][] = [];
      while (
        i < lines.length &&
        lines[i].trim().includes("|") &&
        lines[i].trim().length > 0
      ) {
        rows.push(splitRow(lines[i].trim()));
        i++;
      }
      const colWidth = (100 / Math.max(1, headers.length)).toFixed(1);
      const thHtml = headers
        .map((h) => `<th style="width: ${colWidth}%;">${formatInline(h)}</th>`)
        .join("");
      const trHtml = rows
        .map(
          (r) =>
            `<tr>${r.map((c) => `<td>${formatInline(c)}</td>`).join("")}</tr>`
        )
        .join("");
      out.push(
        `<div class="overflow-x-auto my-3"><table class="sol-table" style="table-layout: fixed; width: 100%;"><thead><tr>${thHtml}</tr></thead><tbody>${trHtml}</tbody></table></div>`
      );
      continue;
    }

    // Bullet lists
    if (/^[-*]\s+/.test(trimmed)) {
      const listItems: string[] = [];
      while (i < lines.length && /^[-*]\s+/.test(lines[i].trim())) {
        listItems.push(
          `<li>${formatInline(lines[i].trim().replace(/^[-*]\s+/, ""))}</li>`
        );
        i++;
      }
      out.push(`<ul class="sol-list my-2">${listItems.join("")}</ul>`);
      continue;
    }

    // Numbered lists
    if (/^\d+\.\s+/.test(trimmed)) {
      const listItems: string[] = [];
      while (i < lines.length && /^\d+\.\s+/.test(lines[i].trim())) {
        listItems.push(
          `<li>${formatInline(lines[i].trim().replace(/^\d+\.\s+/, ""))}</li>`
        );
        i++;
      }
      out.push(
        `<ol class="sol-list list-decimal pl-5 my-2">${listItems.join("")}</ol>`
      );
      continue;
    }

    // Normal paragraph
    out.push(`<p class="my-1.5 leading-relaxed">${formatInline(trimmed)}</p>`);
    i++;
  }

  let finalHtml = out.join("\n");

  // Restore inline math
  finalHtml = finalHtml.replace(/@@INLINE_MATH_(\d+)@@/g, (_, idx) => {
    return inlineMath[parseInt(idx, 10)] || "";
  });

  // Restore block math
  finalHtml = finalHtml.replace(/@@MATH_BLOCK_(\d+)@@/g, (_, idx) => {
    return mathBlocks[parseInt(idx, 10)] || "";
  });

  return finalHtml;
}

/**
 * Synchronously renders inline markdown and LaTeX math (for question text,
 * list items, parameter items) WITHOUT wrapping in outer <p> or <div> blocks.
 * Guarantees zero invalid HTML nesting (<p> inside <p> or <div> inside <p>).
 */
export function renderInlineMarkdownWithMath(raw: string): string {
  if (!raw) return "";

  // 0. Sanitize isolated single-symbol display math like $$\phi$$ or $$\gamma$$ into inline math
  let s = raw.replace(
    /\$\$(\s*\\[a-zA-Z]+(?:\^\{?[^}]*\}?|_[a-zA-Z0-9{}]+)?\s*)\$\$/g,
    "$$1$"
  );

  // 1. Extract block display math first if any
  const displayBlocks: string[] = [];
  s = s.replace(
    /(?:\$\$|\\{1,2}\[)([\s\S]*?)(?:\$\$|\\{1,2}\])/g,
    (_, math) => {
      const clean = cleanLatexString(math);
      // If the math expression is a short symbol or single variable (e.g. \phi, \gamma, \alpha, x),
      // render it as INLINE math instead of creating a huge full-width block inside inline text!
      const isShortInline =
        !clean.includes("\n") && clean.length <= 15 && !clean.includes("=");
      if (isShortInline) {
        try {
          return katex.renderToString(clean, {
            displayMode: false,
            throwOnError: false,
          });
        } catch {
          return `$${clean}$`;
        }
      }

      try {
        const rendered = katex.renderToString(clean, {
          displayMode: true,
          throwOnError: false,
        });
        const token = `@@DISPLAY_MATH_${displayBlocks.length}@@`;
        displayBlocks.push(
          `<span class="sol-math-block block my-2 text-center">${rendered}</span>`
        );
        return token;
      } catch {
        const token = `@@DISPLAY_MATH_${displayBlocks.length}@@`;
        displayBlocks.push(
          `<span class="sol-math-block block my-2 text-center">$$${math}$$</span>`
        );
        return token;
      }
    }
  );

  // 2. Extract and render inline math
  const inlineBlocks: string[] = [];
  s = s.replace(
    /(?:\\{1,2}\(([\s\S]*?)\\{1,2}\)|(?<!\$)\$([^\$\n]+)\$(?!\$))/g,
    (_, p1, p2) => {
      const c = p1 !== undefined ? p1 : p2;
      const clean = cleanLatexString(c);
      let rendered = "";
      try {
        rendered = katex.renderToString(clean, {
          displayMode: false,
          throwOnError: false,
        });
      } catch {
        rendered = `$${clean}$`;
      }
      const token = `@@INLINE_MATH_${inlineBlocks.length}@@`;
      inlineBlocks.push(rendered);
      return token;
    }
  );

  // 3. Format inline markdown (bold, italic, code)
  s = s.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/__(.*?)__/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^\*])\*([^\*]+)\*([^\*]|$)/g, "$1<em>$2</em>$3");
  s = s.replace(
    /`([^`]+)`/g,
    '<code class="px-1 py-0.5 rounded bg-muted text-xs font-mono">$1</code>'
  );

  // 4. Restore inline math
  s = s.replace(/@@INLINE_MATH_(\d+)@@/g, (_, idx) => {
    return inlineBlocks[parseInt(idx, 10)] || "";
  });

  // 5. Restore display math
  s = s.replace(/@@DISPLAY_MATH_(\d+)@@/g, (_, idx) => {
    return displayBlocks[parseInt(idx, 10)] || "";
  });

  return s;
}
