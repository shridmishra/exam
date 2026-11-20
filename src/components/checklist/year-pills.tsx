"use client";

import React from "react";
import { motion } from "framer-motion";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { filterSpringTransition } from "@/lib/motion";

interface YearPillsProps {
  years: string[];
  counts: Record<string, { done: number; total: number }>;
  activeYear: string;
  onSelectYear: (year: string) => void;
}

export const YearPills = React.memo(function YearPills({
  years,
  counts,
  activeYear,
  onSelectYear,
}: YearPillsProps) {
  const getBadgeVariant = (year: string) => {
    switch (year) {
      case "2025":
        return "year2025";
      case "2024":
        return "year2024";
      case "2023":
        return "year2023";
      case "2022":
        return "year2022";
      case "2019":
        return "year2019";
      default:
        return "secondary";
    }
  };

  return (
    <div className="flex items-center gap-1.5 sm:gap-2 flex-nowrap shrink-0 relative">
      {years.map((year) => {
        const stats = counts[year] || { done: 0, total: 0 };
        const isActive = activeYear === year;

        return (
          <Button
            key={year}
            type="button"
            variant="ghost"
            onClick={() => onSelectYear(year)}
            className={cn(
              "relative h-auto flex items-center gap-1 sm:gap-1.5 rounded-full px-2 sm:px-2.5 py-1 text-xs shrink-0 whitespace-nowrap transition-colors focus:outline-none focus:ring-2 focus:ring-ring select-none",
              isActive
                ? "font-semibold text-foreground bg-transparent"
                : "bg-transparent text-muted-foreground hover:bg-secondary/60"
            )}
            title={`View ${year} examination paper`}
          >
            {isActive && (
              <motion.div
                layoutId="checklist-year-pills-active"
                className="absolute inset-0 rounded-full bg-secondary shadow-2xs ring-1 ring-border/20"
                transition={filterSpringTransition}
              />
            )}
            <span className="relative z-10 flex items-center gap-1 sm:gap-1.5">
              <Badge variant={getBadgeVariant(year)} className="font-heading text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5">
                {year}
              </Badge>
              <span className="font-heading tabular-nums text-xs sm:text-[13px] text-foreground/80">
                {stats.done}/{stats.total}
              </span>
            </span>
          </Button>
        );
      })}
    </div>
  );
});
