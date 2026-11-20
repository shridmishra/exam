"use client";

import React, { useState, useMemo } from "react";
import {
  Search01Icon,
  Cancel01Icon,
  ArrowReloadHorizontalIcon,
  Copy01Icon,
} from "@/components/ui/icons";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { MathRenderer } from "@/components/common/math-renderer";
import { toast } from "@/components/ui/sonner";
import { MasterFormula } from "@/types";
import { cn } from "@/lib/utils";

interface FormulasViewProps {
  formulas: MasterFormula[];
  unitTitles: Record<string, string>;
}

export function FormulasView({ formulas, unitTitles }: FormulasViewProps) {
  const [selectedUnit, setSelectedUnit] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState<string>("");

  const filteredFormulas = useMemo(() => {
    return formulas.filter((f) => {
      // Unit filter
      if (selectedUnit !== "all" && String(f.unit) !== selectedUnit) {
        return false;
      }

      // Search filter
      if (searchQuery) {
        const query = searchQuery.toLowerCase();
        const text =
          `${f.title} ${f.notes} ${f.latex_raw} ${f.params.map((p) => `${p.sym} ${p.name}`).join(" ")}`.toLowerCase();
        if (!text.includes(query)) return false;
      }

      return true;
    });
  }, [formulas, selectedUnit, searchQuery]);

  const handleReset = () => {
    setSelectedUnit("all");
    setSearchQuery("");
    toast.info("Formula filters reset");
  };

  const handleCopyFormula = (formula: MasterFormula) => {
    const textToCopy = `${formula.title}\n${formula.latex_main}${
      formula.latex_sub ? `\n${formula.latex_sub}` : ""
    }`;
    navigator.clipboard.writeText(textToCopy);
    toast.success("Formula copied to clipboard", {
      description: formula.title,
    });
  };

  return (
    <div className="space-y-6">
      {/* Title */}
      <div>
        <h1 className="text-lg sm:text-xl font-bold tracking-tight text-foreground">
          Master Formulas
        </h1>
      </div>

      {/* Refined Minimal Control Bar */}
      <div className="flex flex-col gap-3 rounded-2xl bg-card p-3 sm:p-4 shadow-xs sm:flex-row sm:items-center sm:justify-between">
        {/* Left: Unit Pills Segmented Control */}
        <div className="flex min-w-0 items-center gap-2">
          <span className="w-10 shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
            Unit
          </span>
          <div className="no-scrollbar inline-flex min-w-0 items-center gap-0.5 overflow-x-auto rounded-lg bg-secondary/70 dark:bg-secondary/50 p-0.5 ring-1 ring-border/25 overscroll-x-contain">
            {["all", "1", "2", "3", "4", "5"].map((u) => (
              <Button
                key={u}
                type="button"
                variant="ghost"
                size="sm"
                onClick={() => setSelectedUnit(u)}
                className={cn(
                  "h-7 shrink-0 whitespace-nowrap rounded-md px-2.5 text-xs font-medium select-none transition-all",
                  selectedUnit === u
                    ? "bg-card text-foreground dark:bg-filter-active dark:text-filter-active-foreground font-semibold shadow-2xs ring-1 ring-border/20"
                    : "bg-transparent text-muted-foreground hover:bg-card/40 dark:hover:bg-card/50 hover:text-foreground"
                )}
              >
                {u === "all" ? "All" : `Unit ${u}`}
              </Button>
            ))}
          </div>
        </div>

        {/* Right: Counter & Search */}
        <div className="flex items-center gap-2 w-full sm:w-auto">
          <div className="relative flex-1 sm:w-56 md:w-64">
            <Search01Icon className="pointer-events-none absolute left-3 top-1/2 h-3.5 w-3.5 -translate-y-1/2 text-muted-foreground" />
            <Input
              type="text"
              placeholder="Search..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="h-9 rounded-xl border-0 bg-secondary/50 pl-9 pr-8 text-xs sm:text-[13px] shadow-2xs transition-all hover:bg-secondary/70 focus:bg-secondary/90"
            />
            {searchQuery && (
              <Button
                variant="ghost"
                size="icon"
                onClick={() => setSearchQuery("")}
                className="absolute right-1.5 top-1/2 h-6 w-6 -translate-y-1/2 rounded-md text-muted-foreground hover:text-foreground"
                title="Clear search"
              >
                <Cancel01Icon className="h-3.5 w-3.5" />
              </Button>
            )}
          </div>

          <Badge
            variant="subtle"
            className="h-9 shrink-0 rounded-xl bg-secondary/70 px-2.5 sm:px-3 text-xs font-medium tabular-nums text-foreground whitespace-nowrap"
          >
            {filteredFormulas.length === formulas.length
              ? `${formulas.length} formulas`
              : `${filteredFormulas.length} / ${formulas.length}`}
          </Badge>

          {(selectedUnit !== "all" || searchQuery) && (
            <Button
              variant="ghost"
              size="sm"
              onClick={handleReset}
              className="h-9 shrink-0 gap-1 rounded-xl px-2.5 sm:px-3 text-xs font-medium text-muted-foreground hover:bg-secondary hover:text-foreground"
            >
              <ArrowReloadHorizontalIcon className="h-3.5 w-3.5" />
              <span>Reset</span>
            </Button>
          )}
        </div>
      </div>

      {/* Zero match empty state */}
      {filteredFormulas.length === 0 && (
        <div className="flex flex-col items-center justify-center rounded-2xl bg-card p-10 text-center shadow-xs">
          <p className="text-sm font-semibold text-foreground">
            No formulas match your filters
          </p>
          <Button
            variant="secondary"
            size="sm"
            onClick={handleReset}
            className="mt-3 text-xs"
          >
            Reset Filters
          </Button>
        </div>
      )}

      {/* Cards Grid */}
      <div className="grid grid-cols-1 gap-4 sm:gap-5 md:grid-cols-2">
        {filteredFormulas.map((formula) => (
          <Card key={formula.id} className="shadow-xs">
            <CardHeader className="p-3.5 sm:p-5 pb-2">
              <div className="flex flex-wrap items-center justify-between gap-1.5 sm:gap-2 mb-1.5">
                <Badge variant="subtle" className="text-xs">
                  Unit {formula.unit} &bull; {unitTitles[String(formula.unit)] || `Unit ${formula.unit}`}
                </Badge>
                {formula.frequency && (
                  <Badge variant="repeat3x" className="text-xs font-semibold">
                    {formula.frequency.replace(/\s*\([^)]*\)/g, "").trim()}
                  </Badge>
                )}
              </div>
              <div className="flex items-start justify-between gap-2">
                <CardTitle className="text-sm sm:text-base font-semibold text-foreground leading-snug">
                  {formula.title}
                </CardTitle>
                <Button
                  type="button"
                  variant="ghost"
                  size="icon"
                  onClick={() => handleCopyFormula(formula)}
                  className="h-7 w-7 shrink-0 text-muted-foreground/60 hover:text-foreground"
                  title="Copy formula LaTeX to clipboard"
                  aria-label="Copy formula"
                >
                  <Copy01Icon className="h-3.5 w-3.5" />
                </Button>
              </div>
            </CardHeader>

            <CardContent className="p-3.5 sm:p-5 pt-1 sm:pt-2 space-y-3">
              {/* Formula Equations Display (Merged with normal card BG, Unified UI) */}
              <div className="space-y-2 py-1 text-center">
                <div className="overflow-x-auto no-scrollbar py-1 text-foreground overscroll-x-contain">
                  <MathRenderer
                    content={formula.latex_main}
                    isDisplay={true}
                    className="!bg-transparent !p-0 !m-0 text-foreground"
                  />
                </div>

                {formula.latex_sub && (
                  <div className="overflow-x-auto no-scrollbar py-1 text-foreground overscroll-x-contain">
                    <MathRenderer
                      content={formula.latex_sub}
                      isDisplay={true}
                      className="!bg-transparent !p-0 !m-0 text-foreground"
                    />
                  </div>
                )}
              </div>

              {/* Parameters Breakdown */}
              {formula.params && formula.params.length > 0 && (
                <div className="mt-3 space-y-1.5 pt-2">
                  <span className="text-[11px] sm:text-xs font-bold uppercase tracking-wider text-muted-foreground block">
                    Parameters &amp; Units:
                  </span>
                  <div className="grid grid-cols-1 divide-y divide-border/20 text-xs sm:text-[13px]">
                    {formula.params.map((p, idx) => (
                      <div
                        key={idx}
                        className="flex items-start gap-2.5 py-1.5"
                      >
                        <span className="w-9 sm:w-11 shrink-0 font-semibold text-foreground text-left">
                          <MathRenderer content={p.sym} isDisplay={false} />
                        </span>
                        <span className="flex-1 text-left text-muted-foreground leading-relaxed break-words">
                          {p.name}
                        </span>
                        {p.unit && (
                          <span className="shrink-0 self-start text-[11px] sm:text-xs text-muted-foreground/90 bg-secondary px-2 py-0.5 rounded-md font-mono tabular-nums">
                            {p.unit}
                          </span>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Engineering Notes */}
              {formula.notes && (
                <div className="rounded-xl bg-secondary/40 p-3 text-xs sm:text-[13px] text-muted-foreground leading-relaxed">
                  <strong className="text-foreground font-semibold">Notes: </strong>
                  {formula.notes}
                </div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
