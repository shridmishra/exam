"use client";

import React from "react";
import {
  Task01Icon,
  FunctionOfXIcon,
  Calendar03Icon,
} from "@/components/ui/icons";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface MobileNavProps {
  activeTab: "checklist" | "formulas" | "timetable" | "notes";
  setActiveTab: (tab: "checklist" | "formulas" | "timetable" | "notes") => void;
}

export function MobileNav({ activeTab, setActiveTab }: MobileNavProps) {
  const tabs = [
    {
      id: "checklist" as const,
      label: "Checklist",
      icon: Task01Icon,
    },
    {
      id: "formulas" as const,
      label: "Formulas",
      icon: FunctionOfXIcon,
    },
    {
      id: "timetable" as const,
      label: "Timetable",
      icon: Calendar03Icon,
    },
  ];

  return (
    <nav
      className="fixed bottom-0 left-0 right-0 z-40 md:hidden bg-card/95 backdrop-blur-md border-0 pb-[env(safe-area-inset-bottom,0px)] shadow-[0_-2px_10px_rgba(0,0,0,0.06)] dark:shadow-[0_-2px_12px_rgba(0,0,0,0.4)]"
      aria-label="Mobile Navigation"
    >
      <div className="flex h-14 items-center justify-around px-2">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;

          return (
            <Button
              key={tab.id}
              variant="ghost"
              size="sm"
              onClick={() => setActiveTab(tab.id)}
              className={cn(
                "flex flex-1 flex-col items-center justify-center gap-1 h-11 py-1 rounded-xl transition-all duration-200 select-none active:scale-95 outline-none focus:outline-none focus:ring-0 focus-visible:outline-none focus-visible:ring-0 border-0 font-heading",
                isActive
                  ? "bg-secondary text-foreground font-semibold shadow-2xs"
                  : "text-muted-foreground hover:text-foreground hover:bg-secondary/40"
              )}
              aria-label={tab.label}
              title={tab.label}
            >
              <Icon
                className={cn(
                  "h-5 w-5 transition-transform duration-200",
                  isActive && "scale-105 stroke-[2.2]"
                )}
              />
              <span className="font-heading text-[11px] leading-none tracking-tight">
                {tab.label}
              </span>
            </Button>
          );
        })}
      </div>
    </nav>
  );
}
