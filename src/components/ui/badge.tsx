import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "font-heading inline-flex items-center rounded-md px-2 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/80",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive:
          "bg-destructive text-destructive-foreground shadow hover:bg-destructive/80",
        outline: "bg-secondary/70 text-foreground",
        subtle: "bg-secondary text-secondary-foreground font-normal text-[11px]",
        year2025: "bg-[var(--badge-year-2025-bg)] text-[var(--badge-year-2025-fg)]",
        year2024: "bg-[var(--badge-year-2024-bg)] text-[var(--badge-year-2024-fg)]",
        year2023: "bg-[var(--badge-year-2023-bg)] text-[var(--badge-year-2023-fg)]",
        year2022: "bg-[var(--badge-year-2022-bg)] text-[var(--badge-year-2022-fg)]",
        year2019: "bg-[var(--badge-year-2019-bg)] text-[var(--badge-year-2019-fg)]",
        repeat5x: "bg-[var(--badge-repeat-5x-bg)] text-[var(--badge-repeat-5x-fg)]",
        repeat4x: "bg-[var(--badge-repeat-4x-bg)] text-[var(--badge-repeat-4x-fg)]",
        repeat3x: "bg-[var(--badge-repeat-3x-bg)] text-[var(--badge-repeat-3x-fg)]",
        repeat2x: "bg-[var(--badge-repeat-2x-bg)] text-[var(--badge-repeat-2x-fg)]",
        sky: "bg-[var(--pastel-sky-bg)] text-[var(--pastel-sky-foreground)]",
        sage: "bg-[var(--pastel-sage-bg)] text-[var(--pastel-sage-foreground)]",
        peach: "bg-[var(--pastel-peach-bg)] text-[var(--pastel-peach-foreground)]",
        done: "bg-[var(--pastel-done-bg)] text-[var(--pastel-done-foreground)]",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
);

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  );
}

export { Badge, badgeVariants };
