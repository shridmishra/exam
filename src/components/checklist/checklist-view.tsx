"use client";

import React, { useState, useEffect, useMemo, useRef, useDeferredValue, useCallback } from "react";
import { ProgressRing } from "./progress-ring";
import { YearPills } from "./year-pills";
import { ControlPanel } from "./control-panel";
import { QuestionCard } from "./question-card";
import { PersonalNotesEditor } from "./personal-notes-editor";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { toast } from "@/components/ui/sonner";
import { Question, ChecklistFilters, TopicCluster } from "@/types";
import { EXAM_YEARS } from "@/lib/constants";

interface ChecklistViewProps {
  questions: Question[];
  clusters?: TopicCluster[];
  unitTitles: Record<string, string>;
  subjectName?: string;
  storagePrefix?: string;
  onNotesCountChange?: (count: number) => void;
}

export function ChecklistView({
  questions,
  clusters,
  unitTitles,
  subjectName,
  storagePrefix = "geotech",
  onNotesCountChange,
}: ChecklistViewProps) {
  const STORAGE_KEY_COMPLETED = `${storagePrefix}_completed_questions`;
  const STORAGE_KEY_STARRED = `${storagePrefix}_starred_questions`;
  const STORAGE_KEY_LATER = `${storagePrefix}_later_questions`;
  const STORAGE_KEY_NOTES = `${storagePrefix}_custom_notes`;
  const STORAGE_KEY_FILTERS = `${storagePrefix}_checklist_filters`;

  // 1. Storage-synced states (clean slate for SSR & fresh users; loaded purely from user's own browser localStorage)
  const [completed, setCompleted] = useState<Set<string>>(() => new Set());
  const [starred, setStarred] = useState<Set<string>>(() => new Set());
  const [later, setLater] = useState<Set<string>>(() => new Set());
  const [notes, setNotes] = useState<Record<string, string>>({});

  const [filters, setFilters] = useState<ChecklistFilters>({
    year: "all",
    unit: "all",
    repeated: "all",
    type: "all",
    marks: "all",
    status: "all",
    search: "",
  });

  const hasHydratedRef = useRef(false);

  // Dynamic cluster loading: only loaded on-demand when repeated mode is active
  const [loadedClusters, setLoadedClusters] = useState<TopicCluster[]>(clusters || []);

  useEffect(() => {
    if (clusters && clusters.length > 0) {
      setLoadedClusters(clusters);
      return;
    }

    if (filters.repeated !== "all" && loadedClusters.length === 0) {
      if (storagePrefix === "dhs") {
        import("@/data/dhs_canonical.json").then((m) =>
          setLoadedClusters(m.default as TopicCluster[])
        );
      } else if (storagePrefix === "rcc") {
        import("@/data/rcc_canonical.json").then((m) =>
          setLoadedClusters((m.default as unknown) as TopicCluster[])
        );
      } else {
        import("@/data/canonical.json").then((m) =>
          setLoadedClusters(m.default as TopicCluster[])
        );
      }
    }
  }, [filters.repeated, clusters, loadedClusters.length, storagePrefix]);

  // Sync state from localStorage after mount
  useEffect(() => {
    try {
      const validIds = new Set(questions.map((q) => q.id));

      const savedCompleted = localStorage.getItem(STORAGE_KEY_COMPLETED);
      if (savedCompleted) {
        try {
          const parsed = JSON.parse(savedCompleted);
          if (Array.isArray(parsed)) {
            // Strictly sanitize against current subject question IDs
            const sanitized = parsed.filter((id: string) => validIds.has(id));
            setCompleted(new Set(sanitized));
            // Self-healing: if localStorage was contaminated with foreign IDs, clean it up immediately
            if (sanitized.length !== parsed.length) {
              localStorage.setItem(
                STORAGE_KEY_COMPLETED,
                JSON.stringify(sanitized)
              );
            }
          }
        } catch (e) {
          console.warn("Error parsing completed questions:", e);
        }
      }
      const savedStarred = localStorage.getItem(STORAGE_KEY_STARRED);
      if (savedStarred) {
        try {
          const parsed = JSON.parse(savedStarred);
          if (Array.isArray(parsed)) {
            setStarred(new Set(parsed.filter((id: string) => validIds.has(id))));
          }
        } catch (e) {
          console.warn("Error parsing starred questions:", e);
        }
      }

      const savedLater = localStorage.getItem(STORAGE_KEY_LATER);
      if (savedLater) {
        try {
          const parsed = JSON.parse(savedLater);
          if (Array.isArray(parsed)) {
            setLater(new Set(parsed.filter((id: string) => validIds.has(id))));
          }
        } catch (e) {
          console.warn("Error parsing later questions:", e);
        }
      }

      const savedNotes = localStorage.getItem(STORAGE_KEY_NOTES);
      if (savedNotes) {
        try {
          setNotes(JSON.parse(savedNotes));
        } catch (e) {
          console.warn("Error parsing notes:", e);
        }
      }

      const savedFilters = localStorage.getItem(STORAGE_KEY_FILTERS);
      if (savedFilters) {
        try {
          setFilters(JSON.parse(savedFilters));
        } catch (e) {
          console.warn("Error parsing filters:", e);
        }
      }
    } catch (e) {
      console.warn("Error loading checklist state from localStorage:", e);
    } finally {
      hasHydratedRef.current = true;
    }
  }, [
    storagePrefix,
    questions,
    STORAGE_KEY_COMPLETED,
    STORAGE_KEY_STARRED,
    STORAGE_KEY_LATER,
    STORAGE_KEY_NOTES,
    STORAGE_KEY_FILTERS,
  ]);

  // Notify parent of notes count
  useEffect(() => {
    const count = Object.keys(notes).filter((k) => notes[k]?.trim()).length;
    onNotesCountChange?.(count);
  }, [notes, onNotesCountChange]);

  // Save filters to localStorage only after hydration has completed (debounced to avoid main-thread blocking on rapid typing)
  useEffect(() => {
    if (!hasHydratedRef.current) return;
    const timer = setTimeout(() => {
      try {
        localStorage.setItem(STORAGE_KEY_FILTERS, JSON.stringify(filters));
      } catch (e) {
        console.warn("Error saving filters:", e);
      }
    }, 300);

    return () => clearTimeout(timer);
  }, [filters, STORAGE_KEY_FILTERS]);

  // Accordion state
  const [openCards, setOpenCards] = useState<Set<string>>(new Set());
  const [editingQuestion, setEditingQuestion] = useState<Question | null>(null);

  // Question map for quick lookup and toast metadata
  const questionMap = useMemo(() => {
    const map = new Map<string, Question>();
    questions.forEach((q) => map.set(q.id, q));
    return map;
  }, [questions]);

  const getQNumberLabel = (q?: { q_no?: string }) => {
    if (!q?.q_no) return "Question";
    return q.q_no.startsWith("Q.") ? q.q_no : `Q.${q.q_no}`;
  };

  // Toggle handlers wrapped in useCallback to avoid recreating closures on re-render
  const toggleComplete = useCallback((id: string) => {
    const q = questionMap.get(id);
    const qLabel = getQNumberLabel(q);

    setCompleted((prev) => {
      const next = new Set(prev);
      const isNowCompleted = !next.has(id);
      if (next.has(id)) next.delete(id);
      else next.add(id);

      try {
        localStorage.setItem(STORAGE_KEY_COMPLETED, JSON.stringify([...next]));
      } catch (e) {
        console.warn("Error saving completed:", e);
      }

      if (isNowCompleted) {
        toast.success(`Completed ${qLabel}`, {
          description: q ? `${q.year} • Unit ${q.unit} (${q.marks}M)` : "Marked as completed",
          action: {
            label: "Undo",
            onClick: () => toggleComplete(id),
          },
        });
      } else {
        toast.info(`Marked ${qLabel} as incomplete`);
      }

      return next;
    });
  }, [questionMap, STORAGE_KEY_COMPLETED]);

  const toggleStar = useCallback((id: string) => {
    const q = questionMap.get(id);
    const qLabel = getQNumberLabel(q);

    setStarred((prev) => {
      const next = new Set(prev);
      const isNowStarred = !next.has(id);
      if (next.has(id)) next.delete(id);
      else next.add(id);

      try {
        localStorage.setItem(STORAGE_KEY_STARRED, JSON.stringify([...next]));
      } catch (e) {
        console.warn("Error saving starred:", e);
      }

      if (isNowStarred) {
        toast.success(`Starred ${qLabel}`, {
          description: "Added to priority revision list",
        });
      } else {
        toast.info(`Unstarred ${qLabel}`);
      }

      return next;
    });
  }, [questionMap, STORAGE_KEY_STARRED]);

  const toggleLater = useCallback((id: string) => {
    const q = questionMap.get(id);
    const qLabel = getQNumberLabel(q);

    setLater((prev) => {
      const next = new Set(prev);
      const isNowLater = !next.has(id);
      if (next.has(id)) next.delete(id);
      else next.add(id);

      try {
        localStorage.setItem(STORAGE_KEY_LATER, JSON.stringify([...next]));
      } catch (e) {
        console.warn("Error saving later:", e);
      }

      if (isNowLater) {
        toast.success(`Saved ${qLabel} for later`, {
          description: "Filter by Status > Later to review",
        });
      } else {
        toast.info(`Removed ${qLabel} from later`);
      }

      return next;
    });
  }, [questionMap, STORAGE_KEY_LATER]);

  const handleSaveNote = useCallback((questionId: string, noteText: string) => {
    const q = questionMap.get(questionId);
    const qLabel = getQNumberLabel(q);

    setNotes((prev) => {
      const next = { ...prev };
      if (!noteText.trim()) {
        delete next[questionId];
        toast.info(`Personal note removed for ${qLabel}`);
      } else {
        next[questionId] = noteText;
        toast.success(`Personal note saved for ${qLabel}`, {
          description: "Your custom notes are saved locally",
        });
      }

      try {
        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(next));
      } catch (e) {
        console.warn("Error saving notes:", e);
      }

      return next;
    });
  }, [questionMap, STORAGE_KEY_NOTES]);

  const toggleCard = useCallback((id: string) => {
    setOpenCards((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  }, []);

  const handleResetProgress = () => {
    if (
      window.confirm(
        "Reset all completed questions for this subject? This clears your progress in this browser."
      )
    ) {
      setCompleted(new Set());
      try {
        localStorage.removeItem(STORAGE_KEY_COMPLETED);
      } catch (e) {
        console.warn("Error clearing completed questions:", e);
      }
      toast.success("Progress reset successfully", {
        description: "All completed marks cleared for this subject",
      });
    }
  };

  // Dynamic Year List based on questions present in subject
  const years = useMemo(() => {
    const setY = new Set<string>();
    questions.forEach((q) => {
      if (q.year) setY.add(String(q.year));
    });
    if (setY.size === 0) return ["2025", "2024", "2023", "2022"];
    return Array.from(setY).sort((a, b) => Number(b) - Number(a));
  }, [questions]);

  // Total completed questions belonging strictly to this subject
  const completedCount = useMemo(
    () => questions.filter((q) => completed.has(q.id)).length,
    [questions, completed]
  );

  const yearCounts = useMemo(() => {
    const counts: Record<string, { done: number; total: number }> = {};
    for (const y of years) {
      counts[y] = { done: 0, total: 0 };
    }
    for (const q of questions) {
      const y = String(q.year);
      if (!counts[y]) {
        counts[y] = { done: 0, total: 0 };
      }
      counts[y].total++;
      if (completed.has(q.id)) {
        counts[y].done++;
      }
    }
    return counts;
  }, [years, questions, completed]);

  // Deferred search value to ensure responsive 60fps/120fps input typing
  const deferredSearch = useDeferredValue(filters.search);

  // Pre-computed lowercase searchable index for sub-millisecond filtering without string allocations
  const searchableTextMap = useMemo(() => {
    const map = new Map<string, string>();
    for (const q of questions) {
      map.set(
        q.id,
        `${q.q_no} ${q.question} ${q.topic} ${q.unit_name} ${q.solution || q.formatted_solution || ""}`.toLowerCase()
      );
    }
    return map;
  }, [questions]);

  // Filtered questions
  const filteredQuestions = useMemo(() => {
    const searchQuery = deferredSearch ? deferredSearch.toLowerCase().trim() : "";

    return questions.filter((q) => {
      // 1. Year filter
      if (filters.year !== "all" && q.year !== filters.year) return false;

      // 2. Unit filter
      if (filters.unit !== "all" && String(q.unit) !== filters.unit)
        return false;

      // 3. Repeated filter
      if (filters.repeated === "repeated") {
        if (!q.repeated && q.repeat_multiplier === "1x") return false;
      } else if (filters.repeated !== "all") {
        if (q.repeat_multiplier !== filters.repeated) return false;
      }

      // 4. Type filter
      if (
        filters.type !== "all" &&
        !q.type.toLowerCase().includes(filters.type.toLowerCase())
      )
        return false;

      // 5. Marks filter
      if (filters.marks === "2" && q.marks !== 2) return false;
      if (filters.marks === "3" && q.marks !== 3) return false;
      if (filters.marks === "7" && q.marks !== 7 && q.marks !== 6) return false;

      // 6. Status filter
      if (filters.status === "incomplete" && completed.has(q.id)) return false;
      if (filters.status === "completed" && !completed.has(q.id)) return false;
      if (filters.status === "starred" && !starred.has(q.id)) return false;
      if (filters.status === "later" && !later.has(q.id)) return false;

      // 7. Search filter (using fast index lookup)
      if (searchQuery) {
        const text = searchableTextMap.get(q.id) || "";
        if (!text.includes(searchQuery)) return false;
      }

      return true;
    });
  }, [questions, filters, deferredSearch, completed, starred, later, searchableTextMap]);

  const allVisibleExpanded =
    filteredQuestions.length > 0 &&
    filteredQuestions.every((q) => openCards.has(q.id));

  const handleToggleExpandAll = useCallback(() => {
    if (allVisibleExpanded) {
      setOpenCards(new Set());
      toast.info("Collapsed all questions");
    } else {
      setOpenCards(new Set(filteredQuestions.map((q) => q.id)));
      toast.info(`Expanded ${filteredQuestions.length} questions`);
    }
  }, [allVisibleExpanded, filteredQuestions]);

  const handleResetFilters = useCallback(() => {
    setFilters({
      year: "all",
      unit: "all",
      repeated: "all",
      type: "all",
      marks: "all",
      status: "all",
      search: "",
    });
    toast.info("Filters reset to default");
  }, []);

  // Check if "Most Repeated" mode is active
  const isRepeatedMode = filters.repeated !== "all";

  // Frequency tier organization for Repeated mode
  const repeatedTierSections = useMemo(() => {
    if (!isRepeatedMode) return null;

    // Cluster map
    const clusterMap = new Map<string, TopicCluster>();
    for (const c of loadedClusters) {
      clusterMap.set(c.id, c);
    }

    // Group filtered questions by tier -> unit -> cluster
    const tiers: {
      tierMultiplier: string;
      badgeVariant: "repeat5x" | "repeat4x" | "repeat3x" | "repeat2x";
      units: {
        unitNum: number;
        unitTitle: string;
        topics: {
          cluster: TopicCluster | null;
          title: string;
          questions: Question[];
        }[];
      }[];
    }[] = [];

    const tierConfigs = [
      {
        mult: "5x",
        variant: "repeat5x" as const,
      },
      {
        mult: "4x",
        variant: "repeat4x" as const,
      },
      {
        mult: "3x",
        variant: "repeat3x" as const,
      },
      {
        mult: "2x",
        variant: "repeat2x" as const,
      },
    ];

    for (const cfg of tierConfigs) {
      if (filters.repeated !== "all" && filters.repeated !== "repeated" && filters.repeated !== cfg.mult) {
        continue;
      }

      const tierQuestions = filteredQuestions.filter(
        (q) => q.repeat_multiplier === cfg.mult
      );
      if (tierQuestions.length === 0) continue;

      // Group by Unit
      const unitGroups: Record<number, Question[]> = {};
      for (const q of tierQuestions) {
        if (!unitGroups[q.unit]) unitGroups[q.unit] = [];
        unitGroups[q.unit].push(q);
      }

      const unitList = Object.keys(unitGroups)
        .map(Number)
        .sort((a, b) => a - b)
        .map((uNum) => {
          const uQs = unitGroups[uNum];
          // Group by canonical cluster or topic
          const topicMap: Record<string, Question[]> = {};
          for (const q of uQs) {
            const key = q.cluster_id || q.topic;
            if (!topicMap[key]) topicMap[key] = [];
            topicMap[key].push(q);
          }

          const topics = Object.entries(topicMap).map(([key, qList]) => {
            const cluster = clusterMap.get(key) || null;
            const title = cluster?.title || qList[0].topic;
            // Sort questions chronologically 2025 -> 2024 -> 2023 -> 2022
            qList.sort((a, b) => Number(b.year) - Number(a.year));
            return {
              cluster,
              title,
              questions: qList,
            };
          });

          return {
            unitNum: uNum,
            unitTitle: unitTitles[String(uNum)] || `Unit ${uNum}`,
            topics,
          };
        });

      tiers.push({
        tierMultiplier: cfg.mult,
        badgeVariant: cfg.variant,
        units: unitList,
      });
    }

    return tiers;
  }, [isRepeatedMode, filteredQuestions, loadedClusters, unitTitles, filters.repeated]);

  // Chronological Year -> Unit organization for normal mode (single-pass O(N) grouping)
  const chronologicalSections = useMemo(() => {
    if (isRepeatedMode) return null;

    const activeYears = filters.year === "all" ? years : [filters.year];
    const allowedYears = new Set(activeYears);

    // Single-pass O(N) grouping: year -> unit -> questions
    const grouped: Record<string, Record<number, Question[]>> = {};
    for (const q of filteredQuestions) {
      if (!allowedYears.has(q.year)) continue;
      if (!grouped[q.year]) grouped[q.year] = {};
      if (!grouped[q.year][q.unit]) grouped[q.year][q.unit] = [];
      grouped[q.year][q.unit].push(q);
    }

    const sections: {
      year: string;
      units: {
        unitNum: number;
        unitTitle: string;
        questions: Question[];
      }[];
    }[] = [];

    for (const y of activeYears) {
      const unitGroups = grouped[y];
      if (!unitGroups) continue;

      const unitList = Object.keys(unitGroups)
        .map(Number)
        .sort((a, b) => a - b)
        .map((uNum) => ({
          unitNum: uNum,
          unitTitle: unitTitles[String(uNum)] || `Unit ${uNum}`,
          questions: unitGroups[uNum],
        }));

      sections.push({
        year: y,
        units: unitList,
      });
    }

    return sections;
  }, [isRepeatedMode, filteredQuestions, filters.year, unitTitles, years]);

  return (
    <div className="space-y-6">
      {/* Header Row: Title (Left), Progress Ring & Year Pills (Right) */}
      <div className="flex w-full flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex items-center gap-2.5">
          <h1 className="font-heading text-lg sm:text-xl font-bold tracking-tight text-foreground">
            Checklist
            {subjectName && (
              <span className="sr-only">
                {" "}
                — {subjectName} Previous Year Questions &amp; Analysis
              </span>
            )}
          </h1>
        </div>

        <div className="flex items-center gap-2.5 max-w-full overflow-x-auto no-scrollbar pb-1 overscroll-x-contain sm:ml-auto shrink-0">
          <div className="flex items-center gap-1.5 shrink-0">
            <ProgressRing
              completed={completedCount}
              total={questions.length}
              onClick={() =>
                setFilters((prev) => ({
                  ...prev,
                  status: prev.status === "incomplete" ? "all" : "incomplete",
                }))
              }
              isActiveFilter={filters.status === "incomplete"}
            />
            {completedCount > 0 && (
              <Button
                type="button"
                variant="ghost"
                size="sm"
                onClick={handleResetProgress}
                className="h-7 px-2 text-[11px] text-muted-foreground hover:text-destructive hover:bg-destructive/10 transition-colors shrink-0"
                title="Reset completed questions for this subject in your browser"
              >
                Reset Done
              </Button>
            )}
          </div>

          <YearPills
            years={years}
            counts={yearCounts}
            activeYear={filters.year}
            onSelectYear={(y) =>
              setFilters((prev) => ({
                ...prev,
                year: prev.year === y ? "all" : y,
              }))
            }
          />
        </div>
      </div>

      {/* Control Panel: 6 Dimensions + Search */}
      <ControlPanel
        filters={filters}
        setFilters={setFilters}
        matchCount={filteredQuestions.length}
        totalCount={questions.length}
        allExpanded={allVisibleExpanded}
        onToggleExpandAll={handleToggleExpandAll}
        onResetFilters={handleResetFilters}
        availableYears={years}
      />

      {/* Zero Matches Empty State */}
      {filteredQuestions.length === 0 && (
        <div className="flex flex-col items-center justify-center rounded-2xl bg-card p-10 text-center shadow-xs">
          <p className="text-base font-semibold text-foreground">
            No questions match your current filters
          </p>
          <p className="text-xs text-muted-foreground mt-1 max-w-sm">
            Try adjusting your search query or reset filter dimensions to view questions.
          </p>
          <Button
            variant="secondary"
            size="sm"
            onClick={handleResetFilters}
            className="mt-4 text-xs"
          >
            Reset Filters
          </Button>
        </div>
      )}

      {/* Repeated Mode: Organized by Tier -> Unit -> Canonical Concept */}
      {isRepeatedMode && repeatedTierSections && (
        <div className="space-y-10">
          {repeatedTierSections.map((tier) => (
            <div key={tier.tierMultiplier} className="space-y-6">
              {/* Tier Header */}
              <div className="flex items-center gap-2 pb-2 border-b border-border/40">
                <Badge variant={tier.badgeVariant} className="text-xs font-bold px-2.5 py-0.5">
                  {tier.tierMultiplier}
                </Badge>
                <span className="text-xs text-muted-foreground">
                  {tier.units.reduce(
                    (acc, u) =>
                      acc +
                      u.topics.reduce((tAcc, t) => tAcc + t.questions.length, 0),
                    0
                  )}{" "}
                  questions
                </span>
              </div>

              {/* Units within Tier */}
              {tier.units.map((u) => (
                <div key={u.unitNum} className="space-y-4 pl-1 sm:pl-3">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold uppercase tracking-wider text-muted-foreground">
                      Unit {u.unitNum} &bull; {u.unitTitle}
                    </span>
                  </div>

                  {/* Topics within Unit */}
                  {u.topics.map((t, idx) => (
                    <div key={idx} className="space-y-3 pt-2">
                      <div className="flex items-center gap-2 text-sm font-semibold text-foreground/90 font-heading">
                        <span className="h-1.5 w-1.5 rounded-full bg-primary" />
                        <span>{t.title}</span>
                      </div>

                      <div className="space-y-2.5">
                        {t.questions.map((q) => (
                          <QuestionCard
                            key={q.id}
                            question={q}
                            isOpen={openCards.has(q.id)}
                            onToggleOpen={() => toggleCard(q.id)}
                            isCompleted={completed.has(q.id)}
                            onToggleComplete={() => toggleComplete(q.id)}
                            isStarred={starred.has(q.id)}
                            onToggleStar={() => toggleStar(q.id)}
                            isLater={later.has(q.id)}
                            onToggleLater={() => toggleLater(q.id)}
                            personalNote={notes[q.id]}
                            onOpenNotesEditor={() => setEditingQuestion(q)}
                          />
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {/* Normal Mode: Chronological Year -> Unit */}
      {!isRepeatedMode && chronologicalSections && (
        <div className="space-y-10">
          {chronologicalSections.map((sec) => (
            <div key={sec.year} id={`year-section-${sec.year}`} className="space-y-6">
              {/* Year Section Divider */}
              <div className="flex items-center justify-between pb-1.5 pt-2 border-b border-border/30">
                <div className="flex items-center gap-2.5">
                  <Badge
                    variant={(["2025", "2024", "2023", "2022", "2019"].includes(String(sec.year)) ? `year${sec.year}` : "secondary") as any}
                    className="text-xs px-2.5 py-0.5 font-bold shadow-2xs"
                  >
                    {sec.year}
                  </Badge>
                  <h2 className="font-heading text-base sm:text-lg font-semibold tracking-tight text-foreground">
                    Examination Paper
                  </h2>
                  <Badge variant="subtle" className="text-xs tabular-nums text-muted-foreground font-medium">
                    {yearCounts[sec.year]?.done || 0}/{yearCounts[sec.year]?.total || 0} Done
                  </Badge>
                </div>
              </div>

              {/* Units within Year */}
              {sec.units.map((u) => (
                <div key={u.unitNum} className="space-y-3">
                  <div className="flex items-center gap-2">
                    <Badge variant="subtle" className="text-xs font-semibold">
                      Unit {u.unitNum}
                    </Badge>
                    <span className="text-xs font-medium text-muted-foreground">
                      {u.unitTitle}
                    </span>
                  </div>

                  <div className="space-y-2.5">
                    {u.questions.map((q) => (
                      <QuestionCard
                        key={q.id}
                        question={q}
                        isOpen={openCards.has(q.id)}
                        onToggleOpen={() => toggleCard(q.id)}
                        isCompleted={completed.has(q.id)}
                        onToggleComplete={() => toggleComplete(q.id)}
                        isStarred={starred.has(q.id)}
                        onToggleStar={() => toggleStar(q.id)}
                        isLater={later.has(q.id)}
                        onToggleLater={() => toggleLater(q.id)}
                        personalNote={notes[q.id]}
                        onOpenNotesEditor={() => setEditingQuestion(q)}
                      />
                    ))}
                  </div>
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {/* Personal Notes Editor Modal (Mounted only when active) */}
      {editingQuestion && (
        <PersonalNotesEditor
          question={editingQuestion}
          isOpen={true}
          onClose={() => setEditingQuestion(null)}
          onSave={handleSaveNote}
          initialNote={notes[editingQuestion.id] || ""}
        />
      )}
    </div>
  );
}
