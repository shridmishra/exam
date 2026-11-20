"use client";

import React from "react";

interface ProgressRingProps {
  completed: number;
  total: number;
  onClick?: () => void;
  isActiveFilter?: boolean;
}

export const ProgressRing = React.memo(function ProgressRing({
  completed,
  total,
  onClick,
  isActiveFilter = false,
}: ProgressRingProps) {
  const safeCompleted = Math.min(total, Math.max(0, completed));
  const percentage =
    total > 0
      ? Math.min(100, Math.max(0, Math.round((safeCompleted / total) * 100)))
      : 0;
  const radius = 17.5;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (percentage / 100) * circumference;

  return (
    <div
      onClick={onClick}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          onClick?.();
        }
      }}
      title={`Overall Completion: ${safeCompleted}/${total} (${percentage}%) • Click to toggle incomplete questions`}
      className={`relative flex h-[42px] w-[42px] cursor-pointer items-center justify-center rounded-full transition-transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-ring ${
        isActiveFilter ? "ring-2 ring-primary" : ""
      }`}
    >
      <svg
        className="h-[42px] w-[42px] -rotate-90"
        viewBox="0 0 42 42"
        aria-hidden="true"
      >
        <defs>
          <linearGradient
            id="checklistRingGrad"
            x1="0%"
            y1="0%"
            x2="100%"
            y2="100%"
          >
            <stop offset="0%" stopColor="var(--ring-grad-start)" />
            <stop offset="100%" stopColor="var(--ring-grad-end)" />
          </linearGradient>
        </defs>
        {/* Background track */}
        <circle
          className="text-muted stroke-current"
          strokeWidth="3.5"
          fill="transparent"
          r={radius}
          cx="21"
          cy="21"
        />
        {/* Progress stroke */}
        <circle
          stroke="url(#checklistRingGrad)"
          strokeWidth="3.5"
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          fill="transparent"
          r={radius}
          cx="21"
          cy="21"
          style={{ transition: "stroke-dashoffset 0.4s ease" }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center font-bold tabular-nums">
        <span className="font-heading text-xs leading-none text-foreground">
          {percentage}
          <span className="text-[10px] font-normal text-muted-foreground">%</span>
        </span>
      </div>
    </div>
  );
});
