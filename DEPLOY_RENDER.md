# Deploying to Render with Blueprint (render.yaml)

This guide walks you through deploying the **Secure Documents Management System** on [Render](https://render.com) using Infrastructure-as-Code via `render.yaml`.

---

## 1. Why Render Blueprints?

Render Blueprints allow you to configure and manage all your services, environment variables, health checks, and build settings directly from source code in the `render.yaml` file.

---

## 2. Prerequisites: Cloud MySQL Database

Render's native managed database is PostgreSQL. Because SI-PALMS is built on MySQL, you can connect a free cloud MySQL instance:

### Option A: TiDB Cloud Serverless (Recommended — Free 25GB)
1. Go to [tidbcloud.com](https://tidbcloud.com/) and create a free account.
2. Click **Create Cluster** and select **Serverless** (Free forever).
3. Under cluster settings, click **Connect**:
   - Choose connection method: **General / Python**.
   - Note down: `Host`, `Port` (4000), `User`, `Password`, and `Database` name (e.g. `test` or `sipalms_db`).
   - Note: Set `MYSQL_SSL_MODE=true`.

### Option B: Aiven for MySQL (Free Tier)
1. Go to [aiven.io](https://aiven.io/) and create a free MySQL instance.
2. Note down: `Host`, `Port`, `User`, `Password`, and `Database`.

---

## 3. Step-by-Step Deployment on Render

### Step 1: Push Repository to GitHub
Make sure all files including `render.yaml`, `server/main.py`, and `server/db.py` are pushed to your GitHub repository:
```bash
git add .
git commit -m "Configure Render Blueprint deployment"
git push origin main
```

### Step 2: Open Render Dashboard
1. Log in to [dashboard.render.com](https://dashboard.render.com/).
2. In the top-right corner, click **New +** and select **Blueprint**.

### Step 3: Connect Your GitHub Repository
1. Select your repository: `Secure-Documents-Management-System`.
2. Give your Blueprint a name (e.g. `secure-docs-app`).
3. Select your deployment branch (`main`).

### Step 4: Configure Environment Variables
Render will read `render.yaml` and prompt you for the un-synced variables:
- `MYSQL_HOST`: (e.g. `gateway01.us-east-1.prod.aws.tidbcloud.com`)
- `MYSQL_PORT`: `4000` (for TiDB) or `3306` (for standard MySQL)
- `MYSQL_USER`: Your cloud database username
- `MYSQL_PASSWORD`: Your cloud database password
- `MYSQL_DATABASE`: Your database name (e.g. `sipalms_db` or `test`)
- `MYSQL_SSL_MODE`: `true` (if using TiDB / Aiven / RDS) or `false`

### Step 5: Click "Apply"
Render will automatically:
1. Build the Vite React frontend into optimized static files (`dist/`).
2. Install Python backend dependencies.
3. Establish database connection, run initial schema migrations, and seed default user accounts.
4. Start the Uvicorn web server and verify `/api/health`.

---

## 4. Default Seeded Logins

Once deployed, access your URL (e.g. `https://secure-documents-system.onrender.com`) and login with:

- **Police Station Officer**: `PO-1042` / `police1042`
- **Commercial Crime Officer**: `PO-2055` / `police2055`
- **Lead Case Investigator**: `IN-8805` / `invest8805`
- **Chief Forensic Specialist**: `FO-4091` / `forensic4091`
- **Public Prosecutor (Lawyer)**: `LW-9120` / `lawyer9120`
