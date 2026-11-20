import React from "react";
import { Skeleton } from "@/components/ui/skeleton";

export function ChecklistSkeleton() {
  return (
    <div className="space-y-6">
      {/* Control Panel Skeleton */}
      <div className="rounded-2xl bg-card p-3.5 sm:p-4 shadow-xs">
        {/* Top Toolbar */}
        <div className="flex flex-col gap-2.5 sm:flex-row sm:items-center sm:justify-between">
          <div className="relative flex-1">
            <Skeleton className="h-9 w-full rounded-lg" />
          </div>

          <div className="flex items-center justify-between sm:justify-end gap-2 w-full sm:w-auto">
            <Skeleton className="h-9 w-28 rounded-lg" />
            <Skeleton className="h-9 w-28 rounded-lg" />
          </div>
        </div>

        {/* Subtle Divider */}
        <div className="my-3.5 h-px bg-border/40" />

        {/* Symmetrical 3-Column Filter Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-x-5 gap-y-3.5">
          {/* Column 1: Scope & Syllabus */}
          <div className="flex flex-col gap-3">
            <div className="flex items-center gap-2">
              <Skeleton className="h-4 w-[62px] shrink-0" />
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4, 5].map((i) => (
                  <Skeleton key={i} className="h-7 w-12 rounded-md" />
                ))}
              </div>
            </div>

            <div className="flex items-center gap-2">
              <Skeleton className="h-4 w-[62px] shrink-0" />
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4, 5, 6].map((i) => (
                  <Skeleton key={i} className="h-7 w-12 rounded-md" />
                ))}
              </div>
            </div>
          </div>

          {/* Column 2: Intelligence & Format */}
          <div className="flex flex-col gap-3">
            <div className="flex items-center gap-2">
              <Skeleton className="h-4 w-[62px] shrink-0" />
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4].map((i) => (
                  <Skeleton key={i} className="h-7 w-14 rounded-md" />
                ))}
              </div>
            </div>

            <div className="flex items-center gap-2">
              <Skeleton className="h-4 w-[62px] shrink-0" />
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4].map((i) => (
                  <Skeleton key={i} className="h-7 w-16 rounded-md" />
                ))}
              </div>
            </div>
          </div>

          {/* Column 3: Workflow & Priority */}
          <div className="flex flex-col gap-3">
            <div className="flex items-center gap-2">
              <Skeleton className="h-4 w-[62px] shrink-0" />
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4].map((i) => (
                  <Skeleton key={i} className="h-7 w-16 rounded-md" />
                ))}
              </div>
            </div>

            <div className="flex items-center gap-2">
              <Skeleton className="h-4 w-[62px] shrink-0" />
              <div className="flex items-center gap-1">
                {[1, 2, 3, 4].map((i) => (
                  <Skeleton key={i} className="h-7 w-12 rounded-md" />
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Section Header Skeleton */}
      <div className="pt-2 pb-1">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <Skeleton className="h-6 w-20 rounded-md" />
            <Skeleton className="h-5 w-48 rounded-md" />
          </div>
          <Skeleton className="h-5 w-16 rounded-full" />
        </div>
      </div>

      {/* Question Cards Skeleton List */}
      <div className="space-y-3">
        {[1, 2, 3, 4, 5].map((idx) => (
          <div
            key={idx}
            className="rounded-xl bg-card p-3 sm:p-4 shadow-xs space-y-3"
          >
            {/* Top row: Checkbox + Badges + Right Island */}
            <div className="flex items-start justify-between gap-2">
              <div className="flex flex-wrap items-center gap-1.5 flex-1">
                {/* Checkbox */}
                <Skeleton className="h-4 w-4 rounded-sm mr-1" />
                {/* Badges */}
                <Skeleton className="h-5 w-12 rounded-full" />
                <Skeleton className="h-5 w-14 rounded-full" />
                <Skeleton className="h-5 w-16 rounded-full" />
                <Skeleton className="h-5 w-10 rounded-full" />
              </div>
              {/* Action Island */}
              <Skeleton className="h-7 w-24 rounded-lg shrink-0" />
            </div>

            {/* Question Text */}
            <div className="space-y-1.5 pt-0.5">
              <Skeleton
                className={
                  idx % 2 === 0
                    ? "h-4 w-11/12 rounded"
                    : "h-4 w-4/5 rounded"
                }
              />
              <Skeleton
                className={
                  idx % 2 === 0
                    ? "h-4 w-3/4 rounded"
                    : "h-4 w-3/5 rounded"
                }
              />
            </div>

            {/* Bottom Affordance */}
            <div className="pt-1">
              <Skeleton className="h-5 w-24 rounded-md" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
