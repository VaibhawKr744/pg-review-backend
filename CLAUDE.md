# PG Review Platform — Backend

## What this is
A Trustpilot-style review aggregator for PGs/rented properties, starting 
with Gurgaon/Delhi NCR. Users search a PG and see aggregated review data, 
with a focus on whether the owner returns security deposits — plus an 
AI-generated summary verdict (later phase).

## Why I'm building this
Primarily a FastAPI learning project. Prioritize idiomatic, well-understood 
patterns over fast hacks — I want to actually learn auth, CRUD, relationships, 
and core FastAPI concepts properly, not just get something working.

## Stack
- Backend: FastAPI (Python), Pydantic, SQLAlchemy + Alembic
- DB: PostgreSQL
- Auth: JWT (OAuth2PasswordBearer + python-jose, passlib/bcrypt for hashing)
- Deployment: Railway or Render (planned, not yet set up)

## Frontend (separate repo)
Frontend lives in a sibling repo, `pg-review-frontend` — Vite + React + 
TypeScript, not Next.js. It calls this API over REST from 
`http://localhost:5173` in dev (already set as the allowed CORS origin).
This repo only cares about the API contract, not frontend implementation.

## Phase 1 (current focus — keep this simple)
- [x] Project scaffold (FastAPI, venv, dependencies installed)
- [ ] SQLAlchemy DB connection + Base model setup
- [ ] DB schema + models (PG, Review, User — basic relationships)
- [ ] Auth: signup/login/JWT, protected routes
- [ ] PG listing CRUD (manually entered data is fine for now — no scraping yet)
- [ ] Review submission (manual user-submitted reviews only)
- [ ] Basic search/filter on listings
- [ ] CORS confirmed working with frontend

## Phase 2 (later — do not build yet)
- Data ingestion scripts: Reddit (praw) + Google Places API, feeding an LLM 
  classifier for deposit-status extraction
- AI-generated deposit verdict summaries
- Any scraping/automation

## Conventions
- (add as you go — e.g. naming patterns, error handling style, exception 
  handling approach, etc.)