"use client";

import React, { useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Bug02Icon,
  Bulb01Icon,
  PencilEdit01Icon,
  Send01Icon,
} from "@/components/ui/icons";
import { toast } from "@/components/ui/sonner";
import { cn } from "@/lib/utils";

export interface FeedbackDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  currentSubject?: string;
  currentSubjectCode?: string;
  activeTab?: string;
}

type FeedbackType = "bug" | "suggestion" | "content";

const CATEGORIES: {
  id: FeedbackType;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
}[] = [
  { id: "suggestion", label: "Suggestion", icon: Bulb01Icon },
  { id: "bug", label: "Bug", icon: Bug02Icon },
  { id: "content", label: "Correction", icon: PencilEdit01Icon },
];

export function FeedbackDialog({
  open,
  onOpenChange,
  currentSubject = "Geotechnical Engineering - II",
  currentSubjectCode,
  activeTab = "checklist",
}: FeedbackDialogProps) {
  const [type, setType] = useState<FeedbackType>("suggestion");
  const [title, setTitle] = useState("");
  const [message, setMessage] = useState("");
  const [contact, setContact] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const trimmedMsg = message.trim();
    if (!trimmedMsg) {
      toast.error("Please enter your message.");
      return;
    }

    setIsSubmitting(true);

    const payload = {
      type,
      title: title.trim(),
      message: trimmedMsg,
      contact: contact.trim(),
      context: {
        subject: currentSubject,
        subjectCode: currentSubjectCode,
        activeTab,
        url: typeof window !== "undefined" ? window.location.href : "",
        userAgent: typeof navigator !== "undefined" ? navigator.userAgent : "",
        screen:
          typeof window !== "undefined"
            ? `${window.innerWidth}x${window.innerHeight}`
            : undefined,
      },
    };

    try {
      const response = await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Failed to submit");

      toast.success("Feedback submitted! Thank you.");
      setTitle("");
      setMessage("");
      setContact("");
      setType("suggestion");
      onOpenChange(false);
    } catch (err: any) {
      console.error("Feedback submit error:", err);
      try {
        const offlineKey = "exam_pending_feedback";
        const pending = JSON.parse(localStorage.getItem(offlineKey) || "[]");
        pending.push({ ...payload, queuedAt: new Date().toISOString() });
        localStorage.setItem(offlineKey, JSON.stringify(pending));
        toast.info("Saved locally (offline mode).");
        onOpenChange(false);
      } catch {
        toast.error("Failed to send feedback.");
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-[calc(100vw-2rem)] sm:max-w-md p-5 rounded-2xl border-0 bg-card shadow-2xl">
        <DialogHeader className="space-y-1 text-left">
          <DialogTitle className="font-heading text-base font-semibold text-foreground flex items-center gap-2">
            Feedback & Suggestions
          </DialogTitle>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-3 mt-1">
          {/* Category Selector (Pure Background Separation, Zero Borders) */}
          <div className="grid grid-cols-3 gap-1.5 p-1 rounded-xl bg-secondary/60">
            {CATEGORIES.map((cat) => {
              const Icon = cat.icon;
              const isSelected = type === cat.id;
              return (
                <Button
                  key={cat.id}
                  type="button"
                  variant="ghost"
                  size="sm"
                  onClick={() => setType(cat.id)}
                  className={cn(
                    "flex items-center justify-center gap-1.5 h-8 rounded-lg text-xs font-medium transition-all border-0",
                    isSelected
                      ? "bg-card text-foreground font-semibold shadow-2xs"
                      : "text-muted-foreground hover:text-foreground hover:bg-secondary/40"
                  )}
                >
                  <Icon className="h-3.5 w-3.5 shrink-0" />
                  <span>{cat.label}</span>
                </Button>
              );
            })}
          </div>

          {/* Short Title / Summary */}
          <Input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Topic (optional)"
            maxLength={120}
            className="h-9 rounded-xl bg-secondary/50 focus-visible:bg-secondary/80 text-sm border-0 focus-visible:ring-0"
          />

          {/* Detailed Message */}
          <Textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Describe what happened or your suggestion..."
            rows={4}
            maxLength={4000}
            required
            className="min-h-[100px] rounded-xl bg-secondary/50 focus-visible:bg-secondary/80 text-sm leading-relaxed border-0 focus-visible:ring-0"
          />

          {/* Contact (Optional) */}
          <Input
            value={contact}
            onChange={(e) => setContact(e.target.value)}
            placeholder="Your name or contact (optional)"
            maxLength={80}
            className="h-9 rounded-xl bg-secondary/50 focus-visible:bg-secondary/80 text-sm border-0 focus-visible:ring-0"
          />

          {/* Bottom Bar: Minimal Context Hint & Actions */}
          <div className="flex items-center justify-between pt-1 gap-2">
            <span className="text-[11px] text-muted-foreground/60 truncate max-w-[180px] sm:max-w-xs">
              {currentSubject} • {activeTab}
            </span>

            <div className="flex items-center gap-1.5 shrink-0">
              <Button
                type="button"
                variant="ghost"
                size="sm"
                onClick={() => onOpenChange(false)}
                disabled={isSubmitting}
                className="h-8 px-3 rounded-lg text-xs text-muted-foreground hover:text-foreground bg-secondary/40 hover:bg-secondary/70 border-0"
              >
                Cancel
              </Button>
              <Button
                type="submit"
                variant="default"
                size="sm"
                disabled={isSubmitting || !message.trim()}
                className="h-8 px-3.5 rounded-lg gap-1.5 text-xs font-semibold border-0"
              >
                <Send01Icon className="h-3 w-3" />
                <span>{isSubmitting ? "Sending..." : "Submit"}</span>
              </Button>
            </div>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
