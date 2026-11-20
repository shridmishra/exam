"use client";

import React, { useEffect, useState } from "react";
import { ArrowUp01Icon } from "@/components/ui/icons";
import { Button } from "@/components/ui/button";

export function BackToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setVisible(window.scrollY > 300);
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  if (!visible) return null;

  return (
    <Button
      variant="default"
      size="icon"
      onClick={scrollToTop}
      className="fixed bottom-[calc(72px+env(safe-area-inset-bottom,0px))] md:bottom-8 right-4 sm:right-8 z-50 h-10 w-10 sm:h-11 sm:w-11 rounded-full shadow-lg transition-all hover:scale-105"
      aria-label="Back to top"
      title="Back to top"
    >
      <ArrowUp01Icon size={20} className="h-5 w-5" />
    </Button>
  );
}
