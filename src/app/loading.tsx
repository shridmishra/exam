"use client";

import React from "react";
import { ChecklistSkeleton } from "@/components/skeletons";
import { Skeleton } from "@/components/ui/skeleton";

export default function Loading() {
  return (
    <div className="flex min-h-screen flex-col bg-background">
      {/* Header Skeleton Shell */}
      <header className="sticky top-0 z-40 w-full border-b border-border/40 bg-background/80 backdrop-blur-md">
        <div className="container flex h-14 sm:h-16 items-center justify-between gap-4">
          {/* Logo & Subject Brand */}
          <div className="flex items-center gap-3">
            <Skeleton className="h-8 w-8 rounded-lg" />
            <div className="hidden sm:flex flex-col gap-1">
              <Skeleton className="h-4 w-32 rounded" />
              <Skeleton className="h-3 w-20 rounded" />
            </div>
          </div>

          {/* Desktop Nav Pills */}
          <div className="hidden md:flex items-center gap-1.5 rounded-full bg-secondary/50 p-1">
            <Skeleton className="h-8 w-24 rounded-full" />
            <Skeleton className="h-8 w-24 rounded-full" />
            <Skeleton className="h-8 w-24 rounded-full" />
          </div>

          {/* Right Island: Subject Selector & Theme Toggle */}
          <div className="flex items-center gap-2">
            <Skeleton className="h-9 w-32 sm:w-44 rounded-xl" />
            <Skeleton className="h-9 w-9 rounded-xl" />
          </div>
        </div>
      </header>

      {/* Main Content Skeleton */}
      <main className="container flex-1 py-4 sm:py-6 md:py-8 pb-24 md:pb-8">
        <ChecklistSkeleton />
      </main>
    </div>
  );
}
