import katex from "katex";

/**
 * High-performance bounded in-memory LRU/Map caches.
 * Eliminates redundant AST lexing, parsing, and regex tokenization
 * for identical mathematical expressions and markdown fragments.
 */
function createBoundedCache<T>(limit: number = 1000) {
  const cache = new Map<string, T>();
  return {
    get: (key: string): T | undefined => cache.get(key),
    set: (key: string, value: T): void => {
      if (cache.size >= limit) {
        const oldestKey = cache.keys().next().value;
        if (oldestKey !== undefined) cache.delete(oldestKey);
      }
      cache.set(key, value);
    },
    has: (key: string): boolean => cache.has(key),
  };
}

const katexCache = createBoundedCache<string>(2000);
const inlineMarkdownCache = createBoundedCache<string>(1000);
const markdownMathCache = createBoundedCache<string>(1000);
const latexHtmlCache = createBoundedCache<string>(500);

/**
 * Fast cached KaTeX rendering wrapper
 */
export function safeRenderKatex(cleanLatex: string, isDisplay: boolean): string {
  const cacheKey = (isDisplay ? "D:" : "I:") + cleanLatex;
  const cached = katexCache.get(cacheKey);
  if (cached !== undefined) return cached;

  try {
    const rendered = katex.renderToString(cleanLatex, {
      displayMode: isDisplay,
      throwOnError: false,
    });
    katexCache.set(cacheKey, rendered);
    return rendered;
  } catch (e) {
    console.warn("KaTeX render error:", e);
    const fallback = isDisplay ? `$$${cleanLatex}$$` : `$${cleanLatex}$`;
    katexCache.set(cacheKey, fallback);
    return fallback;
  }
}

/**
 * Sanitizes math content before passing to KaTeX.
 * Handles escaped characters, HTML entities, Greek letters, square roots, and degree symbols.
 */
export function cleanLatexString(raw: string): string {
  if (!raw) return "";
  let clean = raw.trim();

  // 1. Convert HTML line breaks to LaTeX line breaks inside math
  clean = clean.replace(/<br\s*\/?>/gi, " \\\\ ");

  // 2. Unescape underscores from JSON or markdown
  clean = clean.replace(/\\_/g, "_");

  // 3. HTML formatting tags inside math (convert to LaTeX formatting)
  clean = clean.replace(/<sub\b[^>]*>(.*?)<\/sub>/gi, "_{$1}");
  clean = clean.replace(/<sup\b[^>]*>(.*?)<\/sup>/gi, "^{$1}");
  clean = clean.replace(/<strong\b[^>]*>(.*?)<\/strong>/gi, "\\mathbf{$1}");
  clean = clean.replace(/<b\b[^>]*>(.*?)<\/b>/gi, "\\mathbf{$1}");
  clean = clean.replace(/<em\b[^>]*>(.*?)<\/em>/gi, "\\mathrm{$1}");
  clean = clean.replace(/<i\b[^>]*>(.*?)<\/i>/gi, "\\mathrm{$1}");
  clean = clean.replace(/<span\b[^>]*>(.*?)<\/span>/gi, "$1");
  clean = clean.replace(/<\/?[a-zA-Z][^>]*>/g, ""); // strip any remaining HTML tags

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

  // Strip raw checkmark inside math mode (badge checkmarks are rendered outside math mode in HTML)
  clean = clean.replace(/✓/g, "");

  // Normalize bullet and degree symbols
  clean = clean.replace(/[•·]/g, "\\cdot ");
  clean = clean.replace(/°/g, "^{\\circ}");

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

  // Percent sign: unescaped % acts as a comment in LaTeX, so escape to \%
  clean = clean.replace(/(?<!\\)%/g, "\\%");

  // Handle any remaining stray &amp; or &
  // In LaTeX math mode, bare '&' is an error unless it's in an aligned/matrix environment.
  if (!/\\begin\{(?:matrix|pmatrix|bmatrix|aligned|align|array|cases)\}/.test(clean)) {
    clean = clean.replace(/&amp;/g, "\\&").replace(/&(?![a-zA-Z#0-9]+;)/g, "\\&");
  } else {
    clean = clean.replace(/&amp;/g, "&");
  }

  return clean;
}

/**
 * Detects and extracts trailing safety/verification phrases from LaTeX math expressions
 * (e.g. `\quad (\text{Safe})`, `\quad \text{[Safe & watertight]}`, `\quad (\mathbf{Safe})`).
 * Converts them into clean, accessible HTML badges outside of KaTeX math mode.
 */
export function extractMathSafe(math: string): { cleanMath: string; trailingBadge: string } {
  let clean = math.trim();
  let trailingBadge = "";

  // 1. If HTML badge was already injected, extract it directly
  const htmlBadgeMatch = clean.match(
    /(?:\\quad|\s)*(?:\\text\{)?\s*(<span class="sol-badge-safe">[\s\S]*?<\/span>)\s*\}?\s*$/
  );
  if (htmlBadgeMatch) {
    clean = clean.slice(0, htmlBadgeMatch.index).trim();
    trailingBadge = htmlBadgeMatch[1];
    return { cleanMath: clean, trailingBadge };
  }

  // 2. Plain text / LaTeX parenthetical safety markers
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

/**
 * Ensures all tables in solutions are made fully responsive:
 * 1. Guarantees they are wrapped inside `<div class="sol-table-wrap overflow-x-auto my-3">`.
 * 2. Injects a calculated `min-width` based on column count so tables with 3-7 columns
 *    never squish character-by-character on mobile screens.
 */
export function makeTablesResponsive(html: string): string {
  if (!html || !html.includes("<table")) return html;

  let s = html;

  // 1. Ensure any table tag has an appropriate min-width calculated from its column count
  s = s.replace(/<table([\s\S]*?)<\/table>/gi, (tableFull) => {
    const tableTagMatch = tableFull.match(/<table([^>]*)>/i);
    if (!tableTagMatch) return tableFull;

    const attrs = tableTagMatch[1];

    // Determine column count from the first row
    const firstRowMatch = tableFull.match(/<tr[\s\S]*?<\/tr>/i);
    let colCount = 3;
    if (firstRowMatch) {
      const thMatches = firstRowMatch[0].match(/<th\b/gi);
      const tdMatches = firstRowMatch[0].match(/<td\b/gi);
      colCount = Math.max(1, thMatches ? thMatches.length : (tdMatches ? tdMatches.length : 3));
    }

    const minWidth = colCount <= 2 ? 300 : Math.max(540, colCount * 140);

    let updatedTable = tableFull;
    if (/style=[\"']/i.test(attrs)) {
      if (!/min-width/i.test(attrs)) {
        const newAttrs = attrs.replace(/(style=[\"'])([^\"']*)([\"'])/i, `$1$2; min-width: ${minWidth}px;$3`);
        updatedTable = updatedTable.replace(tableTagMatch[0], `<table${newAttrs}>`);
      }
    } else {
      updatedTable = updatedTable.replace(tableTagMatch[0], `<table style="min-width: ${minWidth}px;"${attrs}>`);
    }

    return updatedTable;
  });

  // 2. Normalize existing wrappers to include both `sol-table-wrap` and `overflow-x-auto`
  s = s.replace(
    /(<div[^>]*class=[\"'][^\"']*(?:overflow-x-auto|sol-table-wrap)[^\"']*[\"'][^>]*>\s*)(<table[\s\S]*?<\/table>)(\s*<\/div>)/gi,
    (m, divOpen, tbl, divClose) => {
      let updatedOpen = divOpen;
      if (!/sol-table-wrap/i.test(updatedOpen)) {
        updatedOpen = updatedOpen.replace(/class=[\"']([^\"']*)[\"']/i, 'class="$1 sol-table-wrap"');
      }
      if (!/overflow-x-auto/i.test(updatedOpen)) {
        updatedOpen = updatedOpen.replace(/class=[\"']([^\"']*)[\"']/i, 'class="$1 overflow-x-auto"');
      }
      return `${updatedOpen}${tbl}${divClose}`;
    }
  );

  // 3. Wrap any remaining unwrapped tables
  const stashedWrapped: string[] = [];
  s = s.replace(
    /<div[^>]*class=[\"'][^\"']*(?:overflow-x-auto|sol-table-wrap)[^\"']*[\"'][^>]*>[\s\S]*?<\/table>\s*<\/div>/gi,
    (m) => {
      const token = `@@STASHED_WRAPPED_TABLE_${stashedWrapped.length}@@`;
      stashedWrapped.push(m);
      return token;
    }
  );

  s = s.replace(/<table[\s\S]*?<\/table>/gi, (m) => {
    return `<div class="sol-table-wrap overflow-x-auto my-3">${m}</div>`;
  });

  s = s.replace(/@@STASHED_WRAPPED_TABLE_(\d+)@@/g, (_, idx) => {
    return stashedWrapped[parseInt(idx, 10)] || "";
  });

  return s;
}

/**
 * Enhances solution HTML with subtle, minimal muted green styling
 * for final answers, concluding results, and safety/design verifications.
 */
export function enhanceSolutionHtml(html: string): string {
  if (!html) return "";

  let s = html;

  // Protect <code> and <pre> blocks so safety badges are NEVER injected inside code/LaTeX
  const codeBlocks: string[] = [];
  s = s.replace(/<(code|pre)\b[^>]*>[\s\S]*?<\/\1>/gi, (m) => {
    const token = `@@PROTECTED_CODE_${codeBlocks.length}@@`;
    codeBlocks.push(m);
    return token;
  });

  // 1. Transform plain text / parenthesized safety and verification statements
  // e.g. "(Safe against Bligh creep)", "[Safe & watertight]", "(Safe)", "(OK)", "(Extremely Safe)"
  // into chic, minimal muted green status badges: <span class="sol-badge-safe"><span class="sol-badge-check">✓</span> ...</span>
  const safeParenRegex =
    /(?:[ \t]*)(\((?![^)]*?\b(?:un|not|in)safe\b)(?:Safe|safe|OK|O\.K\.|Hence safe|Highly Safe|Extremely Safe)(?:[^)]*?)\)|\[(?![^\]]*?\b(?:un|not|in)safe\b)(?:Safe|safe|OK|O\.K\.|Hence safe|Highly Safe|Extremely Safe)(?:[^\]]*?)\])(?:\.|\b)?/g;

  // Apply to text outside HTML tags
  const tagSplitRegex = /(<\/?[a-zA-Z][^>]*>)/g;
  const parts = s.split(tagSplitRegex);

  for (let i = 0; i < parts.length; i++) {
    if (parts[i].startsWith("<") && parts[i].endsWith(">")) {
      continue;
    }

    parts[i] = parts[i].replace(safeParenRegex, (_, inner) => {
      let text = inner.replace(/^[\(\[]|[\)\]]$/g, "").trim();
      if (text.startsWith("safe")) {
        text = "Safe" + text.slice(4);
      }
      return ` <span class="sol-badge-safe"><span class="sol-badge-check">✓</span> ${text}</span>`;
    });

    // Checkmarked safety phrases e.g. "✓ Safe", "✓ Highly Safe" outside existing spans
    parts[i] = parts[i].replace(
      /(?<!<span[^>]*>)(?:✓|&check;)\s*(Safe|safe|OK|O\.K\.|Hence safe|Highly Safe|Extremely Safe)(?:[^<\n]*)/g,
      (match) => {
        let text = match.replace(/^(?:✓|&check;)\s*/, "").trim();
        if (text.startsWith("safe")) text = "Safe" + text.slice(4);
        return `<span class="sol-badge-safe"><span class="sol-badge-check">✓</span> ${text}</span>`;
      }
    );

    parts[i] = parts[i].replace(
      /\b(Final Answer|Final Result|Ans|Answer)\s*:\s*/gi,
      (_, label) => {
        const cleanLabel = /ans\b|answer/i.test(label) ? "Ans" : "Final Answer";
        return `<span class="sol-ans-tag"><span class="sol-ans-tag-dot"></span>${cleanLabel}</span> `;
      }
    );
  }

  s = parts.join("");

  // Restore protected code blocks
  s = s.replace(/@@PROTECTED_CODE_(\d+)@@/g, (_, idx) => codeBlocks[parseInt(idx, 10)] || "");

  // 1b. Convert inline pseudo-bullets (<br>&bull; or <br>•) inside <li> into structured <ul class="sol-sublist">
  s = s.replace(
    /<li(\s+[^>]*)?>([\s\S]*?)<\/li>/gi,
    (orig, attrs = "", content) => {
      if (content.includes("<ul") || content.includes("<ol")) return orig;
      if (!/<br\s*\/?>\s*(?:&bull;|•)/i.test(content)) return orig;

      const parts = content.split(/<br\s*\/?>\s*(?:&bull;|•)\s*/i);
      const header = parts[0].trim();
      const subItems = parts.slice(1).map((p: string) => p.trim()).filter(Boolean);
      if (subItems.length === 0) return orig;

      const sublist = `<ul class="sol-sublist">${subItems
        .map((item: string) => `<li>${item}</li>`)
        .join("")}</ul>`;
      return `<li${attrs}>${header}${sublist}</li>`;
    }
  );

  // 2. Mark list items `<li>` and rows `.sol-item-row` that contain a final answer or safety badge
  s = s.replace(
    /<li(\s+[^>]*)?>([\s\S]*?)<\/li>/gi,
    (orig, attrs = "", content) => {
      const isFinal =
        content.includes('class="sol-badge-safe"') ||
        content.includes('class="sol-ans-tag"') ||
        content.includes('class="sol-math-badge-row"') ||
        /\b(?:Final Answer|Ans:)\b/i.test(content);

      if (!isFinal) return orig;

      if (/class="/i.test(attrs)) {
        if (/sol-item-final/i.test(attrs)) return orig;
        attrs = attrs.replace(/class="([^"]*)"/i, 'class="$1 sol-item-final"');
      } else {
        attrs = ` class="sol-item-final"${attrs}`;
      }
      return `<li${attrs}>${content}</li>`;
    }
  );

  s = s.replace(
    /(<div\b[^>]*\bclass="[^"]*sol-item-row[^"]*"[^>]*>)([\s\S]*?<\/div>\s*<\/div>)/gi,
    (orig, openingTag, innerAndClosing) => {
      const isFinal =
        innerAndClosing.includes('class="sol-badge-safe"') ||
        innerAndClosing.includes('class="sol-ans-tag"') ||
        innerAndClosing.includes('class="sol-math-badge-row"') ||
        /\b(?:Net Safe Bearing Capacity|Final Answer|Ans:)\b/i.test(innerAndClosing);

      if (!isFinal || openingTag.includes("sol-item-final")) return orig;

      const updatedTag = openingTag.replace(/class="([^"]*)"/i, 'class="$1 sol-item-final"');
      return `${updatedTag}${innerAndClosing}`;
    }
  );

  // 3. Ensure all solution tables are made fully responsive with min-widths and overflow containers
  if (s.includes("<table")) {
    s = makeTablesResponsive(s);
  }

  return s;
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

  const cachedHtml = latexHtmlCache.get(html);
  if (cachedHtml !== undefined) return cachedHtml;

  let s = html;

  const preserved: string[] = [];

  // Protect any already-rendered KaTeX math or blocks so inner MathML is never re-parsed
  s = s.replace(/<span class="katex"[\s\S]*?<\/span>\s*<\/span>/g, (m) => {
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
    const { cleanMath, trailingBadge } = extractMathSafe(clean);
    const isDisplay =
      cleanMath.includes("=") ||
      cleanMath.length > 20 ||
      cleanMath.includes("\\frac") ||
      cleanMath.includes("\\sqrt");
    const rendered = safeRenderKatex(cleanMath, isDisplay);
    const token = `@@PRESERVED_MATH_${preserved.length}@@`;
    preserved.push(
      isDisplay
        ? `<div class="sol-math-block">${rendered}${trailingBadge ? `<div class="sol-math-badge-row">${trailingBadge}</div>` : ""}</div>`
        : `<span class="sol-math-inline">${rendered}${trailingBadge ? ` ${trailingBadge}` : ""}</span>`
    );
    return token;
  });

  // 1. Extract and render display math blocks ($$...$$ and \[...\])
  s = s.replace(
    /(?:\$\$|\\{1,2}\[)([\s\S]*?)(?:\$\$|\\{1,2}\])/g,
    (_, math) => {
      const clean = cleanLatexString(math);
      const { cleanMath, trailingBadge } = extractMathSafe(clean);
      const rendered = safeRenderKatex(cleanMath, true);
      const token = `@@PRESERVED_MATH_${preserved.length}@@`;
      preserved.push(
        `<div class="sol-math-block">${rendered}${trailingBadge ? `<div class="sol-math-badge-row">${trailingBadge}</div>` : ""}</div>`
      );
      return token;
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
      /(?:(?<!\$)\$|\\{1,2}\()((?:[^\$\n]|\n(?!\n))+?)(?:(?<!\\)\$|\\{1,2}\))/g,
      (_, math) => {
        const clean = cleanLatexString(math);
        const { cleanMath, trailingBadge } = extractMathSafe(clean);
        const rendered = safeRenderKatex(cleanMath, false);
        const token = `@@PRESERVED_MATH_${preserved.length}@@`;
        preserved.push(rendered + (trailingBadge ? ` ${trailingBadge}` : ""));
        return token;
      }
    );

    // Also parse any bare LaTeX Greek letters or math symbols in text mode
    parts[i] = parts[i].replace(
      /(?<![\$\\])\\(alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|Delta)(?:_[a-zA-Z0-9{}]+)?(?![a-zA-Z\$])/g,
      (match) => {
        const clean = cleanLatexString(match);
        const rendered = safeRenderKatex(clean, false);
        const token = `@@PRESERVED_MATH_${preserved.length}@@`;
        preserved.push(rendered);
        return token;
      }
    );
  }

  s = parts.join("");

  // Enhance solution HTML (safety badges, final answer styling) BEFORE restoring preserved math
  // so that KaTeX-rendered MathML and inner spans are NEVER touched by text regexes
  s = enhanceSolutionHtml(s);

  // 3. Restore all preserved math and KaTeX blocks
  s = s.replace(/@@PRESERVED_MATH_(\d+)@@/g, (_, idx) => {
    return preserved[parseInt(idx, 10)] || "";
  });

  latexHtmlCache.set(html, s);
  return s;
}

/**
 * Synchronously renders freeform Markdown text (such as personal notes,
 * study scratchpad, comparison tables, and formula notes) into rich HTML
 * with full KaTeX mathematical typesetting.
 */
export function renderMarkdownWithMath(raw: string): string {
  if (!raw) return "";

  const cached = markdownMathCache.get(raw);
  if (cached !== undefined) return cached;

  let s = raw;
  const tokens: string[] = [];
  const codeBlocks: string[] = [];

  function addToken(html: string): string {
    const t = `@@KATEX_TOKEN_${tokens.length}@@`;
    tokens.push(html);
    return t;
  }

  // 0. Protect fenced code blocks (```...```) and inline code (`...`)
  s = s.replace(/```[\s\S]*?```/g, (m) => {
    const t = `@@PROTECTED_CODE_${codeBlocks.length}@@`;
    codeBlocks.push(m);
    return t;
  });
  s = s.replace(/`[^`\n]+`/g, (m) => {
    const t = `@@PROTECTED_CODE_${codeBlocks.length}@@`;
    codeBlocks.push(m);
    return t;
  });

  // 1. Extract Display Math ($$...$$ and \[...\]) FIRST
  s = s.replace(/(?:\$\$|\\{1,2}\[)([\s\S]*?)(?:\$\$|\\{1,2}\])/g, (_, math) => {
    const clean = cleanLatexString(math);
    const { cleanMath, trailingBadge } = extractMathSafe(clean);
    const rendered = safeRenderKatex(cleanMath, true);
    return addToken(
      `<div class="sol-math-block">${rendered}${
        trailingBadge ? `<div class="sol-math-badge-row">${trailingBadge}</div>` : ""
      }</div>`
    );
  });

  // 2. Extract Inline Math ($...$ and \(...\))
  s = s.replace(
    /(?:(?<!\$)\$|\\{1,2}\()((?:[^\$\n]|\n(?!\n))+?)(?:(?<!\\)\$|\\{1,2}\))/g,
    (_, math) => {
      const clean = cleanLatexString(math);
      const { cleanMath, trailingBadge } = extractMathSafe(clean);
      const rendered = safeRenderKatex(cleanMath, false);
      return addToken(rendered + (trailingBadge ? ` ${trailingBadge}` : ""));
    }
  );

  // 3. Extract remaining bare LaTeX symbols (Greek letters, etc.)
  s = s.replace(
    /(?<![\$\\])\\(alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|Delta)(?:_[a-zA-Z0-9{}]+)?(?![a-zA-Z\$])/g,
    (match) => {
      const clean = cleanLatexString(match);
      const rendered = safeRenderKatex(clean, false);
      return addToken(rendered);
    }
  );

  // 4. Process lines (Markdown tables, lists, headings, paragraphs)
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
    t = t.replace(/(^|[^\*])\*([^\*]+)\*([^\*]|$)/g, '$1<span class="sol-item-label">$2</span>$3');
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

    // Pass through standalone display math tokens directly without wrapping in <p>
    if (/^@@KATEX_TOKEN_\d+@@$/.test(trimmed)) {
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
      const minTableWidth = headers.length <= 2 ? 300 : Math.max(540, headers.length * 140);
      out.push(
        `<div class="sol-table-wrap overflow-x-auto my-3"><table class="sol-table" style="table-layout: fixed; width: 100%; min-width: ${minTableWidth}px;"><thead><tr>${thHtml}</tr></thead><tbody>${trHtml}</tbody></table></div>`
      );
      continue;
    }

    // Bullet lists (support -, *, •, and &bull;)
    if (/^(?:[-*]|•|&bull;)\s+/.test(trimmed)) {
      const listItems: string[] = [];
      while (i < lines.length && /^(?:[-*]|•|&bull;)\s+/.test(lines[i].trim())) {
        listItems.push(
          `<li>${formatInline(lines[i].trim().replace(/^(?:[-*]|•|&bull;)\s+/, ""))}</li>`
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

    // Normal paragraph or HTML blocks
    if (trimmed.startsWith("<") && (trimmed.endsWith(">") || trimmed.includes("</"))) {
      out.push(formatInline(trimmed));
    } else {
      out.push(`<p class="my-1.5 leading-relaxed">${formatInline(trimmed)}</p>`);
    }
    i++;
  }

  let finalHtml = out.join("\n");

  // Apply safety badges & final answer styling BEFORE restoring tokens
  finalHtml = enhanceSolutionHtml(finalHtml);

  // Restore protected code
  finalHtml = finalHtml.replace(/@@PROTECTED_CODE_(\d+)@@/g, (_, idx) => {
    return codeBlocks[parseInt(idx, 10)] || "";
  });

  // Restore KaTeX tokens
  finalHtml = finalHtml.replace(/@@KATEX_TOKEN_(\d+)@@/g, (_, idx) => {
    return tokens[parseInt(idx, 10)] || "";
  });

  markdownMathCache.set(raw, finalHtml);
  return finalHtml;
}

/**
 * Synchronously renders inline markdown and LaTeX math (for question text,
 * list items, parameter items) WITHOUT wrapping in outer <p> or <div> blocks.
 * Guarantees zero invalid HTML nesting (<p> inside <p> or <div> inside <p>).
 */
export function renderInlineMarkdownWithMath(raw: string): string {
  if (!raw) return "";

  const cached = inlineMarkdownCache.get(raw);
  if (cached !== undefined) return cached;

  let s = raw;
  const tokens: string[] = [];
  const codeBlocks: string[] = [];

  function addToken(html: string): string {
    const t = `@@INLINE_TOKEN_${tokens.length}@@`;
    tokens.push(html);
    return t;
  }

  // Protect code spans
  s = s.replace(/`([^`\n]+)`/g, (_, code) => {
    const t = `@@PROTECTED_CODE_${codeBlocks.length}@@`;
    codeBlocks.push(`<code class="px-1 py-0.5 rounded bg-muted text-xs font-mono">${code}</code>`);
    return t;
  });

  // Display math inside inline container: convert to inline or inline-block span
  s = s.replace(/(?:\$\$|\\{1,2}\[)([\s\S]*?)(?:\$\$|\\{1,2}\])/g, (_, math) => {
    const clean = cleanLatexString(math);
    const { cleanMath, trailingBadge } = extractMathSafe(clean);
    const isShortInline = !cleanMath.includes("\n") && cleanMath.length <= 15 && !cleanMath.includes("=");
    if (isShortInline) {
      const rendered = safeRenderKatex(cleanMath, false);
      return addToken(rendered + (trailingBadge ? ` ${trailingBadge}` : ""));
    }
    const rendered = safeRenderKatex(cleanMath, true);
    return addToken(
      `<span class="sol-math-block block my-2 text-center">${rendered}${
        trailingBadge ? `<span class="sol-math-badge-row block">${trailingBadge}</span>` : ""
      }</span>`
    );
  });

  // Inline math
  s = s.replace(
    /(?:(?<!\$)\$|\\{1,2}\()((?:[^\$\n]|\n(?!\n))+?)(?:(?<!\\)\$|\\{1,2}\))/g,
    (_, math) => {
      const clean = cleanLatexString(math);
      const { cleanMath, trailingBadge } = extractMathSafe(clean);
      const rendered = safeRenderKatex(cleanMath, false);
      return addToken(rendered + (trailingBadge ? ` ${trailingBadge}` : ""));
    }
  );

  // Greek letters & symbols
  s = s.replace(
    /(?<![\$\\])\\(alpha|beta|gamma|delta|epsilon|varepsilon|theta|mu|pi|sigma|tau|phi|omega|Delta)(?:_[a-zA-Z0-9{}]+)?(?![a-zA-Z\$])/g,
    (match) => {
      const clean = cleanLatexString(match);
      const rendered = safeRenderKatex(clean, false);
      return addToken(rendered);
    }
  );

  // Markdown formatting
  s = s.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/__(.*?)__/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^\*])\*([^\*]+)\*([^\*]|$)/g, '$1<span class="sol-item-label">$2</span>$3');

  s = enhanceSolutionHtml(s);

  // Restore code
  s = s.replace(/@@PROTECTED_CODE_(\d+)@@/g, (_, idx) => codeBlocks[parseInt(idx, 10)] || "");

  // Restore tokens
  s = s.replace(/@@INLINE_TOKEN_(\d+)@@/g, (_, idx) => tokens[parseInt(idx, 10)] || "");

  inlineMarkdownCache.set(raw, s);
  return s;
}
