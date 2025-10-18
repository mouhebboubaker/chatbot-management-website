# Valerie T2T Backend - Quick Start

## 1. Clone
```bash
git clone https://github.com/Metal-2000-Interns/valerie-t2t-backend.git
cd valerie-t2t-backend/backend
```

## 2. Install dependencies
```bash
npm install
```

## 3. Environment variables
Copy example file and edit values:
```bash
cp .env.example .env      # Linux / macOS / Git Bash
# PowerShell:
# Copy-Item .env.example .env
```
Fill `.env` with real secrets (DB URL, JWT secrets, mail creds).

## 4. Create PostgreSQL database
Inside psql (or use your GUI):
```sql
CREATE DATABASE chatbot_db;
```

## 5. Run migrations (create schema)
```bash
npx drizzle-kit migrate
```

## 6. (Optional) Seed test data
```bash
npx ts-node scripts/seed.ts
```

## 7. Start the server
```bash
npx nodemon          # auto‑reload dev mode
# or:
npx ts-node src/index.ts
```

---

### TL;DR
```bash
git clone https://github.com/Metal-2000-Interns/valerie-t2t-backend.git
cd valerie-t2t-backend/backend
npm install
cp .env.example .env
createdb chatbot_db            # or CREATE DATABASE chatbot_db;
npx drizzle-kit migrate
npx ts-node scripts/seed.ts    # (optional)
npx nodemon
```

 
