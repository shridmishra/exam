import React from "react";

export function SeoStructuredData() {
  const siteUrl =
    process.env.NEXT_PUBLIC_SITE_URL ||
    (process.env.VERCEL_PROJECT_PRODUCTION_URL
      ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
      : process.env.VERCEL_URL
      ? `https://${process.env.VERCEL_URL}`
      : "https://exam.shridmishra.com");

  const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: "Exam Intelligence & PYQ Analysis Platform",
    url: siteUrl,
    description:
      "Offline-first previous year question intelligence, repeat frequency trends, formula cheat-sheets, and examination timetable for university civil engineering exams.",
    inLanguage: "en-US",
    educationalUse: "Exam Preparation & Engineering Study",
    audience: {
      "@type": "EducationalAudience",
      educationalRole: "student",
    },
  };

  const coursesSchema = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    name: "University Civil Engineering Exam Courses",
    itemListElement: [
      {
        "@type": "Course",
        position: 1,
        name: "Geotechnical Engineering - II",
        courseCode: "CE 41007",
        description:
          "Comprehensive PYQ checklist, Terzaghi and Meyerhof bearing capacity, earth pressure theories, pile foundation design, and soil investigation.",
        provider: {
          "@type": "Organization",
          name: "Exam Intelligence Platform",
          url: siteUrl,
        },
      },
      {
        "@type": "Course",
        position: 2,
        name: "Design of Advanced Reinforced Concrete Structures (RCC)",
        courseCode: "CE 41001",
        description:
          "Limit state design of RCC structures, retaining walls, flat slabs, deep beams, water tanks, and yield line theory.",
        provider: {
          "@type": "Organization",
          name: "Exam Intelligence Platform",
          url: siteUrl,
        },
      },
      {
        "@type": "Course",
        position: 3,
        name: "Design of Hydraulic Structures",
        courseCode: "CE 41006",
        description:
          "Design of gravity dams, spillways, diversion headworks, Khosla's theory, canal falls, and cross-drainage works.",
        provider: {
          "@type": "Organization",
          name: "Exam Intelligence Platform",
          url: siteUrl,
        },
      },
    ],
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: [
      {
        "@type": "Question",
        name: "What are the most repeated questions in Geotechnical Engineering - II?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "High-probability repeated topics include Terzaghi's General Bearing Capacity Equation and its assumptions, Rankine vs. Coulomb earth pressure theories, settlement computation for shallow footings, negative skin friction in piles, and modes of shear failure (General, Local, and Punching).",
        },
      },
      {
        "@type": "Question",
        name: "How does the PYQ Intelligence system prioritize questions?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Questions are categorized by recurring frequency tiers: Tier 1 (4x Guaranteed, appeared in 2025, 2024, 2023, 2022), Tier 2 (3x High Probability), and Tier 3 (2x Medium Probability), organized by syllabus Unit and canonical concept clusters.",
        },
      },
      {
        "@type": "Question",
        name: "Does the platform work offline?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Yes, the platform is offline-first. Study checklists, completed question states, and personal notes are persisted directly in local browser storage.",
        },
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(coursesSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />
    </>
  );
}
