"use client";

import React, { useState, useEffect, useMemo, useRef } from "react";
import { ProgressRing } from "./progress-ring";
import { YearPills } from "./year-pills";
import { ControlPanel } from "./control-panel";
import { QuestionCard } from "./question-card";
import { PersonalNotesEditor } from "./personal-notes-editor";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Question, ChecklistFilters, TopicCluster } from "@/types";
import { EXAM_YEARS } from "@/lib/constants";
import rawProgress from "@/data/user_progress.json";

interface ChecklistViewProps {
  questions: Question[];
  clusters: TopicCluster[];
  unitTitles: Record<string, string>;
  storagePrefix?: string;
  onNotesCountChange?: (count: number) => void;
}

export function ChecklistView({
  questions,
  clusters,
  unitTitles,
  storagePrefix = "geotech",
  onNotesCountChange,
}: ChecklistViewProps) {
  const STORAGE_KEY_COMPLETED = `${storagePrefix}_completed_questions`;
  const STORAGE_KEY_STARRED = `${storagePrefix}_starred_questions`;
  const STORAGE_KEY_LATER = `${storagePrefix}_later_questions`;
  const STORAGE_KEY_NOTES = `${storagePrefix}_custom_notes`;
  const STORAGE_KEY_FILTERS = `${storagePrefix}_checklist_filters`;

  // 1. Storage-synced states (initialized consistently for SSR & client mount to prevent hydration mismatch)
  const [completed, setCompleted] = useState<Set<string>>(() => {
    const subjectKey = storagePrefix === "dhs" ? "dhs" : "geotech-2";
    const fallback = (rawProgress as any)?.subjects?.[subjectKey]?.completed_questions;
    if (Array.isArray(fallback) && fallback.length > 0) {
      return new Set(fallback);
    }
    return new Set();
  });

  const [starred, setStarred] = useState<Set<string>>(new Set());
  const [later, setLater] = useState<Set<string>>(new Set());
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

  // Sync state from localStorage after mount
  useEffect(() => {
    try {
      const savedCompleted = localStorage.getItem(STORAGE_KEY_COMPLETED);
      if (savedCompleted) {
        setCompleted(new Set(JSON.parse(savedCompleted)));
      }
      const savedStarred = localStorage.getItem(STORAGE_KEY_STARRED);
      if (savedStarred) setStarred(new Set(JSON.parse(savedStarred)));

      const savedLater = localStorage.getItem(STORAGE_KEY_LATER);
      if (savedLater) setLater(new Set(JSON.parse(savedLater)));

      const savedNotes = localStorage.getItem(STORAGE_KEY_NOTES);
      if (savedNotes) setNotes(JSON.parse(savedNotes));

      const savedFilters = localStorage.getItem(STORAGE_KEY_FILTERS);
      if (savedFilters) setFilters(JSON.parse(savedFilters));
    } catch (e) {
      console.warn("Error loading checklist state from localStorage:", e);
    } finally {
      hasHydratedRef.current = true;
    }
  }, [
    storagePrefix,
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

  // Save filters to localStorage only after hydration has completed
  useEffect(() => {
    if (!hasHydratedRef.current) return;
    try {
      localStorage.setItem(STORAGE_KEY_FILTERS, JSON.stringify(filters));
    } catch (e) {
      console.warn("Error saving filters:", e);
    }
  }, [filters, STORAGE_KEY_FILTERS]);

  // Accordion state
  const [openCards, setOpenCards] = useState<Set<string>>(new Set());
  const [editingQuestion, setEditingQuestion] = useState<Question | null>(null);

  // Toggle handlers
  const toggleComplete = (id: string) => {
    setCompleted((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      try {
        localStorage.setItem(STORAGE_KEY_COMPLETED, JSON.stringify([...next]));
      } catch (e) {
        console.warn("Error saving completed:", e);
      }
      return next;
    });
  };

  const toggleStar = (id: string) => {
    setStarred((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      try {
        localStorage.setItem(STORAGE_KEY_STARRED, JSON.stringify([...next]));
      } catch (e) {
        console.warn("Error saving starred:", e);
      }
      return next;
    });
  };

  const toggleLater = (id: string) => {
    setLater((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      try {
        localStorage.setItem(STORAGE_KEY_LATER, JSON.stringify([...next]));
      } catch (e) {
        console.warn("Error saving later:", e);
      }
      return next;
    });
  };

  const handleSaveNote = (questionId: string, noteText: string) => {
    setNotes((prev) => {
      const next = { ...prev };
      if (!noteText.trim()) delete next[questionId];
      else next[questionId] = noteText;
      try {
        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(next));
      } catch (e) {
        console.warn("Error saving notes:", e);
      }
      return next;
    });
  };

  const toggleCard = (id: string) => {
    setOpenCards((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
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

  const yearCounts = useMemo(() => {
    const counts: Record<string, { done: number; total: number }> = {};
    for (const y of years) {
      const yearQuestions = questions.filter((q) => String(q.year) === y);
      const doneCount = yearQuestions.filter((q) => completed.has(q.id)).length;
      counts[y] = { done: doneCount, total: yearQuestions.length };
    }
    return counts;
  }, [years, questions, completed]);

  // Filtered questions
  const filteredQuestions = useMemo(() => {
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

      // 7. Search filter
      if (filters.search) {
        const query = filters.search.toLowerCase();
        const text =
          `${q.q_no} ${q.question} ${q.topic} ${q.unit_name} ${q.solution}`.toLowerCase();
        if (!text.includes(query)) return false;
      }

      return true;
    });
  }, [questions, filters, completed, starred, later]);

  const allVisibleExpanded =
    filteredQuestions.length > 0 &&
    filteredQuestions.every((q) => openCards.has(q.id));

  const handleToggleExpandAll = () => {
    if (allVisibleExpanded) {
      setOpenCards(new Set());
    } else {
      setOpenCards(new Set(filteredQuestions.map((q) => q.id)));
    }
  };

  const handleResetFilters = () => {
    setFilters({
      year: "all",
      unit: "all",
      repeated: "all",
      type: "all",
      marks: "all",
      status: "all",
      search: "",
    });
  };

  // Check if "Most Repeated" mode is active
  const isRepeatedMode = filters.repeated !== "all";

  // Frequency tier organization for Repeated mode
  const repeatedTierSections = useMemo(() => {
    if (!isRepeatedMode) return null;

    // Cluster map
    const clusterMap = new Map<string, TopicCluster>();
    for (const c of clusters) {
      clusterMap.set(c.id, c);
    }

    // Group filtered questions by tier -> unit -> cluster
    const tiers: {
      tierName: string;
      tierMultiplier: string;
      probability: string;
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
        name: "Tier 1: 5x Repeated",
        prob: "100% Guaranteed Concepts",
        variant: "repeat5x" as const,
      },
      {
        mult: "4x",
        name: "Tier 1: 4x Repeated",
        prob: "100% Guaranteed Concepts",
        variant: "repeat4x" as const,
      },
      {
        mult: "3x",
        name: "Tier 2: 3x Repeated",
        prob: "75% High Probability Concepts",
        variant: "repeat3x" as const,
      },
      {
        mult: "2x",
        name: "Tier 3: 2x Repeated",
        prob: "50% Medium Probability Concepts",
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
        tierName: cfg.name,
        tierMultiplier: cfg.mult,
        probability: cfg.prob,
        badgeVariant: cfg.variant,
        units: unitList,
      });
    }

    return tiers;
  }, [isRepeatedMode, filteredQuestions, clusters, unitTitles, filters.repeated]);

  // Chronological Year -> Unit organization for normal mode
  const chronologicalSections = useMemo(() => {
    if (isRepeatedMode) return null;

    const sections: {
      year: string;
      units: {
        unitNum: number;
        unitTitle: string;
        questions: Question[];
      }[];
    }[] = [];

    const activeYears = filters.year === "all" ? years : [filters.year];

    for (const y of activeYears) {
      const yearQuestions = filteredQuestions.filter((q) => q.year === y);
      if (yearQuestions.length === 0) continue;

      const unitGroups: Record<number, Question[]> = {};
      for (const q of yearQuestions) {
        if (!unitGroups[q.unit]) unitGroups[q.unit] = [];
        unitGroups[q.unit].push(q);
      }

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
      {/* Header Row: Title, Progress Ring, Year Pills */}
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-lg sm:text-xl font-bold tracking-tight text-foreground">
            Checklist
          </h1>
        </div>

        <div className="flex items-center gap-2.5 max-w-full overflow-x-auto no-scrollbar pb-1 overscroll-x-contain">
          <ProgressRing
            completed={completed.size}
            total={questions.length}
            onClick={() =>
              setFilters((prev) => ({
                ...prev,
                status: prev.status === "incomplete" ? "all" : "incomplete",
              }))
            }
            isActiveFilter={filters.status === "incomplete"}
          />

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
            <div key={tier.tierName} className="space-y-6">
              {/* Tier Header */}
              <div className="flex items-center gap-3 pb-2">
                <Badge variant={tier.badgeVariant} className="text-xs font-bold px-2.5 py-0.5">
                  {tier.tierMultiplier}
                </Badge>
                <div>
                  <h2 className="text-sm sm:text-base font-semibold text-foreground">{tier.tierName}</h2>
                  <p className="text-xs text-muted-foreground">{tier.probability}</p>
                </div>
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
                      <div className="flex items-center gap-2 text-sm font-semibold text-foreground/90">
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
                  <h2 className="text-base sm:text-lg font-semibold tracking-tight text-foreground">
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

      {/* Personal Notes Editor Modal */}
      <PersonalNotesEditor
        question={editingQuestion}
        isOpen={!!editingQuestion}
        onClose={() => setEditingQuestion(null)}
        onSave={handleSaveNote}
        initialNote={editingQuestion ? notes[editingQuestion.id] : ""}
      />
    </div>
  );
}
