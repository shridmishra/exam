"use client";

import React from "react";
import {
  StarIcon,
  Clock01Icon,
  PencilEdit01Icon,
  ChevronDownIcon,
} from "@/components/ui/icons";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { cn } from "@/lib/utils";
import { SolutionViewer } from "./solution-viewer";
import { RichMathText } from "@/components/common/math-renderer";
import { StructuredQuestion } from "@/components/common/structured-question";
import { Question } from "@/types";

interface QuestionCardProps {
  question: Question;
  isOpen: boolean;
  onToggleOpen: () => void;
  isCompleted: boolean;
  onToggleComplete: () => void;
  isStarred: boolean;
  onToggleStar: () => void;
  isLater: boolean;
  onToggleLater: () => void;
  personalNote?: string;
  onOpenNotesEditor: () => void;
}

export const QuestionCard = React.memo(
  function QuestionCard({
    question,
    isOpen,
    onToggleOpen,
    isCompleted,
    onToggleComplete,
    isStarred,
    onToggleStar,
    isLater,
    onToggleLater,
    personalNote,
    onOpenNotesEditor,
  }: QuestionCardProps) {
    const getYearBadgeVariant = (year: string) => {
      switch (year) {
        case "2025":
          return "year2025";
        case "2024":
          return "year2024";
        case "2023":
          return "year2023";
        case "2022":
          return "year2022";
        case "2019":
          return "year2019";
        default:
          return "secondary";
      }
    };

    const getRepeatBadgeVariant = (rep: string) => {
      switch (rep) {
        case "5x":
          return "repeat5x";
        case "4x":
          return "repeat4x";
        case "3x":
          return "repeat3x";
        case "2x":
          return "repeat2x";
        default:
          return "subtle";
      }
    };

    return (
      <div
        className={`group rounded-xl transition-all duration-200 ${
          isOpen
            ? "bg-transparent shadow-none"
            : "bg-card shadow-xs hover:shadow-sm card-content-visibility"
        }`}
      >
      {/* Header Row */}
      <div
        className="flex cursor-pointer flex-col gap-2 p-3 sm:p-4 select-none"
        onClick={onToggleOpen}
        role="button"
        tabIndex={0}
        aria-expanded={isOpen}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            onToggleOpen();
          }
        }}
      >
        <div className="flex items-start justify-between gap-1.5 sm:gap-3">
          {/* Left Metadata Cluster */}
          <div className="flex min-w-0 flex-1 flex-wrap items-center gap-1 sm:gap-1.5">
            {/* Mark Completed Checkbox */}
            <div
              className="flex items-center shrink-0 mr-0.5 sm:mr-1"
              onClick={(e) => e.stopPropagation()}
            >
              <Checkbox
                checked={isCompleted}
                onCheckedChange={onToggleComplete}
                variant="success"
                title={isCompleted ? "Mark Incomplete" : "Mark as Completed"}
                aria-label={isCompleted ? "Mark Incomplete" : "Mark as Completed"}
              />
            </div>

            <Badge
              variant={getYearBadgeVariant(question.year)}
              className="text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5"
              title={`${question.year} Examination Paper`}
            >
              {question.year}
            </Badge>

            <Badge
              variant="subtle"
              className="text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5"
              title={question.unit_name ? `Unit ${question.unit}: ${question.unit_name}` : `Unit ${question.unit}`}
            >
              Unit {question.unit}
            </Badge>

            <Badge
              variant="subtle"
              className="text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5"
              title={`Format: ${question.type}`}
            >
              {question.type}
            </Badge>

            <Badge
              variant="subtle"
              className="text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5"
              title={`Weightage: ${question.marks}M`}
            >
              {question.marks}M
            </Badge>

            {question.repeat_multiplier && question.repeat_multiplier !== "1x" && (
              <Badge
                variant={getRepeatBadgeVariant(question.repeat_multiplier)}
                className="text-[11px] sm:text-xs px-1.5 sm:px-2 py-0.5 font-bold"
                title={
                  question.rep_frequency
                    ? `Repeated across: ${question.rep_frequency.replace(/\s*\([^)]*\)/g, "").trim()}`
                    : `${question.repeat_multiplier} Repeated`
                }
              >
                {question.repeat_multiplier}
              </Badge>
            )}
          </div>

          {/* Right Action Controls */}
          <div
            className="flex shrink-0 items-center gap-1.5 sm:gap-2 mt-0.5"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Quick Actions Island (Star, Later, Note) */}
            <div
              className="action-island"
              role="group"
              aria-label="Question quick actions"
            >
              {/* Star */}
              <Button
                type="button"
                variant="ghost"
                size="icon"
                onClick={onToggleStar}
                className={cn(
                  "action-island-btn",
                  isStarred && "is-active-star"
                )}
                title={isStarred ? "Remove Star" : "Star Question"}
                aria-label="Star question"
              >
                <StarIcon
                  className={cn(
                    "h-3.5 w-3.5",
                    isStarred && "fill-current"
                  )}
                />
              </Button>

              {/* Later */}
              <Button
                type="button"
                variant="ghost"
                size="icon"
                onClick={onToggleLater}
                className={cn(
                  "action-island-btn",
                  isLater && "is-active-later"
                )}
                title={isLater ? "Remove from Later" : "Save for Later"}
                aria-label="Save for later"
              >
                <Clock01Icon className="h-3.5 w-3.5" />
              </Button>

              {/* Note Editor */}
              <Button
                type="button"
                variant="ghost"
                size="icon"
                onClick={onOpenNotesEditor}
                className={cn(
                  "action-island-btn",
                  personalNote && "is-active-note"
                )}
                title={personalNote ? "Edit Personal Note (Saved)" : "Add Personal Note"}
                aria-label="Personal note"
              >
                <PencilEdit01Icon className="h-3.5 w-3.5" />
              </Button>
            </div>
          </div>
        </div>

        {/* Structured Verbatim PYQ Question */}
        <div className="mt-1">
          <StructuredQuestion
            content={question.question}
            qNo={question.q_no}
            isCompleted={isCompleted}
          />
        </div>

        {/* View / Hide Answer Affordance Button */}
        <div className="mt-2.5 flex items-center">
          <span className="font-heading inline-flex items-center gap-1.5 rounded-md px-2.5 py-1 text-xs font-medium text-muted-foreground bg-secondary/50 group-hover:bg-secondary group-hover:text-foreground transition-all duration-150 select-none">
            <span>{isOpen ? "Hide Answer" : "View Answer"}</span>
            <ChevronDownIcon
              className={cn(
                "h-3.5 w-3.5 transition-transform duration-200",
                isOpen && "rotate-180"
              )}
            />
          </span>
        </div>
      </div>

      {/* Expandable Solution & Notes Container */}
      {isOpen && (
        <div className="px-4 py-4 sm:px-6">
          {/* User's Personal Note Callout (if present) */}
          {personalNote && (
            <div className="mb-4 rounded-xl bg-secondary/40 p-4">
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs font-bold uppercase tracking-wider text-muted-foreground flex items-center gap-1.5">
                  <PencilEdit01Icon className="h-3.5 w-3.5" />
                  My Personal Note
                </span>
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={onOpenNotesEditor}
                  className="h-6 text-[11px] text-muted-foreground hover:text-foreground"
                >
                  Edit Note
                </Button>
              </div>
              <div className="text-sm">
                <RichMathText text={personalNote} />
              </div>
            </div>
          )}

          {/* Formatted Solution View */}
          <div className="space-y-3">
            <SolutionViewer html={question.formatted_solution || question.solution} />
          </div>
        </div>
      )}
    </div>
  );
},
(prev, next) => {
  return (
    prev.isOpen === next.isOpen &&
    prev.isCompleted === next.isCompleted &&
    prev.isStarred === next.isStarred &&
    prev.isLater === next.isLater &&
    prev.personalNote === next.personalNote &&
    prev.question === next.question
  );
});
