"use client";

import React, { useState, useEffect, useMemo } from "react";
import {
  Clock01Icon,
  PencilEdit02Icon,
  Delete02Icon,
  Tick02Icon,
  InformationCircleIcon,
} from "@/components/ui/icons";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { ExamItem } from "@/types";
import { STORAGE_KEYS } from "@/lib/constants";
import { cn } from "@/lib/utils";
import { toast } from "@/components/ui/sonner";

interface TimetablePresets {
  default: ExamItem[];
  backlog: ExamItem[];
}

interface TimetableProps {
  presets: TimetablePresets;
}

const STORAGE_KEY_TIMETABLE = STORAGE_KEYS.TIMETABLE;

export function isExamCompleted(item: ExamItem): boolean {
  if (!item || !item.isoDate) return Boolean(item && item.completed);
  const now = new Date();
  const examEndTime = new Date(`${item.isoDate}T17:00:00`);
  if (!isNaN(examEndTime.getTime())) {
    return now.getTime() >= examEndTime.getTime();
  }
  const todayIso = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`;
  return item.isoDate < todayIso;
}

function recalculateGaps(items: ExamItem[]): ExamItem[] {
  const sorted = [...items].sort((a, b) =>
    (a.isoDate || "").localeCompare(b.isoDate || "")
  );
  const dayNames = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const baseDate = new Date("2026-11-01T00:00:00");

  return sorted.map((item, idx) => {
    const completed = isExamCompleted(item);
    let day = item.day;
    let dateStr = item.date;
    let order = item.order;

    if (item.isoDate) {
      const d = new Date(item.isoDate + "T00:00:00");
      if (!isNaN(d.getTime())) {
        day = dayNames[d.getDay()];
        dateStr = `${String(d.getDate()).padStart(2, "0")} ${months[d.getMonth()]} ${d.getFullYear()}`;
        order =
          Math.round(
            (d.getTime() - baseDate.getTime()) / (1000 * 60 * 60 * 24)
          ) + 1;
      }
    }

    let gap = "First Exam";
    if (idx > 0) {
      const prevD = new Date(sorted[idx - 1].isoDate + "T00:00:00");
      const currD = new Date(item.isoDate + "T00:00:00");
      const diffDays = Math.round(
        (currD.getTime() - prevD.getTime()) / (1000 * 60 * 60 * 24)
      );
      if (diffDays === 0) gap = "Same Day";
      else if (diffDays === 1) gap = "1 Day Gap";
      else gap = `${diffDays} Days Gap`;
    }

    return {
      ...item,
      day,
      date: dateStr,
      order,
      gap,
      completed,
    };
  });
}

export function TimetableView({ presets }: TimetableProps) {
  const hasHydratedRef = React.useRef(false);

  // Initialize schedule strictly with presets.default (3 regular papers, green)
  const [schedule, setSchedule] = useState<ExamItem[]>(() =>
    recalculateGaps(presets.default)
  );

  // Hydrate custom timetable from user's local storage if present
  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY_TIMETABLE);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed) && parsed.length > 0) {
          setSchedule(recalculateGaps(parsed));
        }
      }
    } catch (e) {
      console.warn("Error reading timetable from localStorage:", e);
    } finally {
      hasHydratedRef.current = true;
    }
  }, []);

  // Save changes directly to user's local storage after hydration
  useEffect(() => {
    if (!hasHydratedRef.current) return;
    try {
      localStorage.setItem(STORAGE_KEY_TIMETABLE, JSON.stringify(schedule));
    } catch (e) {
      console.warn("Error saving timetable:", e);
    }
  }, [schedule]);

  // Active filter tab: all, regular, old, done
  const [activeFilter, setActiveFilter] = useState<
    "all" | "regular" | "old" | "done"
  >("all");

  // Active view: calendar, table, timeline
  const [activeView, setActiveView] = useState<
    "calendar" | "table" | "timeline"
  >("calendar");

  // Sort direction for table
  const [sortAscending, setSortAscending] = useState(true);

  // Modal state
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingItem, setEditingItem] = useState<ExamItem | null>(null);

  // Form state
  const [formData, setFormData] = useState({
    subject: "",
    code: "",
    shortTag: "",
    isoDate: "",
    category: "Regular" as "Regular" | "Old Syllabus" | "Custom",
    customTag: "",
  });

  // Live status pill calculation
  const liveStatus = useMemo(() => {
    const now = new Date();
    const todayMid = new Date(now.getFullYear(), now.getMonth(), now.getDate());

    let nextExam: ExamItem | null = null;
    let daysDiff = 9999;

    for (const item of schedule) {
      if (!item.isoDate || item.completed) continue;
      const examDate = new Date(item.isoDate + "T00:00:00");
      const diffTime = examDate.getTime() - todayMid.getTime();
      const diff = Math.round(diffTime / (1000 * 60 * 60 * 24));
      if (diff >= 0 && diff < daysDiff) {
        daysDiff = diff;
        nextExam = item;
      }
    }

    if (nextExam) {
      let diffText = "";
      if (daysDiff === 0) {
        diffText = "Today!";
      } else if (daysDiff === 1) {
        diffText = "Tomorrow!";
      } else {
        diffText = `in ${daysDiff} days`;
      }
      const codeDisplay =
        nextExam.shortTag || nextExam.code.replace("CE ", "");
      const datePart = (nextExam.date || "").split(" ").slice(0, 2).join(" ");
      return {
        isAllDone: false,
        text: `Next: ${datePart} (${codeDisplay}) • ${diffText}`,
        highlight: daysDiff <= 1,
      };
    }

    const totalPapers = schedule.length;
    const allDone = totalPapers > 0 && schedule.every((s) => s.completed);
    if (allDone) {
      return {
        isAllDone: true,
        text: "✓ All examinations concluded",
        highlight: false,
      };
    }

    return {
      isAllDone: false,
      text: "All scheduled papers concluded",
      highlight: false,
    };
  }, [schedule]);

  // Filter counts
  const totalCount = schedule.length;
  const regCount = schedule.filter((s) => !s.isOld).length;
  const oldCount = schedule.filter((s) => s.isOld).length;
  const doneCount = schedule.filter((s) => s.completed).length;

  // Filtered and sorted schedule
  const filteredSchedule = useMemo(() => {
    const list = schedule.filter((item) => {
      if (activeFilter === "regular") return !item.isOld;
      if (activeFilter === "old") return item.isOld;
      if (activeFilter === "done") return item.completed;
      return true;
    });

    return [...list].sort((a, b) => {
      const comp = (a.isoDate || "").localeCompare(b.isoDate || "");
      return sortAscending ? comp : -comp;
    });
  }, [schedule, activeFilter, sortAscending]);

  // Unique sorted months (YYYY-MM)
  const monthList = useMemo(() => {
    const set = new Set<string>(["2026-11", "2026-12"]);
    schedule.forEach((item) => {
      if (item.isoDate && item.isoDate.length >= 7) {
        set.add(item.isoDate.substring(0, 7));
      }
    });
    return Array.from(set).sort();
  }, [schedule]);

  // Handlers
  const handleLoadPreset = (type: "default" | "backlog" | "clear") => {
    if (type === "default") {
      if (window.confirm("Reset timetable to the 3 standard regular papers?")) {
        setSchedule(recalculateGaps(presets.default));
        toast.success("Loaded 3 regular exam papers", {
          description: "Timetable reset to standard syllabus",
        });
      }
    } else if (type === "backlog") {
      if (
        window.confirm(
          "Load the full 7-paper SGSITS timetable (including 4 old syllabus backlog subjects)?"
        )
      ) {
        setSchedule(recalculateGaps(presets.backlog));
        toast.success("Loaded full 7-paper timetable", {
          description: "Includes regular and backlog subjects",
        });
      }
    } else if (type === "clear") {
      if (window.confirm("Clear all subjects from your timetable?")) {
        setSchedule([]);
        toast.info("Cleared all exam papers from timetable");
      }
    }
  };

  const handleDeleteItem = (id: number) => {
    const item = schedule.find((s) => s.id === id);
    const name = item ? item.shortTag || item.subject : "this paper";
    if (window.confirm(`Remove "${name}" from your examination timetable?`)) {
      setSchedule((prev) => recalculateGaps(prev.filter((s) => s.id !== id)));
      if (item) {
        toast.success(`Removed "${name}" from timetable`, {
          action: {
            label: "Undo",
            onClick: () => {
              setSchedule((prev) => recalculateGaps([...prev, item]));
              toast.success(`Restored "${name}" to timetable`);
            },
          },
        });
      }
    }
  };

  const openAddModal = (initialDate?: string) => {
    setEditingItem(null);
    setFormData({
      subject: "",
      code: "",
      shortTag: "",
      isoDate: initialDate || "",
      category: "Regular",
      customTag: "",
    });
    setIsModalOpen(true);
  };

  const openEditModal = (item: ExamItem) => {
    setEditingItem(item);
    const isRegular = item.tag === "Regular" && !item.isOld;
    const isBacklog = item.isOld || item.tag === "Old Syllabus" || item.tag === "Backlog";
    const isCustom = !isRegular && !isBacklog;
    setFormData({
      subject: item.subject,
      code: item.code,
      shortTag: item.shortTag || "",
      isoDate: item.isoDate,
      category: isRegular ? "Regular" : isBacklog ? "Old Syllabus" : "Custom",
      customTag: isCustom ? item.tag : "",
    });
    setIsModalOpen(true);
  };

  const handleSaveModal = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.subject.trim() || !formData.isoDate) return;

    let tag = "Regular";
    let isOld = false;

    if (formData.category === "Old Syllabus") {
      tag = "Backlog";
      isOld = true;
    } else if (formData.category === "Custom") {
      tag = formData.customTag.trim() || "Custom";
      isOld = false;
    }

    const code = formData.code.trim() || "EXAM";
    const shortTag = formData.shortTag.trim() || code;

    if (editingItem) {
      setSchedule((prev) =>
        recalculateGaps(
          prev.map((item) =>
            item.id === editingItem.id
              ? {
                  ...item,
                  subject: formData.subject.trim(),
                  code,
                  shortTag,
                  isoDate: formData.isoDate,
                  tag,
                  isOld,
                }
              : item
          )
        )
      );
      toast.success(`Updated "${formData.subject.trim()}"`, {
        description: `${formData.isoDate} • ${shortTag}`,
      });
    } else {
      const newItem: ExamItem = {
        id: Date.now(),
        order: schedule.length + 1,
        subject: formData.subject.trim(),
        code,
        shortTag,
        date: "",
        isoDate: formData.isoDate,
        day: "",
        tag,
        isOld,
        gap: "",
        completed: false,
      };
      setSchedule((prev) => recalculateGaps([...prev, newItem]));
      toast.success(`Added "${formData.subject.trim()}"`, {
        description: `${formData.isoDate} • ${shortTag}`,
      });
    }

    setIsModalOpen(false);
    setEditingItem(null);
  };

  const now = new Date();
  const currentTodayIso = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`;
  const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  const monthShorts = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const dayLabels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

  return (
    <div className="space-y-4">
      {/* Super Minimal Header Row (Zero Borders) */}
      <div className="timetable-header-row">
        <div className="timetable-header-left">
          <h1 className="timetable-title">Examination Timetable</h1>
        </div>

        <div className="timetable-header-right">
          <div className="live-status-pill">
            <span
              className={cn(
                "status-dot",
                liveStatus.isAllDone && "all-done"
              )}
            />
            <span>{liveStatus.text}</span>
          </div>
        </div>
      </div>

      {/* Super Minimal Controls & Directly Colored Filter Badges */}
      <div className="controls-bar-minimal">
        <div className="filter-tabs-minimal">
          <Button
            type="button"
            variant="ghost"
            onClick={() => setActiveFilter("all")}
            className={cn("tab-pill tab-pill-all", activeFilter === "all" && "active")}
          >
            All <span className="pill-count">{totalCount}</span>
          </Button>

          <Button
            type="button"
            variant="ghost"
            onClick={() => setActiveFilter("regular")}
            className={cn(
              "tab-pill tab-pill-regular",
              activeFilter === "regular" && "active"
            )}
          >
            Regular <span className="pill-count">{regCount}</span>
          </Button>

          <Button
            type="button"
            variant="ghost"
            onClick={() => setActiveFilter("old")}
            className={cn(
              "tab-pill tab-pill-old",
              activeFilter === "old" && "active"
            )}
          >
            Backlog <span className="pill-count">{oldCount}</span>
          </Button>

          <Button
            type="button"
            variant="ghost"
            onClick={() => setActiveFilter("done")}
            className={cn(
              "tab-pill tab-pill-done",
              activeFilter === "done" && "active"
            )}
          >
            Done <span className="pill-count">{doneCount}</span>
          </Button>
        </div>

        <div className="controls-right-minimal">
          <Button
            type="button"
            variant="ghost"
            onClick={() => openAddModal()}
            className="btn-subtle-action"
            title="Customize timetable"
          >
            <PencilEdit02Icon className="h-3.5 w-3.5" />
            <span>Edit</span>
          </Button>

          <div className="view-switchers-minimal">
            <Button
              type="button"
              variant="ghost"
              onClick={() => setActiveView("calendar")}
              className={cn("view-pill", activeView === "calendar" && "active")}
              title="Monthly calendars"
            >
              Calendar
            </Button>
            <Button
              type="button"
              variant="ghost"
              onClick={() => setActiveView("table")}
              className={cn("view-pill", activeView === "table" && "active")}
              title="Table view"
            >
              Table
            </Button>
            <Button
              type="button"
              variant="ghost"
              onClick={() => setActiveView("timeline")}
              className={cn("view-pill", activeView === "timeline" && "active")}
              title="Timeline view"
            >
              Timeline
            </Button>
          </div>
        </div>
      </div>

      {/* VIEW 1: SEPARATED CALENDARS */}
      {activeView === "calendar" && (
        <section id="calendar-view">
          <div className="cal-separated-container">
            {monthList.map((ym) => {
              const [yearStr, monthStr] = ym.split("-");
              const year = parseInt(yearStr, 10);
              const month = parseInt(monthStr, 10) - 1;

              const daysInMonth = new Date(year, month + 1, 0).getDate();
              const firstDayOfWeek = new Date(year, month, 1).getDay();

              const monthExams = schedule.filter(
                (item) => item.isoDate && item.isoDate.startsWith(ym)
              );
              const examCount = monthExams.length;

              let maxWeeks = 5;
              for (let d = 1; d <= daysInMonth; d++) {
                const w = Math.floor((d + firstDayOfWeek - 1) / 7);
                if (w >= maxWeeks) maxWeeks = w + 1;
              }

              const isCurrentMonth =
                now.getFullYear() === year && now.getMonth() === month;

              // Build gridMap 7 x maxWeeks
              const gridMap: (number | null)[][] = Array.from(
                { length: 7 },
                () => Array(maxWeeks).fill(null)
              );
              for (let d = 1; d <= daysInMonth; d++) {
                const dayOfWeek = (firstDayOfWeek + d - 1) % 7;
                const weekIndex = Math.floor((d + firstDayOfWeek - 1) / 7);
                if (weekIndex < maxWeeks) {
                  gridMap[dayOfWeek][weekIndex] = d;
                }
              }

              const weekHeaders = Array.from({ length: maxWeeks }, (_, i) => i + 1);

              return (
                <div key={ym} className="cal-box" data-month={ym}>
                  <div className="cal-box-header">
                    <span>
                      {monthNames[month]} {year}
                    </span>
                    <div className="flex items-center gap-1.5">
                      {isCurrentMonth && (
                        <Badge
                          variant="sky"
                          className="rounded-full px-2.5 py-0.5 text-[11px] font-semibold"
                        >
                          Today: {now.getDate()} {monthShorts[month]}
                        </Badge>
                      )}
                      <Badge
                        variant="subtle"
                        className="rounded-full px-2.5 py-0.5 text-[11px] font-medium text-muted-foreground"
                      >
                        {examCount} {examCount === 1 ? "Paper" : "Papers"}
                      </Badge>
                    </div>
                  </div>

                  <div
                    className="cal-grid-vertical"
                    style={{
                      gridTemplateColumns: `46px repeat(${maxWeeks}, 1fr)`,
                    }}
                  >
                    <div className="cal-col-label">Day</div>
                    {weekHeaders.map((w) => (
                      <div key={w} className="cal-col-label">
                        W{w}
                      </div>
                    ))}

                    {dayLabels.map((label, dow) => (
                      <React.Fragment key={label}>
                        <div className="cal-row-label">{label}</div>
                        {Array.from({ length: maxWeeks }, (_, w) => {
                          const dayNum = gridMap[dow][w];
                          if (dayNum === null) {
                            return (
                              <div
                                key={`${dow}-${w}`}
                                className="cal-cell empty"
                              >
                                —
                              </div>
                            );
                          }

                          const dIso = `${year}-${String(month + 1).padStart(2, "0")}-${String(dayNum).padStart(2, "0")}`;
                          const isToday = dIso === currentTodayIso;
                          const exam = schedule.find(
                            (item) => item.isoDate === dIso
                          );

                          let cellClasses = "cal-cell";
                          if (isToday) cellClasses += " today current-date";

                          if (exam) {
                            if (exam.completed) cellClasses += " exam-done";
                            else if (exam.isOld || exam.tag === "Backlog" || exam.tag === "Old Syllabus") cellClasses += " exam-old";
                            else cellClasses += " exam-reg";
                          }

                          const tagText = exam
                            ? exam.shortTag || exam.code.replace("CE ", "")
                            : null;

                          return (
                            <div
                              key={`${dow}-${w}`}
                              className={cellClasses}
                              onClick={() => {
                                if (exam) openEditModal(exam);
                                else openAddModal(dIso);
                              }}
                              title={
                                exam
                                  ? `${exam.subject} (${exam.tag})${exam.completed ? " - Concluded" : ""}`
                                  : `${dayNum} ${monthShorts[month]} ${year}`
                              }
                            >
                              <span>{dayNum}</span>
                              {exam ? (
                                exam.completed ? (
                                  <span
                                    className="cal-cell-tag cal-cell-tag-done"
                                    title="Concluded Paper"
                                  >
                                    ✓ {tagText}
                                  </span>
                                ) : (
                                  <span className="cal-cell-tag">{tagText}</span>
                                )
                              ) : isToday ? (
                                <span className="cal-cell-tag">Today</span>
                              ) : null}
                            </div>
                          );
                        })}
                      </React.Fragment>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      )}

      {/* VIEW 2: TABLE (Sortable by Date) */}
      {activeView === "table" && (
        <section id="table-view" className="table-wrap">
          <table>
            <thead>
              <tr>
                <th
                  onClick={() => setSortAscending((prev) => !prev)}
                  title="Click to sort by date"
                >
                  Exam Date <span>{sortAscending ? "▲" : "▼"}</span>
                </th>
                <th>Day</th>
                <th>Code</th>
                <th>Subject Name</th>
                <th>Category</th>
                <th>Status</th>
                <th>Prep Gap</th>
                <th style={{ textAlign: "right" }}>Action</th>
              </tr>
            </thead>
            <tbody>
              {filteredSchedule.length === 0 ? (
                <tr>
                  <td
                    colSpan={8}
                    style={{
                      textAlign: "center",
                      padding: "24px",
                      color: "hsl(var(--muted-foreground))",
                    }}
                  >
                    No examination papers match the selected filter.
                  </td>
                </tr>
              ) : (
                filteredSchedule.map((item) => (
                  <tr
                    key={item.id}
                    className={cn(item.completed && "row-done")}
                  >
                    <td>
                      <strong>{item.date}</strong>
                      {item.completed && (
                        <span
                          style={{
                            color: "var(--pastel-done-foreground)",
                            marginLeft: "4px",
                            fontWeight: 700,
                          }}
                        >
                          ✓
                        </span>
                      )}
                    </td>
                    <td style={{ fontSize: "13px", color: "hsl(var(--muted-foreground))" }}>
                      {item.day}
                    </td>
                    <td>
                      <span className="code-tag">{item.code}</span>
                    </td>
                    <td>
                      <strong
                        style={{
                          color: item.completed
                            ? "hsl(var(--muted-foreground))"
                            : "inherit",
                          fontWeight: item.completed ? 500 : 600,
                        }}
                      >
                        {item.subject}
                      </strong>
                    </td>
                    <td>
                      <Badge
                        variant={
                          item.isOld || item.tag === "Backlog" || item.tag === "Old Syllabus"
                            ? "peach"
                            : item.tag === "Regular"
                            ? "sage"
                            : "subtle"
                        }
                        className="rounded-full px-2 py-0.5 text-[11px] font-semibold"
                      >
                        {item.tag}
                      </Badge>
                    </td>
                    <td>
                      <span
                        className={cn(
                          "status-badge",
                          item.completed
                            ? "status-badge-concluded"
                            : "status-badge-upcoming"
                        )}
                      >
                        {item.completed ? (
                          <>
                            <Tick02Icon className="h-3 w-3" />
                            <span>Concluded</span>
                          </>
                        ) : (
                          <>
                            <Clock01Icon className="h-3 w-3" />
                            <span>Upcoming</span>
                          </>
                        )}
                      </span>
                    </td>
                    <td style={{ fontSize: "13px", fontWeight: 500 }}>
                      {item.gap}
                    </td>
                    <td style={{ textAlign: "right", whiteSpace: "nowrap" }}>
                      <div
                        style={{
                          display: "inline-flex",
                          alignItems: "center",
                          gap: "6px",
                        }}
                      >
                        <Button
                          type="button"
                          variant="ghost"
                          size="icon"
                          onClick={() => openEditModal(item)}
                          className="h-7 w-7 text-muted-foreground hover:text-foreground"
                          title="Edit paper details"
                        >
                          <PencilEdit02Icon className="h-3.5 w-3.5" />
                        </Button>
                        <Button
                          type="button"
                          variant="ghost"
                          size="icon"
                          onClick={() => handleDeleteItem(item.id)}
                          className="h-7 w-7 text-muted-foreground hover:text-destructive"
                          title="Remove paper"
                        >
                          <Delete02Icon className="h-3.5 w-3.5" />
                        </Button>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </section>
      )}

      {/* VIEW 3: TIMELINE */}
      {activeView === "timeline" && (
        <section id="timeline-view" className="timeline-list">
          {filteredSchedule.length === 0 ? (
            <div
              style={{
                textAlign: "center",
                padding: "24px",
                color: "hsl(var(--muted-foreground))",
              }}
            >
              No examination papers match the selected filter.
            </div>
          ) : (
            filteredSchedule.map((item) => (
              <div
                key={item.id}
                className={cn(
                  "timeline-card",
                  item.completed
                    ? "done"
                    : item.isOld
                    ? "old"
                    : "regular"
                )}
              >
                <div style={{ minWidth: "110px" }}>
                  <div
                    style={{
                      fontSize: "16px",
                      fontWeight: 700,
                      display: "flex",
                      alignItems: "center",
                      gap: "6px",
                    }}
                  >
                    {item.date}
                    {item.completed && (
                      <span style={{ color: "var(--pastel-done-foreground)" }}>
                        ✓
                      </span>
                    )}
                  </div>
                  <div
                    style={{
                      fontSize: "11px",
                      color: "hsl(var(--muted-foreground))",
                    }}
                  >
                    {item.day}
                  </div>
                </div>

                <div style={{ flex: 1 }}>
                  <div
                    style={{
                      display: "flex",
                      gap: "8px",
                      alignItems: "center",
                      marginBottom: "2px",
                    }}
                  >
                    <span className="code-tag">{item.code}</span>
                    <Badge
                      variant={
                        item.isOld || item.tag === "Backlog" || item.tag === "Old Syllabus"
                          ? "peach"
                          : item.tag === "Regular"
                          ? "sage"
                          : "subtle"
                      }
                      className="rounded-full px-2 py-0.5 text-[11px] font-semibold"
                    >
                      {item.tag}
                    </Badge>
                    {item.completed && (
                      <Badge
                        variant="done"
                        className="rounded-full px-2 py-0.5 text-[11px] font-semibold"
                      >
                        ✓ Concluded
                      </Badge>
                    )}
                  </div>
                  <div
                    style={{
                      fontSize: "14px",
                      fontWeight: 600,
                      color: item.completed
                        ? "hsl(var(--muted-foreground))"
                        : "inherit",
                    }}
                  >
                    {item.subject}
                  </div>
                </div>

                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "10px",
                  }}
                >
                  <span
                    style={{
                      fontSize: "12px",
                      fontWeight: 600,
                      background: "hsl(var(--secondary))",
                      padding: "4px 10px",
                      borderRadius: "9999px",
                    }}
                  >
                    {item.gap}
                  </span>
                  <span
                    className={cn(
                      "status-badge",
                      item.completed
                        ? "status-badge-concluded"
                        : "status-badge-upcoming"
                    )}
                  >
                    {item.completed ? (
                      <>
                        <Tick02Icon className="h-3 w-3" />
                        <span>Concluded</span>
                      </>
                    ) : (
                      <>
                        <Clock01Icon className="h-3 w-3" />
                        <span>Upcoming</span>
                      </>
                    )}
                  </span>
                </div>
              </div>
            ))
          )}
        </section>
      )}

      {/* CUSTOMIZE TIMETABLE MODAL */}
      <Dialog open={isModalOpen} onOpenChange={setIsModalOpen}>
        <DialogContent className="max-w-xl max-h-[90vh] overflow-y-auto p-5">
          <DialogHeader>
            <DialogTitle className="text-lg font-bold">
              {editingItem ? "Edit Examination Paper" : "Customize Exam Timetable"}
            </DialogTitle>
            <p className="text-xs text-muted-foreground mt-0.5">
              Saved privately in your browser. Add custom papers, modify dates, or switch schedules.
            </p>
          </DialogHeader>

          {/* Add / Edit Form */}
          <form onSubmit={handleSaveModal} className="space-y-3 mt-3">
            <div className="rounded-lg bg-secondary/50 p-3.5 space-y-3">
              <div>
                <label className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block mb-1">
                  Subject Name *
                </label>
                <Input
                  required
                  placeholder="e.g. Geotechnical Engineering - II"
                  value={formData.subject}
                  onChange={(e) =>
                    setFormData((prev) => ({ ...prev, subject: e.target.value }))
                  }
                  className="h-9 text-sm bg-card border-none"
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block mb-1">
                    Subject Code
                  </label>
                  <Input
                    placeholder="e.g. CE 41007"
                    value={formData.code}
                    onChange={(e) =>
                      setFormData((prev) => ({ ...prev, code: e.target.value }))
                    }
                    className="h-9 text-sm bg-card border-none"
                  />
                </div>

                <div>
                  <label className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block mb-1">
                    Subject Tag / Subtag *
                  </label>
                  <Input
                    required
                    placeholder="e.g. Geo-2, RCC, DHS, SA-2, Elective..."
                    value={formData.shortTag}
                    onChange={(e) =>
                      setFormData((prev) => ({
                        ...prev,
                        shortTag: e.target.value,
                      }))
                    }
                    className="h-9 text-sm bg-card border-none"
                  />
                </div>

                <div>
                  <label className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block mb-1">
                    Exam Date *
                  </label>
                  <Input
                    type="date"
                    required
                    value={formData.isoDate}
                    onChange={(e) =>
                      setFormData((prev) => ({
                        ...prev,
                        isoDate: e.target.value,
                      }))
                    }
                    className="h-9 text-sm bg-card border-none"
                  />
                </div>

                <div>
                  <label className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block mb-1">
                    Category / Tag
                  </label>
                  <div className="flex items-center gap-1.5 h-9">
                    <Button
                      type="button"
                      variant={formData.category === "Regular" ? "default" : "secondary"}
                      size="sm"
                      onClick={() =>
                        setFormData((prev) => ({ ...prev, category: "Regular" }))
                      }
                      className="flex-1 text-xs h-full"
                    >
                      Regular (Green)
                    </Button>
                    <Button
                      type="button"
                      variant={
                        formData.category === "Old Syllabus"
                          ? "default"
                          : "secondary"
                      }
                      size="sm"
                      onClick={() =>
                        setFormData((prev) => ({
                          ...prev,
                          category: "Old Syllabus",
                        }))
                      }
                      className="flex-1 text-xs h-full"
                    >
                      Backlog (Peach)
                    </Button>
                    <Button
                      type="button"
                      variant={
                        formData.category === "Custom"
                          ? "default"
                          : "secondary"
                      }
                      size="sm"
                      onClick={() =>
                        setFormData((prev) => ({
                          ...prev,
                          category: "Custom",
                        }))
                      }
                      className="flex-1 text-xs h-full"
                    >
                      Custom Tag
                    </Button>
                  </div>
                </div>

                {formData.category === "Custom" && (
                  <div className="sm:col-span-2">
                    <label className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block mb-1">
                      Custom Tag Name
                    </label>
                    <Input
                      placeholder="e.g. Elective, Viva, Minor, Lab..."
                      value={formData.customTag}
                      onChange={(e) =>
                        setFormData((prev) => ({
                          ...prev,
                          customTag: e.target.value,
                        }))
                      }
                      className="h-9 text-sm bg-card border-none"
                    />
                  </div>
                )}
              </div>

              <div className="flex items-center justify-between pt-1">
                <div className="flex items-center gap-2 text-xs text-muted-foreground">
                  <InformationCircleIcon className="h-4 w-4 shrink-0 text-muted-foreground/80" />
                  <span>Completion is automatically determined once the exam date has passed.</span>
                </div>

                <div className="flex items-center gap-2">
                  {editingItem && (
                    <Button
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={() => {
                        setEditingItem(null);
                        setFormData({
                          subject: "",
                          code: "",
                          shortTag: "",
                          isoDate: "",
                          category: "Regular",
                          customTag: "",
                        });
                      }}
                      className="text-xs"
                    >
                      Cancel Edit
                    </Button>
                  )}
                  <Button type="submit" size="sm" className="text-xs font-semibold">
                    {editingItem ? "Save Changes" : "Add Subject"}
                  </Button>
                </div>
              </div>
            </div>
          </form>

          {/* Presets Row */}
          <div className="rounded-lg bg-secondary/50 p-3 mt-4 flex items-center justify-between flex-wrap gap-2">
            <span className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground">
              Schedule Presets
            </span>
            <div className="flex items-center gap-1.5 flex-wrap">
              <Button
                type="button"
                variant="outline"
                size="sm"
                onClick={() => handleLoadPreset("default")}
                className="h-7 text-xs bg-card"
              >
                3 Regular Papers
              </Button>
              <Button
                type="button"
                variant="outline"
                size="sm"
                onClick={() => handleLoadPreset("backlog")}
                className="h-7 text-xs bg-card"
              >
                7 Papers Schedule
              </Button>
              <Button
                type="button"
                variant="ghost"
                size="sm"
                onClick={() => handleLoadPreset("clear")}
                className="h-7 text-xs text-destructive hover:bg-destructive/10"
              >
                Clear All
              </Button>
            </div>
          </div>

          {/* Configured Subjects List */}
          <div className="mt-4 space-y-2">
            <span className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground block">
              Configured Papers ({schedule.length})
            </span>
            <div className="space-y-1.5 max-h-48 overflow-y-auto pr-1">
              {schedule.map((item) => (
                <div
                  key={item.id}
                  className={cn(
                    "flex items-center justify-between gap-2 p-2 rounded-md bg-secondary/40 text-xs",
                    item.completed && "opacity-75"
                  )}
                >
                  <div className="flex items-center gap-2 min-w-0">
                    <span className="font-semibold">{item.code}</span>
                    <span className="truncate">{item.subject}</span>
                    <Badge
                      variant={
                        item.isOld || item.tag === "Backlog" || item.tag === "Old Syllabus"
                          ? "peach"
                          : item.tag === "Regular"
                          ? "sage"
                          : "subtle"
                      }
                      className="rounded-full px-2 py-0.5 text-[10px] font-semibold"
                    >
                      {item.shortTag || item.tag}
                    </Badge>
                  </div>

                  <div className="flex items-center gap-1 shrink-0">
                    <span className="text-muted-foreground font-medium mr-1">
                      {item.date}
                    </span>
                    <Button
                      type="button"
                      variant="ghost"
                      size="icon"
                      onClick={() => openEditModal(item)}
                      className="h-6 w-6 text-muted-foreground hover:text-foreground"
                    >
                      <PencilEdit02Icon className="h-3 w-3" />
                    </Button>
                    <Button
                      type="button"
                      variant="ghost"
                      size="icon"
                      onClick={() => handleDeleteItem(item.id)}
                      className="h-6 w-6 text-muted-foreground hover:text-destructive"
                    >
                      <Delete02Icon className="h-3 w-3" />
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
