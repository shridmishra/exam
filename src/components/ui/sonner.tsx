"use client";

import { useTheme } from "next-themes";
import { Toaster as Sonner, toast } from "sonner";

type ToasterProps = React.ComponentProps<typeof Sonner>;

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme();

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      position="top-right"
      visibleToasts={1}
      duration={2600}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast font-sans text-xs sm:text-sm border-0 shadow-2xl rounded-2xl backdrop-blur-xl",
          description: "group-[.toast]:text-muted-foreground text-xs",
          actionButton:
            "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground text-xs font-semibold rounded-lg px-2.5 py-1 shadow-none border-0",
          cancelButton:
            "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground text-xs font-medium rounded-lg px-2.5 py-1 shadow-none border-0",
        },
      }}
      {...props}
    />
  );
};

export { Toaster, toast };
