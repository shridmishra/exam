"use client";

import React from "react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

interface YearPillsProps {
  years: string[];
  counts: Record<string, { done: number; total: number }>;
  activeYear: string;
  onSelectYear: (year: string) => void;
}

export function YearPills({
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
    <div className="flex items-center gap-1.5 sm:gap-2 flex-nowrap shrink-0">
      {years.map((year) => {
        const stats = counts[year] || { done: 0, total: 0 };
        const isActive = activeYear === year;

        return (
          <Button
            key={year}
            type="button"
            variant="ghost"
            onClick={() => onSelectYear(year)}
            className={`h-auto flex items-center gap-1 sm:gap-1.5 rounded-full px-2 sm:px-2.5 py-1 text-xs shrink-0 whitespace-nowrap transition-all hover:bg-secondary/80 focus:outline-none focus:ring-2 focus:ring-ring ${
              isActive
                ? "bg-secondary font-semibold text-foreground shadow-2xs"
                : "bg-transparent text-muted-foreground hover:bg-secondary/60"
            }`}
            title={`View ${year} examination paper`}
          >
            <Badge variant={getBadgeVariant(year)} className="text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5">
              {year}
            </Badge>
            <span className="tabular-nums text-xs sm:text-[13px] text-foreground/80">
              {stats.done}/{stats.total}
            </span>
          </Button>
        );
      })}
    </div>
  );
}
