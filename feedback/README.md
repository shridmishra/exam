# User Feedback & Suggestions

This directory stores user-submitted bug reports, PYQ typos, formula corrections, and feature suggestions submitted via the web platform.

## Architecture & Storage Design

1. **Conflict-Free Commits**:
   - Each submission is stored in an independent JSON file named:
     `YYYY-MM-DD_fb_<timestamp>_<unique-id>.json`
   - Storing each entry as an isolated file guarantees **zero git merge conflicts** when multiple users submit suggestions simultaneously from different locations.

2. **GitHub API Integration**:
   - In production (e.g. Vercel), the `/api/feedback` route uses the GitHub REST API (via `GITHUB_TOKEN`) to commit new feedback directly into this directory on the `main` branch.
   - The developer can review submissions directly in the GitHub repo, receive commit alerts, or pull them via `git pull`.

3. **Local Development Fallback**:
   - When running locally (`npm run dev`), submissions are saved directly to this directory on disk and appended to `all_feedbacks.json`.

4. **Viewing Feedback**:
   - To view all feedback in your terminal, run:
     ```bash
     npm run feedback
     # or
     node scripts/view-feedback.js
     ```

## Environment Variables
To enable direct GitHub commits from production, configure these variables in Vercel or `.env.local`:
- `GITHUB_TOKEN`: GitHub Personal Access Token (with `contents:write` permission for this repo).
- `GITHUB_REPO`: `shridmishra/exam` (defaults to current repo).
- `GITHUB_BRANCH`: `main` (defaults to `main`).
