"use client";

import React, { useState, useEffect } from "react";
import {
  Download01Icon,
  Upload01Icon,
  Copy01Icon,
  Delete02Icon,
  Note01Icon,
  Tick02Icon,
  PencilEdit01Icon,
} from "@/components/ui/icons";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { RichMathText } from "@/components/common/math-renderer";
import { Question } from "@/types";
import { STORAGE_KEYS } from "@/lib/constants";

interface NotesArchiveViewProps {
  questions: Question[];
  onOpenQuestion?: (questionId: string) => void;
}

const STORAGE_KEY_NOTES = STORAGE_KEYS.NOTES;
const STORAGE_KEY_SCRATCHPAD = STORAGE_KEYS.SCRATCHPAD;

export function NotesArchiveView({
  questions,
  onOpenQuestion,
}: NotesArchiveViewProps) {
  const [notes, setNotes] = useState<Record<string, string>>(() => {
    if (typeof window === "undefined") return {};
    try {
      const saved = localStorage.getItem(STORAGE_KEY_NOTES);
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  const [scratchpad, setScratchpad] = useState<string>(() => {
    if (typeof window === "undefined") return "";
    try {
      return localStorage.getItem(STORAGE_KEY_SCRATCHPAD) || "";
    } catch {
      return "";
    }
  });

  const [copied, setCopied] = useState(false);
  const [scratchpadPreview, setScratchpadPreview] = useState(false);

  // Save scratchpad
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY_SCRATCHPAD, scratchpad);
    } catch (e) {
      console.warn("Error saving scratchpad:", e);
    }
  }, [scratchpad]);

  // Question lookup map
  const questionMap = new Map<string, Question>();
  for (const q of questions) {
    questionMap.set(q.id, q);
  }

  const savedNotesList = Object.entries(notes)
    .filter(([_, content]) => content && content.trim())
    .map(([qid, content]) => ({
      question: questionMap.get(qid),
      questionId: qid,
      content,
    }));

  const handleDeleteNote = (qid: string) => {
    setNotes((prev) => {
      const next = { ...prev };
      delete next[qid];
      try {
        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(next));
      } catch (e) {
        console.warn("Error deleting note:", e);
      }
      return next;
    });
  };

  const handleExportJSON = () => {
    const data = {
      notes,
      scratchpad,
      exportedAt: new Date().toISOString(),
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `geotech_notes_backup_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleImportJSON = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const data = JSON.parse(event.target?.result as string);
        if (data.notes) {
          setNotes(data.notes);
          localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(data.notes));
        }
        if (data.scratchpad) {
          setScratchpad(data.scratchpad);
          localStorage.setItem(STORAGE_KEY_SCRATCHPAD, data.scratchpad);
        }
        alert("Notes and scratchpad restored successfully!");
      } catch (err) {
        alert("Failed to parse backup JSON file.");
      }
    };
    reader.readAsText(file);
    e.target.value = "";
  };

  const handleCopyAll = () => {
    const lines: string[] = ["# Geotechnical Engineering - II Personal Study Notes\n"];

    if (scratchpad.trim()) {
      lines.push("## General Subject Notes / Scratchpad\n", scratchpad, "\n---\n");
    }

    for (const item of savedNotesList) {
      const q = item.question;
      lines.push(
        `### ${q?.q_no || item.questionId} (${q?.year || ""} - Unit ${q?.unit || ""})`,
        `Question: ${q?.question || ""}`,
        `Note:\n${item.content}\n`
      );
    }

    navigator.clipboard.writeText(lines.join("\n"));
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-6">
      {/* Title & Actions */}
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-lg sm:text-xl font-bold tracking-tight text-foreground">
            Personal Study Archive
          </h1>
          <h2 className="text-[11px] sm:text-xs font-medium text-muted-foreground mt-0.5">
            Notes &amp; Custom Answers
          </h2>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <Button
            variant="outline"
            size="sm"
            onClick={handleExportJSON}
            className="text-xs gap-1.5"
          >
            <Download01Icon className="h-3.5 w-3.5" />
            Export Backup
          </Button>

          <label>
            <Button
              variant="outline"
              size="sm"
              asChild
              className="text-xs gap-1.5 cursor-pointer"
            >
              <span>
                <Upload01Icon className="h-3.5 w-3.5" />
                Import
              </span>
            </Button>
            <Input
              type="file"
              accept=".json"
              onChange={handleImportJSON}
              className="hidden"
            />
          </label>

          <Button
            variant="outline"
            size="sm"
            onClick={handleCopyAll}
            className="text-xs gap-1.5"
          >
            {copied ? (
              <>
                <Tick02Icon className="h-3.5 w-3.5 text-emerald-500" />
                Copied!
              </>
            ) : (
              <>
                <Copy01Icon className="h-3.5 w-3.5" />
                Copy All
              </>
            )}
          </Button>
        </div>
      </div>

      {/* General Scratchpad Card */}
      <Card className="shadow-sm">
        <CardHeader className="p-4 pb-2">
          <div className="flex items-center justify-between">
            <CardTitle className="text-base font-bold text-foreground flex items-center gap-2">
              <Note01Icon className="h-4 w-4" />
              General Revision Scratchpad
            </CardTitle>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setScratchpadPreview(!scratchpadPreview)}
              className="h-7 text-xs"
            >
              <PencilEdit01Icon className="h-3.5 w-3.5 mr-1" />
              {scratchpadPreview ? "Edit Scratchpad" : "Preview"}
            </Button>
          </div>
        </CardHeader>
        <CardContent className="p-4 pt-2">
          {scratchpadPreview ? (
            <div className="min-h-[140px] rounded-xl bg-secondary/40 p-4 text-sm">
              {scratchpad.trim() ? (
                <RichMathText text={scratchpad} />
              ) : (
                <span className="text-muted-foreground italic">
                  Scratchpad is empty.
                </span>
              )}
            </div>
          ) : (
            <Textarea
              placeholder="Jot down quick reminders, key exam formulas ($...$ or $$...$$), or high-priority revision topics..."
              value={scratchpad}
              onChange={(e) => setScratchpad(e.target.value)}
              className="min-h-[140px] text-sm leading-relaxed"
            />
          )}
        </CardContent>
      </Card>

      {/* Saved Notes for PYQ Questions */}
      <div className="space-y-4">
        <h2 className="text-sm sm:text-base font-semibold text-foreground">
          Question Notes ({savedNotesList.length})
        </h2>

        {savedNotesList.length === 0 ? (
          <div className="rounded-2xl bg-card p-8 text-center text-muted-foreground text-sm shadow-xs">
            You haven&apos;t saved any personal notes on questions yet. Click the note
            icon on any question card in the Checklist to add one!
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-4">
            {savedNotesList.map((item) => {
              const q = item.question;
              return (
                <Card key={item.questionId} className="shadow-sm">
                  <CardHeader className="p-4 pb-2">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-foreground">
                          {q?.q_no || item.questionId}
                        </span>
                        {q?.year && (
                          <Badge variant="subtle" className="text-[10px]">
                            {q.year}
                          </Badge>
                        )}
                        {q?.unit && (
                          <Badge variant="subtle" className="text-[10px]">
                            Unit {q.unit}
                          </Badge>
                        )}
                      </div>

                      <div className="flex items-center gap-1">
                        {onOpenQuestion && (
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() => onOpenQuestion(item.questionId)}
                            className="h-7 text-xs"
                          >
                            Open in Checklist
                          </Button>
                        )}
                        <Button
                          variant="ghost"
                          size="icon"
                          onClick={() => handleDeleteNote(item.questionId)}
                          className="h-7 w-7 text-muted-foreground hover:text-destructive"
                          title="Delete Note"
                        >
                          <Delete02Icon className="h-3.5 w-3.5" />
                        </Button>
                      </div>
                    </div>

                    {q?.question && (
                      <div className="text-xs text-muted-foreground line-clamp-1 mt-1">
                        {q.question}
                      </div>
                    )}
                  </CardHeader>

                  <CardContent className="p-4 pt-2">
                    <div className="rounded-lg bg-secondary/30 p-3 text-sm">
                      <RichMathText text={item.content} />
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
