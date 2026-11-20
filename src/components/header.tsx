"use client";

import React, { useState, useEffect, useRef } from "react";
import Image from "next/image";
import { useTheme } from "next-themes";
import { motion } from "framer-motion";
import {
  Task01Icon,
  FunctionOfXIcon,
  Calendar03Icon,
  Sun03Icon,
  Moon02Icon,
  ChevronDownIcon,
  Tick02Icon,
} from "@/components/ui/icons";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { SubjectOption } from "@/types";
import { cn } from "@/lib/utils";
import { tabSpringTransition } from "@/lib/motion";

const NAV_ITEMS = [
  { id: "checklist" as const, label: "Checklist", icon: Task01Icon },
  { id: "formulas" as const, label: "Formulas", icon: FunctionOfXIcon },
  { id: "timetable" as const, label: "Timetable", icon: Calendar03Icon },
];

interface HeaderProps {
  activeTab: "checklist" | "formulas" | "timetable" | "notes";
  setActiveTab: (tab: "checklist" | "formulas" | "timetable" | "notes") => void;
  selectedSubjectId?: string;
  onSelectSubject?: (subjectId: string) => void;
  subjects?: SubjectOption[];
  subjectName?: string;
  notesCount?: number;
}

export const Header = React.memo(function Header({
  activeTab,
  setActiveTab,
  selectedSubjectId,
  onSelectSubject,
  subjects = [],
  subjectName = "Geotechnical Engineering - II",
  notesCount = 0,
}: HeaderProps) {
  const { theme, setTheme } = useTheme();

  const [isVisible, setIsVisible] = useState(true);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownOpenRef = useRef(false);
  dropdownOpenRef.current = dropdownOpen;

  // Keep header visible whenever switching tabs or subjects
  useEffect(() => {
    setIsVisible(true);
  }, [activeTab, selectedSubjectId]);

  // Hide navbar on scroll down, reveal immediately on scroll up
  useEffect(() => {
    let lastScrollY = typeof window !== "undefined" ? Math.max(0, window.scrollY) : 0;
    let ticking = false;
    const scrollThreshold = 8;
    const topThreshold = 64;

    const handleScroll = () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          // If dropdown menu is currently open, keep navbar visible
          if (dropdownOpenRef.current) {
            setIsVisible(true);
            ticking = false;
            return;
          }

          const currentScrollY = Math.max(0, window.scrollY);
          const maxScrollY =
            (document.documentElement.scrollHeight || document.body.scrollHeight) -
            window.innerHeight;
          const scrollDelta = currentScrollY - lastScrollY;

          if (currentScrollY <= topThreshold) {
            // At the top of the page, always show navbar
            setIsVisible(true);
          } else if (currentScrollY >= maxScrollY - 20) {
            // In rubber-band / overscroll zone at page bottom: ignore bounce
          } else if (Math.abs(scrollDelta) >= scrollThreshold) {
            if (scrollDelta > 0) {
              // Scrolling down -> hide navbar
              setIsVisible(false);
            } else {
              // Scrolling up -> reveal navbar
              setIsVisible(true);
            }
          }

          lastScrollY = currentScrollY;
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const currentSubject = subjects.find((s) => s.id === selectedSubjectId);
  const displayName = currentSubject ? currentSubject.name : subjectName;
  const availableSubjects = subjects.filter((s) => s.status !== "planned");

  return (
    <>
      {/* Dimmed backdrop when subject switcher dropdown is open to cleanly separate it from page content */}
      {dropdownOpen && (
        <div
          className="fixed inset-0 z-30 bg-background/50 backdrop-blur-[2px] transition-opacity duration-200 cursor-pointer"
          onClick={() => setDropdownOpen(false)}
          aria-hidden="true"
        />
      )}

      <header
        onFocusCapture={() => setIsVisible(true)}
        className={cn(
          "sticky top-0 z-40 w-full bg-card/90 backdrop-blur-md supports-[backdrop-filter]:bg-card/80 transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] will-change-transform",
          isVisible
            ? "translate-y-0 shadow-[0_1px_3px_rgba(0,0,0,0.04),0_1px_2px_rgba(0,0,0,0.02)] dark:shadow-[0_2px_8px_rgba(0,0,0,0.35)]"
            : "-translate-y-full pointer-events-none shadow-none"
        )}
      >
        <div className="container relative flex h-14 sm:h-16 items-center justify-between gap-2 sm:gap-4">
          {/* Subject Switcher Dropdown */}
          <div className="flex items-center min-w-0 max-w-[calc(100%-48px)] md:max-w-xs lg:max-w-sm z-10">
            {availableSubjects.length > 0 && onSelectSubject ? (
              <DropdownMenu open={dropdownOpen} onOpenChange={setDropdownOpen}>
                <DropdownMenuTrigger asChild>
                  <Button
                    variant="ghost"
                    className="group flex h-auto max-w-full items-center gap-1.5 sm:gap-2 px-2.5 sm:px-3 py-1.5 text-left font-bold tracking-tight text-foreground transition-all bg-secondary hover:bg-secondary/80 data-[state=open]:bg-secondary/80 rounded-lg outline-none focus:outline-none focus:ring-0 focus-visible:outline-none focus-visible:ring-0 border-0"
                    title="Switch subject"
                    aria-label="Switch subject"
                  >
                    <span className="font-heading text-xs sm:text-sm md:text-[15px] font-semibold tracking-tight truncate max-w-[210px] sm:max-w-xs">
                      {displayName}
                    </span>
                    <ChevronDownIcon className="h-3.5 w-3.5 sm:h-4 sm:w-4 shrink-0 text-muted-foreground transition-transform duration-200 group-data-[state=open]:rotate-180 group-hover:text-foreground" />
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent
                  align="start"
                  sideOffset={8}
                  className="w-[calc(100vw-2rem)] sm:w-[340px] max-w-[340px] p-2 rounded-2xl border border-border/40 bg-popover/95 backdrop-blur-md shadow-2xl"
                >
                  {/* Separation Header */}
                  <div className="flex items-center justify-between px-2.5 py-1.5 pb-2 text-[11px] font-semibold uppercase tracking-[0.04em] text-muted-foreground">
                    <span>Switch Subject</span>
                    <span className="text-[10px] font-normal lowercase tracking-normal text-muted-foreground/70">
                      {availableSubjects.length} available
                    </span>
                  </div>
                  <DropdownMenuSeparator className="mb-1.5" />

                  <div className="space-y-1">
                    {availableSubjects.map((sub, idx) => {
                      const isSelected = sub.id === (selectedSubjectId || currentSubject?.id);
                      return (
                        <React.Fragment key={sub.id}>
                          {idx > 0 && <DropdownMenuSeparator className="my-1 opacity-60" />}
                          <DropdownMenuItem
                            onSelect={() => {
                              onSelectSubject(sub.id);
                              setDropdownOpen(false);
                            }}
                            onClick={() => {
                              onSelectSubject(sub.id);
                              setDropdownOpen(false);
                            }}
                            className={cn(
                              "flex items-center justify-between gap-3 rounded-xl px-3 py-2.5 cursor-pointer transition-all duration-150 outline-none select-none",
                              isSelected
                                ? "bg-secondary dark:bg-filter-active font-medium text-foreground shadow-2xs"
                                : "hover:bg-secondary/70 focus:bg-secondary/70 data-[highlighted]:bg-secondary/70 dark:hover:bg-filter-active/50 dark:focus:bg-filter-active/50 dark:data-[highlighted]:bg-filter-active/50 text-foreground/90 hover:text-foreground"
                            )}
                          >
                            <div className="flex flex-col min-w-0 flex-1">
                              <span className="font-heading truncate text-sm font-medium text-foreground">
                                {sub.name}
                              </span>
                              <div className="flex items-center gap-1.5 text-xs text-muted-foreground mt-1 font-heading">
                                <span className="text-[11px] font-medium px-1.5 py-0.5 rounded bg-muted/80 dark:bg-card text-foreground/80">
                                  {sub.code}
                                </span>
                                <span className="px-1.5 py-0.5 rounded bg-muted/80 dark:bg-card text-foreground/80">
                                  {sub.short_name}
                                </span>
                                {sub.question_count ? (
                                  <span className="px-1.5 py-0.5 rounded bg-muted/80 dark:bg-card text-foreground/80">
                                    {sub.question_count} Qs
                                  </span>
                                ) : null}
                              </div>
                            </div>
                            {isSelected && (
                              <div className="flex h-5 w-5 items-center justify-center rounded-full bg-primary/10 text-primary dark:bg-foreground/15 dark:text-foreground shrink-0">
                                <Tick02Icon className="h-3.5 w-3.5 stroke-[2.5]" />
                              </div>
                            )}
                          </DropdownMenuItem>
                        </React.Fragment>
                      );
                    })}
                  </div>
                </DropdownMenuContent>
              </DropdownMenu>
          ) : (
            <div
              className="cursor-pointer font-bold tracking-tight text-foreground transition-opacity hover:opacity-80 truncate"
              onClick={() => setActiveTab("checklist")}
              title="Back to Checklist"
            >
              <span className="font-heading text-xs sm:text-sm md:text-[15px] font-semibold tracking-tight truncate">{displayName}</span>
            </div>
          )}
        </div>

        {/* Navigation Tabs (Desktop centered island, hidden on mobile in favor of bottom nav) */}
        <nav
          className="hidden md:flex absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 items-center gap-1 sm:gap-1.5 z-10"
          aria-label="Main Navigation"
        >
          {NAV_ITEMS.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <Button
                key={item.id}
                variant="ghost"
                size="sm"
                onClick={() => setActiveTab(item.id)}
                className={cn(
                  "relative flex items-center gap-1.5 font-heading text-xs sm:text-[14.5px] font-medium outline-none focus:outline-none focus:ring-0 focus-visible:outline-none focus-visible:ring-0 border-0 transition-colors px-3 py-1.5 rounded-lg select-none",
                  isActive
                    ? "text-foreground font-semibold"
                    : "text-muted-foreground hover:text-foreground"
                )}
                title={item.label}
              >
                {isActive && (
                  <motion.div
                    layoutId="header-active-nav-pill"
                    className="absolute inset-0 rounded-lg bg-secondary shadow-2xs ring-1 ring-border/20"
                    transition={tabSpringTransition}
                  />
                )}
                <span className="relative z-10 flex items-center gap-1.5">
                  <Icon className="h-4 w-4 shrink-0" />
                  <span className="font-heading hidden sm:inline">{item.label}</span>
                </span>
              </Button>
            );
          })}
        </nav>

        {/* Actions / Theme Toggle & Circular Profile Link */}
        <div className="flex items-center gap-2 sm:gap-2.5 z-10 shrink-0">
          <Button
            variant="ghost"
            size="icon"
            onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
            title="Toggle light/dark theme"
            aria-label="Toggle theme"
            className="h-9 w-9 text-muted-foreground hover:text-foreground outline-none focus:outline-none focus:ring-0 focus-visible:outline-none focus-visible:ring-0 border-0"
          >
            <Sun03Icon className="h-4 w-4 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
            <Moon02Icon className="absolute h-4 w-4 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
          </Button>

          <a
            href="https://shrid.site"
            target="_blank"
            rel="noopener noreferrer"
            title="Visit shrid.site"
            aria-label="Visit shrid.site"
            className="group relative flex h-8 w-8 sm:h-8.5 sm:w-8.5 items-center justify-center rounded-full overflow-hidden ring-1 ring-border/50 hover:ring-border transition-all duration-200 hover:scale-105 active:scale-95 shadow-2xs outline-none focus:outline-none focus-visible:ring-2 focus-visible:ring-primary shrink-0"
          >
            <Image
              src="/shrid-avatar.jpg"
              alt="Shrid Mishra"
              width={34}
              height={34}
              className="h-full w-full object-cover transition-transform duration-300 group-hover:scale-110"
              priority
            />
          </a>
        </div>
      </div>
    </header>
    </>
  );
});
