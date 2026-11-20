import React from "react";
import { Skeleton } from "@/components/ui/skeleton";

export function NotesSkeleton() {
  return (
    <div className="space-y-6">
      {/* Title & Actions Skeleton */}
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <Skeleton className="h-6 w-52 rounded-md" />
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <Skeleton className="h-8 w-28 rounded-lg" />
          <Skeleton className="h-8 w-20 rounded-lg" />
          <Skeleton className="h-8 w-24 rounded-lg" />
        </div>
      </div>

      {/* General Scratchpad Card Skeleton */}
      <div className="rounded-2xl bg-card p-4 sm:p-5 shadow-xs space-y-3">
        <div className="flex items-center justify-between pb-1">
          <Skeleton className="h-5 w-48 rounded-md" />
          <Skeleton className="h-7 w-28 rounded-lg" />
        </div>
        <Skeleton className="h-28 w-full rounded-xl" />
      </div>

      {/* Search Input Skeleton */}
      <div className="flex items-center justify-between gap-3">
        <Skeleton className="h-9 flex-1 sm:max-w-xs rounded-xl" />
        <Skeleton className="h-6 w-24 rounded-full" />
      </div>

      {/* Notes List Cards Skeleton */}
      <div className="space-y-3">
        {[1, 2, 3].map((i) => (
          <div
            key={i}
            className="rounded-xl bg-card p-4 shadow-xs space-y-3"
          >
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Skeleton className="h-5 w-20 rounded-md" />
                <Skeleton className="h-5 w-32 rounded-full" />
              </div>
              <Skeleton className="h-7 w-16 rounded-md" />
            </div>
            <div className="space-y-1.5">
              <Skeleton className="h-4 w-4/5 rounded" />
              <Skeleton className="h-4 w-2/3 rounded" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
