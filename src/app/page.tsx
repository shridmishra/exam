"use client";

import React, { useState, useEffect } from "react";
import { Header } from "@/components/header";
import { ChecklistView } from "@/components/checklist/checklist-view";
import { FormulasView } from "@/components/formulas/formulas-view";
import { TimetableView } from "@/components/timetable/timetable-view";
import { NotesArchiveView } from "@/components/notes/notes-archive-view";
import { MobileNav } from "@/components/common/mobile-nav";

import rawQuestions from "@/data/questions.json";
import rawClusters from "@/data/canonical.json";
import rawFormulas from "@/data/formulas.json";
import rawSubject from "@/data/subject.json";
import rawTimetable from "@/data/timetable.json";
import rawSubjects from "@/data/subjects.json";

import rawDhsQuestions from "@/data/dhs_questions.json";
import rawDhsClusters from "@/data/dhs_canonical.json";
import rawDhsFormulas from "@/data/dhs_formulas.json";
import rawDhsSubject from "@/data/dhs_subject.json";

import rawRccQuestions from "@/data/rcc_questions.json";
import rawRccClusters from "@/data/rcc_canonical.json";
import rawRccFormulas from "@/data/rcc_formulas.json";
import rawRccSubject from "@/data/rcc_subject.json";

import {
  Question,
  TopicCluster,
  MasterFormula,
  SubjectMeta,
  SubjectOption,
  ExamItem,
} from "@/types";
import { STORAGE_KEYS } from "@/lib/constants";

interface SubjectDataset {
  subject: SubjectMeta;
  questions: Question[];
  clusters: TopicCluster[];
  formulas: MasterFormula[];
}

const SUBJECTS_DATA: Record<string, SubjectDataset> = {
  "geotech-2": {
    subject: rawSubject as SubjectMeta,
    questions: rawQuestions as Question[],
    clusters: rawClusters as TopicCluster[],
    formulas: rawFormulas as MasterFormula[],
  },
  "dhs": {
    subject: rawDhsSubject as SubjectMeta,
    questions: (rawDhsQuestions as unknown) as Question[],
    clusters: rawDhsClusters as TopicCluster[],
    formulas: rawDhsFormulas as MasterFormula[],
  },
  "rcc": {
    subject: rawRccSubject as SubjectMeta,
    questions: (rawRccQuestions as unknown) as Question[],
    clusters: (rawRccClusters as unknown) as TopicCluster[],
    formulas: rawRccFormulas as MasterFormula[],
  },
};

const timetablePresets = rawTimetable as {
  default: ExamItem[];
  backlog: ExamItem[];
};

const STORAGE_KEY_ACTIVE_VIEW = STORAGE_KEYS.ACTIVE_VIEW;
const STORAGE_KEY_ACTIVE_SUBJECT = STORAGE_KEYS.ACTIVE_SUBJECT;

export default function Home() {
  const [selectedSubjectId, setSelectedSubjectId] = useState<string>("geotech-2");
  const [activeTab, setActiveTab] = useState<
    "checklist" | "formulas" | "timetable" | "notes"
  >("checklist");
  const [notesCount, setNotesCount] = useState(0);

  // Sync saved subject and view tab after client mount to eliminate SSR hydration mismatches
  useEffect(() => {
    try {
      const savedSubject = localStorage.getItem(STORAGE_KEY_ACTIVE_SUBJECT);
      if (savedSubject && SUBJECTS_DATA[savedSubject]) {
        setSelectedSubjectId(savedSubject);
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
    SUBJECTS_DATA[selectedSubjectId] || SUBJECTS_DATA["geotech-2"];
  const currentSubject = activeDataset.subject;
  const currentQuestions = activeDataset.questions;
  const currentClusters = activeDataset.clusters;
  const currentFormulas = activeDataset.formulas;
  const storagePrefix = currentSubject.storage_prefix || selectedSubjectId;

  const handleSelectSubject = (subjectId: string) => {
    if (SUBJECTS_DATA[subjectId]) {
      setSelectedSubjectId(subjectId);
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
          <TimetableView presets={timetablePresets} />
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
