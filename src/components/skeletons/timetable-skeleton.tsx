import React from "react";
import { Skeleton } from "@/components/ui/skeleton";

export function TimetableSkeleton() {
  return (
    <div className="space-y-4">
      {/* Header Row Skeleton */}
      <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between py-1">
        <Skeleton className="h-6 w-52 rounded-md" />
        <Skeleton className="h-7 w-64 rounded-full" />
      </div>

      {/* Controls Bar Minimal Skeleton */}
      <div className="flex flex-col gap-3 rounded-2xl bg-card p-3 sm:p-4 shadow-xs sm:flex-row sm:items-center sm:justify-between">
        {/* Filter Pills */}
        <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar">
          {[1, 2, 3, 4].map((i) => (
            <Skeleton key={i} className="h-8 w-20 rounded-full" />
          ))}
        </div>

        {/* Right Actions */}
        <div className="flex items-center gap-2">
          <Skeleton className="h-8 w-24 rounded-lg" />
          <Skeleton className="h-8 w-28 rounded-lg" />
        </div>
      </div>

      {/* Calendar Boxes Skeleton */}
      <div className="space-y-6">
        {[1, 2].map((monthIdx) => (
          <div
            key={monthIdx}
            className="rounded-2xl bg-card p-4 sm:p-5 shadow-xs space-y-4"
          >
            {/* Month Header */}
            <div className="flex items-center justify-between pb-2 border-b border-border/30">
              <Skeleton className="h-6 w-36 rounded-md" />
              <div className="flex items-center gap-2">
                <Skeleton className="h-5 w-24 rounded-full" />
                <Skeleton className="h-5 w-16 rounded-full" />
              </div>
            </div>

            {/* Calendar Grid Representation */}
            <div className="grid grid-cols-7 gap-2 pt-2">
              {[1, 2, 3, 4, 5, 6, 7].map((dayIdx) => (
                <div key={dayIdx} className="space-y-2">
                  <Skeleton className="h-4 w-full rounded" />
                  <Skeleton className="h-16 sm:h-20 w-full rounded-xl" />
                  <Skeleton className="h-16 sm:h-20 w-full rounded-xl" />
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
