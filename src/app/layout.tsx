import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import localFont from "next/font/local";
import { ThemeProvider } from "@/components/theme-provider";
import { BackToTop } from "@/components/common/back-to-top";
import { Toaster } from "@/components/ui/sonner";
import { SeoStructuredData } from "@/components/common/seo-structured-data";
import { STORAGE_KEYS } from "@/lib/constants";
import "katex/dist/katex.min.css";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const googleSans = localFont({
  src: [
    {
      path: "./_fonts/GoogleSans-Regular.woff2",
      weight: "400",
      style: "normal",
    },
    {
      path: "./_fonts/GoogleSans-Italic.woff2",
      weight: "400",
      style: "italic",
    },
    {
      path: "./_fonts/GoogleSans-Medium.woff2",
      weight: "500",
      style: "normal",
    },
    {
      path: "./_fonts/GoogleSans-MediumItalic.woff2",
      weight: "500",
      style: "italic",
    },
    {
      path: "./_fonts/GoogleSans-SemiBold.woff2",
      weight: "600",
      style: "normal",
    },
    {
      path: "./_fonts/GoogleSans-SemiBoldItalic.woff2",
      weight: "600",
      style: "italic",
    },
    {
      path: "./_fonts/GoogleSans-Bold.woff2",
      weight: "700",
      style: "normal",
    },
    {
      path: "./_fonts/GoogleSans-BoldItalic.woff2",
      weight: "700",
      style: "italic",
    },
  ],
  variable: "--font-google-sans",
  display: "swap",
});

const siteUrl =
  process.env.NEXT_PUBLIC_SITE_URL ||
  (process.env.VERCEL_PROJECT_PRODUCTION_URL
    ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
    : process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : "https://exam.shridmishra.com");

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fbfaf8" },
    { media: "(prefers-color-scheme: dark)", color: "#09090b" },
  ],
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  colorScheme: "light dark",
};

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "Exam Intelligence & PYQ Analysis Platform",
    template: "%s | Exam Intelligence Platform",
  },
  description:
    "Offline-first previous year question intelligence, repeat frequency trends, formula cheat-sheets, and examination timetables for university civil engineering exams.",
  applicationName: "Exam Intelligence Platform",
  authors: [{ name: "Shrid Mishra", url: "https://github.com/shridmishra" }],
  creator: "Shrid Mishra",
  publisher: "Exam Intelligence Platform",
  keywords: [
    "Exam Intelligence",
    "PYQ Analysis",
    "Previous Year Questions",
    "Civil Engineering",
    "Geotechnical Engineering",
    "Foundation Engineering",
    "RCC Design",
    "Hydraulic Structures",
    "Engineering Formulas",
    "Exam Timetable",
    "Solved Exam Papers",
    "Engineering Exam Prep",
    "Semester Exam Intelligence",
  ],
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "Exam Intelligence & PYQ Analysis Platform",
    description:
      "Offline-first previous year question intelligence, repeat frequency trends, formula cheat-sheets, and examination timetables for university civil engineering exams.",
    url: "/",
    siteName: "Exam Intelligence Platform",
    locale: "en_US",
    type: "website",
    images: [
      {
        url: "/favicon.svg",
        width: 512,
        height: 512,
        alt: "Exam Intelligence & PYQ Analysis Platform Logo",
      },
    ],
  },
  twitter: {
    card: "summary",
    title: "Exam Intelligence & PYQ Analysis Platform",
    description:
      "Offline-first previous year question intelligence, repeat frequency trends, formula cheat-sheets, and examination timetables for university civil engineering exams.",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  icons: {
    icon: [
      { url: "/favicon.svg", type: "image/svg+xml" },
      { url: "/favicon.ico" },
    ],
    apple: [{ url: "/apple-touch-icon.png" }],
  },
  category: "education",
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
      className={`${googleSans.variable} ${inter.variable}`}
    >
      <head>
        <SeoStructuredData />
      </head>
      <body
        className={`${googleSans.variable} ${inter.variable} min-h-screen bg-background font-sans antialiased text-foreground`}
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

