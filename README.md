# JobJoby

A tool I'm building to track job postings and my own applications.

## Why I built it

When I apply for jobs, I lose track of what each posting asked for and where I stand with each application. I also want real numbers on what the market asks for: which skills come up most, and how many junior roles accept equivalent experience instead of a degree.

So I paste a job posting (or pull it from a public API or my email job alerts), JobJoby extracts what the job asks for, stores it in PostgreSQL, and shows stats about demand and about my applications.

## Stack

- Python, SQLAlchemy, pandas
- PostgreSQL
- FastAPI
- Docker Compose
- Later: React + TypeScript for the web app

## How to run it

I need Docker and Python 3.

1. Copy the example env file and fill it in:
   ```
   cp .env.example .env
   ```
2. Put the database password in its own file. Docker reads it from there, and so does my code:
   ```
   mkdir .secrets
   echo "choose-a-password" > .secrets/postgres_password.txt
   ```
3. Start PostgreSQL:
   ```
   docker compose up -d
   ```
4. Install the Python packages:
   ```
   python -m venv myvenv
   source myvenv/bin/activate
   pip install -r requirements.txt
   ```
5. Create the tables and insert one test job:
   ```
   cd backend
   python -m scripts.create_table
   ```

`.env` and `.secrets/` are in `.gitignore`, so they never get committed.

## Status

Work in progress. I'm building it phase by phase. See [ROADMAP.md](ROADMAP.md) for the plan and what's done.
