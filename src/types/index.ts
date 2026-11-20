export interface Question {
  id: string;
  year: string;
  unit: number;
  unit_name: string;
  q_no: string;
  marks: number;
  type: string;
  co: string;
  bl: string;
  pi: string;
  topic: string;
  repeated: boolean;
  rep_frequency: string;
  repeat_multiplier: string;
  cluster_id: string | null;
  question: string;
  solution: string;
  formatted_solution?: string;
}

export interface TopicCluster {
  id: string;
  unit: number;
  unit_name: string;
  title: string;
  type: string;
  co: string;
  questions: Array<{
    id: string;
    year: string;
    q_no: string;
    marks: number;
    type: string;
    question: string;
  }>;
  years: string[];
  total_marks: number;
  rep_frequency: string;
  is_repeated: boolean;
  master_solution: string;
  canonical_question?: string;
}

export interface FormulaParam {
  sym: string;
  name: string;
  unit: string;
}

export interface MasterFormula {
  id: string;
  unit: number;
  title: string;
  frequency: string;
  freq_badge: string;
  latex_main: string;
  latex_sub: string;
  latex_raw: string;
  params: FormulaParam[];
  notes: string;
}

export interface ExamItem {
  id: number;
  date: string;
  isoDate: string;
  day: string;
  order: number;
  code: string;
  subject: string;
  shortTag: string;
  tag: string;
  isOld: boolean;
  gap: string;
  completed: boolean;
  notes?: string;
  link?: string | null;
}

export interface SubjectOption {
  id: string;
  path: string;
  name: string;
  short_name: string;
  code: string;
  status: "ready" | "planned" | string;
  question_count?: number;
  canonical_count?: number;
  formula_count?: number;
  is_default?: boolean;
}

export interface SubjectMeta {
  id: string;
  name: string;
  short_name: string;
  code: string;
  alt_codes: string[];
  branch: string;
  semester: string;
  academic_year: string;
  description: string;
  storage_prefix: string;
  unit_titles: Record<string, string>;
  units: Array<{
    num: number;
    title: string;
    short_title: string;
    co: string;
  }>;
  exam_years: number[];
}

export interface ChecklistFilters {
  year: string;      // 'all' | '2025' | '2024' | '2023' | '2022'
  unit: string;      // 'all' | '1' | '2' | '3' | '4' | '5'
  repeated: string;  // 'all' | 'repeated' | '4x' | '3x' | '2x'
  type: string;      // 'all' | 'Theory' | 'Numerical' | 'Derivation'
  marks: string;     // 'all' | '2' | '3' | '7'
  status: string;    // 'all' | 'incomplete' | 'completed' | 'starred' | 'later'
  search: string;
}

export interface UserPersonalNote {
  questionId: string;
  note: string;
  updatedAt: string;
}
