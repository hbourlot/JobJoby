# JobJoby – Roadmap

A job-tracking tool. I paste a job posting (or pull it from a public API), it extracts what the job asks for, stores it in PostgreSQL, and shows stats about demand and about my own applications.

**Stack:** Python, PostgreSQL, SQLAlchemy, pandas, FastAPI, Docker Compose. Web app later with React + TypeScript.

I tick the boxes as I go.

## Phase 1 – Foundation
- [x] Project structure: `backend/` (`app/`, `tests/`, `requirements.txt`, `Dockerfile`), plus `.gitignore` and `.env.example` at the root
- [x] `docker-compose.yml` with PostgreSQL (+ pgAdmin, optional)
- [x] SQLAlchemy models: `companies`, `jobs`, `skills`, `job_skills`, `languages`, `job_languages`, `applications`
- [x] Script that creates the tables and inserts one test job
- [x] README with how to run it

## Phase 2 – Extraction
- [ ] Skill list (Python, SQL, Docker, React, ...) kept in a file, not hard-coded
- [ ] Function that reads a posting and returns: skills, level (intern / junior / senior), languages, "degree required", "equivalent experience accepted"
- [ ] Simple rules and regex first. No AI needed.
- [ ] Unit tests with 5–10 real posting texts (no personal data)

## Phase 3 – API (FastAPI)
- [ ] `POST /jobs` (paste the text, it extracts and saves)
- [ ] `GET /jobs` with filters (`?skill=docker&level=junior`)
- [ ] `POST /applications` and `PATCH /applications/{id}` (applied, interview, rejected, no reply)
- [ ] `GET /stats/skills` (most requested skills)

## Phase 4 – Analysis (pandas)
- [ ] Most requested skills, by level
- [ ] % of jobs that require a degree vs accept equivalent experience
- [ ] Applications per week and response rate
- [ ] Export to CSV (a script in `backend/scripts/`)

## Phase 5 – Job alerts by email
- [ ] Turn on job alerts on LinkedIn (and other sites) for the searches in my `Work` note
- [ ] Read the mailbox over IMAP (Gmail needs an app password; keep it in `.env`, never commit it)
- [ ] Only read emails from the alert senders (filter by sender and subject)
- [ ] Parse each email: job title, company, location, link
- [ ] Save new jobs to the database and skip duplicates (same rule as Phase 6). `raw_text` stays empty until I paste the full text
- [ ] Open the link and paste the full text into `POST /jobs` for the skill extraction (Phase 2)
- [ ] Run it on a schedule (cron), from a script in `backend/scripts/`

## Phase 6 – Data from public APIs
- [ ] Pull jobs from a free public API (e.g. Remotive, Arbeitnow; check which cover Portugal)
- [ ] Avoid duplicates: same link, or same company + title (the same job can come with different links from email and from an API)
- [ ] A scheduled job (cron) that runs daily, from a script in `backend/scripts/`

## Phase 7 – Polish for the portfolio
- [ ] Charts (matplotlib) or a simple page
- [ ] Tests for the API
- [ ] Clear README with screenshots and an architecture diagram
- [ ] Add the project to the portfolio and CV

## Phase 8 – Web app (React + TypeScript)
- [ ] `frontend/` folder with Vite + React + TypeScript, separate from the API
- [ ] Enable CORS in FastAPI for the frontend origin
- [ ] Typed API client (types that match the API responses)
- [ ] Jobs page: table with filters (skill, level, company, status)
- [ ] Add-job form: I paste the posting text and see the extracted skills before saving
- [ ] Applications board: columns for applied / interview / rejected / no reply
- [ ] Stats page: charts for most requested skills and degree requirements (e.g. Recharts)
- [ ] Add the frontend to `docker-compose.yml`
- [ ] If it goes online: add login first. It holds personal application data.

## Rules
- No scraping of LinkedIn or other sites that forbid it. Use pasted text, email alerts, or public APIs.
- Test data must not contain personal information.
