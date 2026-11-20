import type { Metadata } from "next";
import { Inter } from "next/font/google";
import localFont from "next/font/local";
import { ThemeProvider } from "@/components/theme-provider";
import { BackToTop } from "@/components/common/back-to-top";
import { Toaster } from "@/components/ui/sonner";
import { STORAGE_KEYS } from "@/lib/constants";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

const aeonik = localFont({
  src: [
    {
      path: "./_fonts/AeonikTRIAL-Light.otf",
      weight: "300",
      style: "normal",
    },
    {
      path: "./_fonts/AeonikTRIAL-LightItalic.otf",
      weight: "300",
      style: "italic",
    },
    {
      path: "./_fonts/AeonikTRIAL-Regular.otf",
      weight: "400",
      style: "normal",
    },
    {
      path: "./_fonts/AeonikTRIAL-RegularItalic.otf",
      weight: "400",
      style: "italic",
    },
    {
      path: "./_fonts/AeonikTRIAL-Regular.otf",
      weight: "500",
      style: "normal",
    },
    {
      path: "./_fonts/AeonikTRIAL-Bold.otf",
      weight: "600",
      style: "normal",
    },
    {
      path: "./_fonts/AeonikTRIAL-Bold.otf",
      weight: "700",
      style: "normal",
    },
    {
      path: "./_fonts/AeonikTRIAL-BoldItalic.otf",
      weight: "700",
      style: "italic",
    },
  ],
  variable: "--font-aeonik",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Exam Intelligence & PYQ Analysis Platform",
  description:
    "Offline-first previous year question intelligence, repeat trends, formula cheat-sheet, and examination timetable for Geotechnical Engineering - II.",
  icons: {
    icon: [
      { url: "/favicon.svg", type: "image/svg+xml" },
      { url: "/favicon.ico" },
    ],
    apple: [{ url: "/apple-touch-icon.png" }],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${inter.variable} ${aeonik.variable}`}
    >
      <body
        className={`${inter.variable} ${aeonik.variable} min-h-screen bg-background font-sans antialiased text-foreground`}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          storageKey={STORAGE_KEYS.THEME}
        >
          {children}
          <BackToTop />
          <Toaster position="top-right" richColors visibleToasts={1} closeButton />
        </ThemeProvider>
      </body>
    </html>
  );
}
