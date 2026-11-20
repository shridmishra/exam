"use client";

import React, { useMemo } from "react";
import {
  renderLatexInHtml,
  renderMarkdownWithMath,
  renderInlineMarkdownWithMath,
  safeRenderKatex,
} from "@/lib/math-utils";

export {
  renderLatexInHtml,
  renderMarkdownWithMath,
  renderInlineMarkdownWithMath,
};

interface MathRendererProps {
  content: string;
  isDisplay?: boolean;
  className?: string;
}

export const MathRenderer = React.memo(function MathRenderer({
  content,
  isDisplay = false,
  className,
}: MathRendererProps) {
  const rendered = useMemo(() => {
    if (!content) return "";
    let clean = content.trim();
    clean = clean.replace(/\\_/g, "_");
    clean = clean
      .replace(/&lt;/g, "<")
      .replace(/&gt;/g, ">")
      .replace(/&amp;/g, "&");

    return safeRenderKatex(clean, isDisplay);
  }, [content, isDisplay]);

  if (isDisplay) {
    return (
      <div
        className={`sol-math-block ${className || ""}`}
        dangerouslySetInnerHTML={{ __html: rendered }}
      />
    );
  }

  return (
    <span
      className={className}
      dangerouslySetInnerHTML={{ __html: rendered }}
    />
  );
});

export interface RichMathTextProps {
  text: string;
  className?: string;
  inline?: boolean;
  as?: "div" | "span";
}

/**
 * Parses mixed text, Markdown formatting, inline math ($...$), and block math ($$...$$).
 * When `inline` is true, renders as `<span>` and avoids block `<p>` wrappers,
 * preventing hydration errors when used inside `<p>` or inline containers.
 */
export const RichMathText = React.memo(function RichMathText({
  text,
  className,
  inline = false,
  as,
}: RichMathTextProps) {
  const html = useMemo(() => {
    if (!text) return "";
    return inline
      ? renderInlineMarkdownWithMath(text)
      : renderMarkdownWithMath(text);
  }, [text, inline]);

  if (!html) return null;

  const Tag = as || (inline ? "span" : "div");

  return (
    <Tag
      className={`rich-math-text ${className || ""}`.trim()}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
});
