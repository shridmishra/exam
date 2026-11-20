"use client";

import React, { useMemo } from "react";
import { renderLatexInHtml } from "@/lib/math-utils";

interface SolutionViewerProps {
  html: string;
}

export const SolutionViewer = React.memo(function SolutionViewer({ html }: SolutionViewerProps) {
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
      className="solution-viewer text-sm sm:text-[14.5px] leading-relaxed text-foreground w-full min-w-0 max-w-full space-y-3"
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
    />
  );
});
