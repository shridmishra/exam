"use client";

import * as React from "react";
import { Tick02Icon } from "@/components/ui/icons";
import { cn } from "@/lib/utils";

export interface CheckboxProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  checked?: boolean;
  onCheckedChange?: (checked: boolean) => void;
  variant?: "default" | "success";
}

const Checkbox = React.forwardRef<HTMLButtonElement, CheckboxProps>(
  (
    {
      className,
      checked = false,
      onCheckedChange,
      onClick,
      onKeyDown,
      disabled,
      variant = "default",
      ...props
    },
    ref
  ) => {
    const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
      e.stopPropagation();
      if (disabled) return;
      onCheckedChange?.(!checked);
      onClick?.(e);
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLButtonElement>) => {
      if (disabled) return;
      if (e.key === " " || e.key === "Enter") {
        e.preventDefault();
        e.stopPropagation();
        onCheckedChange?.(!checked);
      }
      onKeyDown?.(e);
    };

    const variantCheckedStyles =
      variant === "success"
        ? "border-success bg-success text-success-foreground"
        : "border-primary bg-primary text-primary-foreground";

    return (
      <button
        type="button"
        role="checkbox"
        aria-checked={checked}
        disabled={disabled}
        ref={ref}
        onClick={handleClick}
        onKeyDown={handleKeyDown}
        className={cn(
          "peer relative flex h-4.5 w-4.5 shrink-0 items-center justify-center rounded-[5px] border border-solid transition-all duration-150 cursor-pointer select-none",
          "focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring",
          "disabled:cursor-not-allowed disabled:opacity-50",
          "before:absolute before:-inset-1 before:content-['']",
          checked
            ? cn(variantCheckedStyles, "shadow-2xs")
            : "bg-[var(--checkbox-bg)] border-[var(--checkbox-border)] hover:bg-[var(--checkbox-hover-bg)] hover:border-[var(--checkbox-hover-border)]",
          className
        )}
        {...props}
      >
        <span
          className={cn(
            "flex items-center justify-center text-current transition-all duration-100",
            checked ? "opacity-100 scale-100" : "opacity-0 scale-75"
          )}
        >
          <Tick02Icon className="h-3 w-3 stroke-[2.5]" />
        </span>
      </button>
    );
  }
);
Checkbox.displayName = "Checkbox";

export { Checkbox };
