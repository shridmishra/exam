"use client";

import React, { useMemo } from "react";
import { renderLatexInHtml } from "@/lib/math-utils";

interface SolutionViewerProps {
  html: string;
}

export function SolutionViewer({ html }: SolutionViewerProps) {
  // Synchronously transform LaTeX within the solution HTML into KaTeX HTML.
  // Rendering during useMemo guarantees:
  // 1. Zero flash of raw unrendered LaTeX strings
  // 2. Full hydration immunity with zero virtual DOM mismatches
  // 3. React re-renders never wipe out KaTeX output
  const renderedHtml = useMemo(() => {
    return renderLatexInHtml(html);
  }, [html]);

  return (
    <div
      className="solution-viewer text-sm sm:text-[14.5px] leading-relaxed text-foreground max-w-none space-y-3"
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
}
