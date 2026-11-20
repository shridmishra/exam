"use client";

import React from "react";
import { motion } from "framer-motion";
import {
  Search01Icon,
  Cancel01Icon,
  RotateCcwIcon,
  ChevronsDownIcon,
  ChevronsUpIcon,
} from "@/components/ui/icons";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { ChecklistFilters } from "@/types";
import { cn } from "@/lib/utils";
import { filterSpringTransition } from "@/lib/motion";

interface ControlPanelProps {
  filters: ChecklistFilters;
  setFilters: React.Dispatch<React.SetStateAction<ChecklistFilters>>;
  matchCount: number;
  totalCount: number;
  allExpanded: boolean;
  onToggleExpandAll: () => void;
  onResetFilters: () => void;
  availableYears?: string[];
}

interface FilterButtonProps {
  active: boolean;
  onClick: () => void;
  children: React.ReactNode;
  title?: string;
  className?: string;
  layoutId?: string;
}

const pillTrackClassName =
  "no-scrollbar inline-flex min-w-0 items-center gap-0.5 overflow-x-auto rounded-lg bg-secondary/70 dark:bg-secondary/50 p-0.5 ring-1 ring-border/25 overscroll-x-contain";

const FilterButton = React.memo(function FilterButton({
  active,
  onClick,
  children,
  title,
  className,
  layoutId,
}: FilterButtonProps) {
  return (
    <Button
      type="button"
      variant="ghost"
      size="sm"
      onClick={onClick}
      title={title}
      className={cn(
        "relative font-heading h-7 px-2 text-xs font-medium rounded-md transition-colors select-none shrink-0 whitespace-nowrap",
        active
          ? "text-foreground dark:text-filter-active-foreground font-semibold bg-transparent"
          : "bg-transparent text-muted-foreground hover:text-foreground hover:bg-card/40 dark:hover:bg-card/50",
        className
      )}
    >
      {active && layoutId && (
        <motion.div
          layoutId={layoutId}
          className="absolute inset-0 rounded-md bg-card text-foreground dark:bg-filter-active dark:text-filter-active-foreground shadow-2xs ring-1 ring-border/20"
          transition={filterSpringTransition}
        />
      )}
      {active && !layoutId && (
        <div className="absolute inset-0 rounded-md bg-card text-foreground dark:bg-filter-active dark:text-filter-active-foreground shadow-2xs ring-1 ring-border/20" />
      )}
      <span className="relative z-10">{children}</span>
    </Button>
  );
});

export const ControlPanel = React.memo(function ControlPanel({
  filters,
  setFilters,
  matchCount,
  totalCount,
  allExpanded,
  onToggleExpandAll,
  onResetFilters,
  availableYears,
}: ControlPanelProps) {
  const yearOptions = ["all", ...(availableYears || ["2025", "2024", "2023", "2022"])];
  const has5x = Boolean(availableYears && availableYears.length >= 5);
  const repeatTiers = has5x ? ["5x", "4x", "3x", "2x"] : ["4x", "3x", "2x"];

  const hasActiveFilters =
    filters.year !== "all" ||
    filters.unit !== "all" ||
    filters.repeated !== "all" ||
    filters.type !== "all" ||
    filters.marks !== "all" ||
    filters.status !== "all" ||
    filters.search !== "";

  return (
    <div className="rounded-2xl bg-card p-3.5 sm:p-5 shadow-xs transition-all">
      {/* Top Utility & Search Toolbar */}
      <div className="flex flex-col gap-2.5 sm:flex-row sm:items-center sm:justify-between">
        <div className="relative w-full sm:w-64 md:w-72">
          <Search01Icon className="pointer-events-none absolute left-3 top-1/2 h-3.5 w-3.5 -translate-y-1/2 text-muted-foreground" />
          <Input
            type="text"
            placeholder="Search questions..."
            aria-label="Search questions"
            value={filters.search}
            onChange={(e) =>
              setFilters((prev) => ({ ...prev, search: e.target.value }))
            }
            className="font-heading h-9 rounded-lg border-0 bg-secondary/40 pl-9 pr-8 text-xs transition-all hover:bg-secondary/60 focus:bg-secondary/80 focus:ring-1 focus:ring-ring"
          />
          {filters.search && (
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setFilters((prev) => ({ ...prev, search: "" }))}
              className="absolute right-1 top-1/2 h-6 w-6 -translate-y-1/2 rounded-md text-muted-foreground hover:text-foreground"
              title="Clear search"
              aria-label="Clear search"
            >
              <Cancel01Icon className="h-3.5 w-3.5" />
            </Button>
          )}
        </div>

        <div className="flex items-center justify-between sm:justify-end gap-2 w-full sm:w-auto">
          <Badge
            variant="subtle"
            className="font-heading h-9 rounded-lg bg-secondary/60 px-2.5 sm:px-3 text-xs font-medium tabular-nums text-foreground/90 shrink-0"
          >
            {matchCount === totalCount
              ? `${totalCount} questions`
              : `${matchCount} of ${totalCount}`}
          </Badge>

          <div className="flex items-center gap-1.5 shrink-0">
            <Button
              variant="secondary"
              size="sm"
              onClick={onToggleExpandAll}
              className="font-heading h-9 gap-1.5 rounded-lg px-2.5 sm:px-3 text-xs font-medium text-foreground hover:bg-secondary/80"
            >
              {allExpanded ? (
                <>
                  <ChevronsUpIcon className="h-3.5 w-3.5" />
                  <span>Collapse All</span>
                </>
              ) : (
                <>
                  <ChevronsDownIcon className="h-3.5 w-3.5" />
                  <span>Expand All</span>
                </>
              )}
            </Button>

            {hasActiveFilters && (
              <Button
                variant="ghost"
                size="sm"
                onClick={onResetFilters}
                className="font-heading h-9 gap-1.5 rounded-lg px-2 sm:px-2.5 text-xs font-medium text-muted-foreground hover:bg-secondary hover:text-foreground"
              >
                <RotateCcwIcon className="h-3.5 w-3.5" />
                <span>Reset</span>
              </Button>
            )}
          </div>
        </div>
      </div>

      {/* Subtle Divider */}
      <div className="my-3.5 h-px bg-border/40" />

      {/* Symmetrical 3-Column Grid for All 6 Filter Dimensions */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-x-5 gap-y-3.5">
        {/* Column 1: Scope & Syllabus */}
        <div className="flex flex-col gap-3">
          {/* Dimension 1: Year */}
          <div className="flex min-w-0 items-center gap-2">
            <span className="font-heading w-[62px] min-w-[62px] shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
              Year
            </span>
            <div className={pillTrackClassName}>
              {yearOptions.map((y) => (
                <FilterButton
                  key={y}
                  active={filters.year === y}
                  onClick={() => setFilters((prev) => ({ ...prev, year: y }))}
                  layoutId="cp-filter-year"
                >
                  {y === "all" ? "All" : y}
                </FilterButton>
              ))}
            </div>
          </div>

          {/* Dimension 2: Unit */}
          <div className="flex min-w-0 items-center gap-2">
            <span className="font-heading w-[62px] min-w-[62px] shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
              Unit
            </span>
            <div className={pillTrackClassName}>
              {["all", "1", "2", "3", "4", "5"].map((u) => (
                <FilterButton
                  key={u}
                  active={filters.unit === u}
                  onClick={() => setFilters((prev) => ({ ...prev, unit: u }))}
                  layoutId="cp-filter-unit"
                >
                  {u === "all" ? "All" : `Unit ${u}`}
                </FilterButton>
              ))}
            </div>
          </div>
        </div>

        {/* Column 2: Intelligence & Format */}
        <div className="flex flex-col gap-3">
          {/* Dimension 3: Repeated */}
          <div className="flex min-w-0 items-center gap-2">
            <span className="font-heading w-[62px] min-w-[62px] shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
              Repeated
            </span>
            <div className={pillTrackClassName}>
              <FilterButton
                active={filters.repeated === "all"}
                onClick={() => setFilters((prev) => ({ ...prev, repeated: "all" }))}
                layoutId="cp-filter-repeated"
              >
                All
              </FilterButton>
              <FilterButton
                active={filters.repeated === "repeated"}
                onClick={() =>
                  setFilters((prev) => ({
                    ...prev,
                    repeated: "repeated",
                    year: "all",
                    type: "all",
                    marks: "all",
                  }))
                }
                title="All repeated questions (4x, 3x, 2x)"
                layoutId="cp-filter-repeated"
              >
                Most Repeated
              </FilterButton>
              {repeatTiers.map((r) => (
                <FilterButton
                  key={r}
                  active={filters.repeated === r}
                  onClick={() =>
                    setFilters((prev) => ({
                      ...prev,
                      repeated: r,
                      year: "all",
                      type: "all",
                      marks: "all",
                    }))
                  }
                  title={`Repeated across ${r[0]} exam papers`}
                  layoutId="cp-filter-repeated"
                >
                  {r}
                </FilterButton>
              ))}
            </div>
          </div>

          {/* Dimension 4: Type */}
          <div className="flex min-w-0 items-center gap-2">
            <span className="font-heading w-[62px] min-w-[62px] shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
              Type
            </span>
            <div className={pillTrackClassName}>
              {[
                { id: "all", label: "All" },
                { id: "Theory", label: "Theory" },
                { id: "Numerical", label: "Numerical" },
                { id: "Derivation", label: "Derivation" },
              ].map((t) => (
                <FilterButton
                  key={t.id}
                  active={filters.type === t.id}
                  onClick={() => setFilters((prev) => ({ ...prev, type: t.id }))}
                  layoutId="cp-filter-type"
                >
                  {t.label}
                </FilterButton>
              ))}
            </div>
          </div>
        </div>

        {/* Column 3: Workflow & Priority */}
        <div className="flex flex-col gap-3 md:col-span-2 xl:col-span-1">
          {/* Dimension 5: Status */}
          <div className="flex min-w-0 items-center gap-2">
            <span className="font-heading w-[62px] min-w-[62px] shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
              Status
            </span>
            <div className={pillTrackClassName}>
              {[
                { id: "all", label: "All" },
                { id: "incomplete", label: "Incomplete" },
                { id: "completed", label: "Completed" },
                { id: "starred", label: "Starred" },
                { id: "later", label: "Later" },
              ].map((st) => (
                <FilterButton
                  key={st.id}
                  active={filters.status === st.id}
                  onClick={() => setFilters((prev) => ({ ...prev, status: st.id }))}
                  layoutId="cp-filter-status"
                >
                  {st.label}
                </FilterButton>
              ))}
            </div>
          </div>

          {/* Dimension 6: Marks */}
          <div className="flex min-w-0 items-center gap-2">
            <span className="font-heading w-[62px] min-w-[62px] shrink-0 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground/80 select-none">
              Marks
            </span>
            <div className={pillTrackClassName}>
              {[
                { id: "all", label: "All" },
                { id: "2", label: "2M" },
                { id: "3", label: "3M" },
                { id: "7", label: "7M/6M" },
              ].map((m) => (
                <FilterButton
                  key={m.id}
                  active={filters.marks === m.id}
                  onClick={() => setFilters((prev) => ({ ...prev, marks: m.id }))}
                  layoutId="cp-filter-marks"
                >
                  {m.label}
                </FilterButton>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
});
