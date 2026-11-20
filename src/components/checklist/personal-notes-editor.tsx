"use client";

import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { RichMathText } from "@/components/common/math-renderer";
import { Question } from "@/types";
import {
  FloppyDiskIcon,
  Delete02Icon,
  ViewIcon,
  PencilEdit01Icon,
} from "@/components/ui/icons";
import { tabSpringTransition } from "@/lib/motion";

interface PersonalNotesEditorProps {
  question: Question | null;
  isOpen: boolean;
  onClose: () => void;
  onSave: (questionId: string, noteText: string) => void;
  initialNote?: string;
}

export const PersonalNotesEditor = React.memo(function PersonalNotesEditor({
  question,
  isOpen,
  onClose,
  onSave,
  initialNote = "",
}: PersonalNotesEditorProps) {
  const [note, setNote] = useState(initialNote);
  const [activeTab, setActiveTab] = useState<"edit" | "preview">("edit");

  useEffect(() => {
    setNote(initialNote);
  }, [initialNote, isOpen]);

  if (!question) return null;

  const handleSave = () => {
    onSave(question.id, note);
    onClose();
  };

  const handleClear = () => {
    setNote("");
  };

  return (
    <Dialog open={isOpen} onOpenChange={(open) => !open && onClose()}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2 text-base font-semibold">
            <span>Personal Note &bull; {question.q_no}</span>
            <span className="text-xs font-normal text-muted-foreground">
              ({question.year} &bull; Unit {question.unit})
            </span>
          </DialogTitle>
          <div className="text-xs text-muted-foreground line-clamp-2 mt-1">
            {question.question}
          </div>
        </DialogHeader>

        <Tabs
          value={activeTab}
          onValueChange={(val) => setActiveTab(val as "edit" | "preview")}
          className="mt-2"
        >
          <TabsList className="grid w-full grid-cols-2 relative p-1">
            <TabsTrigger
              value="edit"
              className="relative gap-1.5 text-xs data-[state=active]:bg-transparent data-[state=active]:shadow-none select-none"
            >
              {activeTab === "edit" && (
                <motion.div
                  layoutId="notes-editor-tab-pill"
                  className="absolute inset-0 rounded-md bg-background shadow-xs ring-1 ring-border/20"
                  transition={tabSpringTransition}
                />
              )}
              <span className="relative z-10 flex items-center gap-1.5">
                <PencilEdit01Icon className="h-3.5 w-3.5" />
                <span>Edit Markdown &amp; LaTeX</span>
              </span>
            </TabsTrigger>
            <TabsTrigger
              value="preview"
              className="relative gap-1.5 text-xs data-[state=active]:bg-transparent data-[state=active]:shadow-none select-none"
            >
              {activeTab === "preview" && (
                <motion.div
                  layoutId="notes-editor-tab-pill"
                  className="absolute inset-0 rounded-md bg-background shadow-xs ring-1 ring-border/20"
                  transition={tabSpringTransition}
                />
              )}
              <span className="relative z-10 flex items-center gap-1.5">
                <ViewIcon className="h-3.5 w-3.5" />
                <span>Preview</span>
              </span>
            </TabsTrigger>
          </TabsList>

          <TabsContent value="edit" className="mt-3">
            <Textarea
              placeholder="Write your custom notes, formulas ($...$ or $$...$$), bullet points, or memory tricks here..."
              value={note}
              onChange={(e) => setNote(e.target.value)}
              className="min-h-[220px] text-sm leading-relaxed"
            />
            <div className="mt-1.5 text-[11px] text-muted-foreground">
              Tip: Supports LaTeX math like $K_a = \tan^2(45^\circ - \phi/2)$ and $$display$$ equations.
            </div>
          </TabsContent>

          <TabsContent value="preview" className="mt-3">
            <div className="min-h-[220px] rounded-xl bg-secondary/40 p-4 text-sm">
              {note.trim() ? (
                <RichMathText text={note} />
              ) : (
                <span className="text-muted-foreground italic">
                  No note content yet. Switch to Edit to write your notes.
                </span>
              )}
            </div>
          </TabsContent>
        </Tabs>

        <DialogFooter className="flex items-center justify-between sm:justify-between">
          <Button
            type="button"
            variant="ghost"
            size="sm"
            onClick={handleClear}
            className="text-xs text-muted-foreground hover:text-destructive"
          >
            <Delete02Icon className="h-3.5 w-3.5 mr-1" />
            Clear
          </Button>

          <div className="flex items-center gap-2">
            <Button
              type="button"
              variant="secondary"
              size="sm"
              onClick={onClose}
              className="text-xs"
            >
              Cancel
            </Button>
            <Button
              type="button"
              size="sm"
              onClick={handleSave}
              className="text-xs gap-1.5"
            >
              <FloppyDiskIcon className="h-3.5 w-3.5" />
              Save Note
            </Button>
          </div>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
});
