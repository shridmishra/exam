import React from "react";
import { Skeleton } from "@/components/ui/skeleton";

export function FormulasSkeleton() {
  return (
    <div className="space-y-6">
      {/* Title */}
      <div>
        <Skeleton className="h-6 w-40 rounded-md" />
      </div>

      {/* Control Bar Skeleton */}
      <div className="flex flex-col gap-3 rounded-2xl bg-card p-3 sm:p-4 shadow-xs sm:flex-row sm:items-center sm:justify-between">
        {/* Left: Unit Pills */}
        <div className="flex min-w-0 items-center gap-2">
          <Skeleton className="h-4 w-10 shrink-0" />
          <div className="flex items-center gap-1">
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <Skeleton key={i} className="h-7 w-12 rounded-md" />
            ))}
          </div>
        </div>

        {/* Right: Search & Counter */}
        <div className="flex items-center gap-2 w-full sm:w-auto">
          <Skeleton className="h-9 w-full sm:w-56 md:w-64 rounded-xl" />
          <Skeleton className="h-9 w-24 rounded-xl shrink-0" />
        </div>
      </div>

      {/* Cards Grid Skeleton */}
      <div className="grid grid-cols-1 gap-4 sm:gap-5 md:grid-cols-2">
        {[1, 2, 3, 4].map((i) => (
          <div
            key={i}
            className="rounded-xl bg-card p-4 sm:p-5 shadow-xs space-y-4"
          >
            {/* Header: Badges & Title */}
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Skeleton className="h-5 w-32 rounded-full" />
                <Skeleton className="h-5 w-14 rounded-full" />
              </div>
              <div className="flex items-start justify-between gap-2">
                <Skeleton className="h-5 w-3/4 rounded-md" />
                <Skeleton className="h-7 w-7 rounded-md shrink-0" />
              </div>
            </div>

            {/* Formula Math Box */}
            <div className="h-16 w-full rounded-lg bg-secondary/40 flex items-center justify-center p-3">
              <Skeleton className="h-6 w-2/3 rounded-md" />
            </div>

            {/* Parameter & Details rows */}
            <div className="space-y-2 pt-1">
              <Skeleton className="h-3.5 w-5/6 rounded" />
              <Skeleton className="h-3.5 w-4/6 rounded" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
