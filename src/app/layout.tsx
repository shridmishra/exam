import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { ThemeProvider } from "@/components/theme-provider";
import { BackToTop } from "@/components/common/back-to-top";
import { STORAGE_KEYS } from "@/lib/constants";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-sans",
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
    <html lang="en" suppressHydrationWarning className={inter.variable}>
      <body className={`${inter.variable} min-h-screen bg-background font-sans antialiased text-foreground`}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          storageKey={STORAGE_KEYS.THEME}
        >
          {children}
          <BackToTop />
        </ThemeProvider>
      </body>
    </html>
  );
}
