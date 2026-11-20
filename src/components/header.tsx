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
  Computer01Icon,
  Bulb01Icon,
  MessageEdit01Icon,
  GithubIcon,
  UserIcon,
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
import { FeedbackDialog } from "@/components/common/feedback-dialog";
import { Switch } from "@/components/ui/switch";
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
  const { theme, setTheme, resolvedTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const isDark = mounted ? (theme === "dark" || resolvedTheme === "dark") : true;

  const [isVisible, setIsVisible] = useState(true);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [userMenuOpen, setUserMenuOpen] = useState(false);
  const [isFeedbackOpen, setIsFeedbackOpen] = useState(false);
  const dropdownOpenRef = useRef(false);
  const userMenuOpenRef = useRef(false);
  dropdownOpenRef.current = dropdownOpen;
  userMenuOpenRef.current = userMenuOpen;

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
          // If any dropdown menu is currently open, keep navbar visible
          if (dropdownOpenRef.current || userMenuOpenRef.current) {
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

        {/* User Avatar & Settings Dropdown (Pure Background Separation, Zero Border) */}
        <div className="flex items-center z-10 shrink-0">
          <DropdownMenu open={userMenuOpen} onOpenChange={setUserMenuOpen}>
            <DropdownMenuTrigger asChild>
              <Button
                variant="ghost"
                size="icon"
                className="group relative flex h-8 w-8 sm:h-9 sm:w-9 shrink-0 items-center justify-center rounded-full p-0 transition-all duration-200 hover:scale-105 active:scale-95 shadow-2xs outline-none focus:outline-none focus:ring-0 focus-visible:outline-none focus-visible:ring-0 border-0 bg-secondary/80 cursor-pointer select-none overflow-hidden"
                aria-label="Shrid Mishra - profile and settings"
                title="Shrid Mishra"
              >
                <Image
                  src="/shrid-avatar.jpg"
                  alt="Shrid Mishra"
                  width={36}
                  height={36}
                  className="h-8 w-8 sm:h-9 sm:w-9 object-cover rounded-full transition-transform duration-200 group-hover:scale-105"
                  priority
                />
              </Button>
            </DropdownMenuTrigger>

            <DropdownMenuContent
              align="end"
              sideOffset={8}
              className="w-[260px] p-2 rounded-2xl border-0 bg-card shadow-2xl"
            >
              {/* Shrid Mishra Profile (Clickable Link to https://shrid.site) */}
              <a
                href="https://shrid.site"
                target="_blank"
                rel="noopener noreferrer"
                className="group flex items-center gap-2.5 px-2.5 py-2 rounded-xl transition-colors hover:bg-secondary/70 border-0 outline-none"
                title="Visit shrid.site"
              >
                <div className="h-8 w-8 rounded-full overflow-hidden shrink-0">
                  <Image
                    src="/shrid-avatar.jpg"
                    alt="Shrid Mishra"
                    width={32}
                    height={32}
                    className="h-full w-full object-cover rounded-full transition-transform duration-200 group-hover:scale-105"
                  />
                </div>
                <div className="flex flex-col min-w-0">
                  <span className="font-heading text-xs font-semibold text-foreground truncate group-hover:text-primary transition-colors">
                    Shrid Mishra
                  </span>
                  <span className="text-[11px] text-muted-foreground truncate">
                    shrid.site ↗
                  </span>
                </div>
              </a>

              <DropdownMenuSeparator className="my-1.5 bg-secondary/60 h-px border-0" />

              {/* Dark Mode Toggle Switch (Icon beside text, normal switch, pure background separation) */}
              <div
                role="button"
                tabIndex={0}
                onClick={(e) => {
                  e.preventDefault();
                  setTheme(isDark ? "light" : "dark");
                }}
                onKeyDown={(e) => {
                  if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    setTheme(isDark ? "light" : "dark");
                  }
                }}
                className="flex items-center justify-between px-2.5 py-2 rounded-xl cursor-pointer hover:bg-secondary/70 transition-colors select-none outline-none border-0"
              >
                <div className="flex items-center gap-2.5">
                  {isDark ? (
                    <Moon02Icon className="h-4 w-4 text-foreground shrink-0" />
                  ) : (
                    <Sun03Icon className="h-4 w-4 text-foreground shrink-0" />
                  )}
                  <span className="font-heading text-xs font-medium text-foreground">
                    Dark mode
                  </span>
                </div>
                <Switch
                  checked={isDark}
                  onCheckedChange={(checked) => setTheme(checked ? "dark" : "light")}
                  aria-label="Toggle dark mode"
                />
              </div>

              <DropdownMenuSeparator className="my-1.5 bg-secondary/60 h-px border-0" />

              {/* Bugs & Suggestions Option */}
              <DropdownMenuItem
                onSelect={() => {
                  setUserMenuOpen(false);
                  setIsFeedbackOpen(true);
                }}
                onClick={() => {
                  setUserMenuOpen(false);
                  setIsFeedbackOpen(true);
                }}
                className="flex items-center gap-2.5 rounded-xl px-2.5 py-2 cursor-pointer transition-colors hover:bg-secondary/70 focus:bg-secondary/70 data-[highlighted]:bg-secondary/70 text-foreground border-0"
              >
                <div className="flex h-7 w-7 items-center justify-center rounded-lg bg-secondary text-foreground shrink-0">
                  <MessageEdit01Icon className="h-4 w-4" />
                </div>
                <div className="flex flex-col min-w-0 flex-1">
                  <span className="font-heading text-xs font-semibold text-foreground">
                    Bugs & Suggestions
                  </span>
                  <span className="text-[11px] text-muted-foreground">
                    Report an issue or suggest ideas
                  </span>
                </div>
              </DropdownMenuItem>

              <DropdownMenuSeparator className="my-1.5 bg-secondary/60 h-px border-0" />

              {/* GitHub Repository Link */}
              <DropdownMenuItem asChild>
                <a
                  href="https://github.com/shridmishra/exam"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2.5 rounded-xl px-2.5 py-2 cursor-pointer transition-colors hover:bg-secondary/70 focus:bg-secondary/70 data-[highlighted]:bg-secondary/70 text-foreground border-0"
                >
                  <GithubIcon className="h-4 w-4 text-muted-foreground" />
                  <span className="font-heading text-xs font-medium text-foreground">
                    GitHub Repository
                  </span>
                </a>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </header>

    {/* Bugs & Suggestions Dialog */}
    <FeedbackDialog
      open={isFeedbackOpen}
      onOpenChange={setIsFeedbackOpen}
      currentSubject={displayName}
      currentSubjectCode={currentSubject?.code}
      activeTab={activeTab}
    />
    </>
  );
});
