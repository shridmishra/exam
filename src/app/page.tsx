"use client";

import React, { useState, useEffect } from "react";
import dynamic from "next/dynamic";
import { Header } from "@/components/header";
import { ChecklistView } from "@/components/checklist/checklist-view";
import { MobileNav } from "@/components/common/mobile-nav";
import { toast } from "@/components/ui/sonner";

// Statically import only the default subject questions, subject meta, and subjects registry
import rawQuestions from "@/data/questions.json";
import rawSubject from "@/data/subject.json";
import rawSubjects from "@/data/subjects.json";

import {
  Question,
  TopicCluster,
  MasterFormula,
  SubjectMeta,
  SubjectOption,
} from "@/types";
import { STORAGE_KEYS } from "@/lib/constants";

// Lazy-loaded views to reduce initial bundle and execution overhead
const FormulasView = dynamic(
  () =>
    import("@/components/formulas/formulas-view").then(
      (mod) => mod.FormulasView
    ),
  {
    loading: () => (
      <div className="py-16 text-center text-sm text-muted-foreground animate-pulse">
        Loading Formulas...
      </div>
    ),
  }
);

const TimetableView = dynamic(
  () =>
    import("@/components/timetable/timetable-view").then(
      (mod) => mod.TimetableView
    ),
  {
    loading: () => (
      <div className="py-16 text-center text-sm text-muted-foreground animate-pulse">
        Loading Examination Timetable...
      </div>
    ),
  }
);

const NotesArchiveView = dynamic(
  () =>
    import("@/components/notes/notes-archive-view").then(
      (mod) => mod.NotesArchiveView
    ),
  {
    loading: () => (
      <div className="py-16 text-center text-sm text-muted-foreground animate-pulse">
        Loading Notes Archive...
      </div>
    ),
  }
);

interface SubjectDataset {
  subject: SubjectMeta;
  questions: Question[];
  clusters?: TopicCluster[];
  formulas?: MasterFormula[];
}

const GEOTECH_DATASET: SubjectDataset = {
  subject: rawSubject as SubjectMeta,
  questions: rawQuestions as Question[],
};

// In-memory cache for loaded subject datasets to avoid re-fetching
const loadedSubjectsCache: Record<string, SubjectDataset> = {
  "geotech-2": GEOTECH_DATASET,
};

async function fetchSubjectDataset(subjectId: string): Promise<SubjectDataset | null> {
  if (loadedSubjectsCache[subjectId]) {
    return loadedSubjectsCache[subjectId];
  }

  if (subjectId === "dhs") {
    const [sub, q, f] = await Promise.all([
      import("@/data/dhs_subject.json"),
      import("@/data/dhs_questions.json"),
      import("@/data/dhs_formulas.json"),
    ]);
    const dataset: SubjectDataset = {
      subject: sub.default as SubjectMeta,
      questions: q.default as unknown as Question[],
      formulas: f.default as MasterFormula[],
    };
    loadedSubjectsCache["dhs"] = dataset;
    return dataset;
  }

  if (subjectId === "rcc") {
    const [sub, q, f] = await Promise.all([
      import("@/data/rcc_subject.json"),
      import("@/data/rcc_questions.json"),
      import("@/data/rcc_formulas.json"),
    ]);
    const dataset: SubjectDataset = {
      subject: sub.default as SubjectMeta,
      questions: q.default as unknown as Question[],
      formulas: f.default as MasterFormula[],
    };
    loadedSubjectsCache["rcc"] = dataset;
    return dataset;
  }

  return null;
}

const STORAGE_KEY_ACTIVE_VIEW = STORAGE_KEYS.ACTIVE_VIEW;
const STORAGE_KEY_ACTIVE_SUBJECT = STORAGE_KEYS.ACTIVE_SUBJECT;

export default function Home() {
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>("geotech-2");
  const [activeTab, setActiveTab] = useState<
    "checklist" | "formulas" | "timetable" | "notes"
  >("checklist");
  const [notesCount, setNotesCount] = useState(0);
  const [subjectDatasets, setSubjectDatasets] = useState<Record<string, SubjectDataset>>(loadedSubjectsCache);
  const [isSwitchingSubject, setIsSwitchingSubject] = useState(false);

  // Sync saved subject and view tab after client mount to eliminate SSR hydration mismatches
  useEffect(() => {
    try {
      const savedSubject = localStorage.getItem(STORAGE_KEY_ACTIVE_SUBJECT);
      if (savedSubject && savedSubject !== "geotech-2") {
        fetchSubjectDataset(savedSubject).then((data) => {
          if (data) {
            setSubjectDatasets((prev) => ({ ...prev, [savedSubject]: data }));
            setSelectedSubjectId(savedSubject);
          }
        });
      }

      const savedTab = localStorage.getItem(STORAGE_KEY_ACTIVE_VIEW);
      if (
        savedTab === "checklist" ||
        savedTab === "formulas" ||
        savedTab === "timetable" ||
        savedTab === "notes"
      ) {
        setActiveTab(savedTab);
      }
    } catch (e) {
      console.warn("Failed to read localStorage:", e);
    }
  }, []);

  // Persist selected subject
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY_ACTIVE_SUBJECT, selectedSubjectId);
    } catch (e) {
      console.warn("Failed to save active subject:", e);
    }
  }, [selectedSubjectId]);

  // Persist active view tab
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY_ACTIVE_VIEW, activeTab);
    } catch (e) {
      console.warn("Failed to save active view:", e);
    }
  }, [activeTab]);

  const activeDataset =
    subjectDatasets[selectedSubjectId] || GEOTECH_DATASET;
  const currentSubject = activeDataset.subject;
  const currentQuestions = activeDataset.questions;
  const currentClusters = activeDataset.clusters;
  const currentFormulas = activeDataset.formulas;
  const storagePrefix = currentSubject.storage_prefix || selectedSubjectId;

  const handleSelectSubject = async (subjectId: string) => {
    if (subjectId === selectedSubjectId) return;

    if (subjectDatasets[subjectId]) {
      setSelectedSubjectId(subjectId);
      const sub = subjectDatasets[subjectId].subject;
      toast.success(`Switched to ${sub.name}`, {
        description: `${sub.code} syllabus & questions loaded`,
      });
      return;
    }

    setIsSwitchingSubject(true);
    try {
      const data = await fetchSubjectDataset(subjectId);
      if (data) {
        setSubjectDatasets((prev) => ({ ...prev, [subjectId]: data }));
        setSelectedSubjectId(subjectId);
        toast.success(`Switched to ${data.subject.name}`, {
          description: `${data.subject.code} syllabus & questions loaded`,
        });
      }
    } catch (e) {
      console.error("Failed to load subject dataset:", e);
      toast.error("Failed to load subject dataset");
    } finally {
      setIsSwitchingSubject(false);
    }
  };

  return (
    <div className="flex min-h-screen flex-col bg-background">
      <Header
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        selectedSubjectId={selectedSubjectId}
        onSelectSubject={handleSelectSubject}
        subjects={rawSubjects as SubjectOption[]}
        subjectName={currentSubject.name}
        notesCount={notesCount}
      />

      <main className="container flex-1 py-4 sm:py-6 md:py-8 pb-24 md:pb-8">
        {isSwitchingSubject ? (
          <div className="flex flex-col items-center justify-center py-20 text-center">
            <div className="h-6 w-6 animate-spin rounded-full border-2 border-primary border-t-transparent mb-3" />
            <p className="text-sm text-muted-foreground">Loading subject syllabus & questions...</p>
          </div>
        ) : (
          <>
            {activeTab === "checklist" && (
              <ChecklistView
                key={selectedSubjectId}
                questions={currentQuestions}
                clusters={currentClusters}
                unitTitles={currentSubject.unit_titles}
                storagePrefix={storagePrefix}
                onNotesCountChange={setNotesCount}
              />
            )}

            {activeTab === "formulas" && (
              <FormulasView
                key={selectedSubjectId}
                formulas={currentFormulas}
                unitTitles={currentSubject.unit_titles}
              />
            )}

            {activeTab === "timetable" && (
              <TimetableView />
            )}

            {activeTab === "notes" && (
              <NotesArchiveView
                key={selectedSubjectId}
                questions={currentQuestions}
                onOpenQuestion={() => {
                  setActiveTab("checklist");
                }}
              />
            )}
          </>
        )}
      </main>

      <footer className="py-6 pb-20 md:pb-8 text-center text-xs text-muted-foreground">
        <div className="container">
          <p>
            {currentSubject.name} ({currentSubject.code}) &bull; Exam Intelligence &amp; PYQ Mastery Platform
          </p>
        </div>
      </footer>

      <MobileNav
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />
    </div>
  );
}
