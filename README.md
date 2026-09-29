# Secure Documents Management System (SI-PALMS)

A secure, role-based police & legal document management system featuring cryptographic document integrity verification, EVM blockchain anchoring, tamper detection, and audit logging.

---

## 🚀 Quick Deploy to Render

Deploy this repository with **1-click Blueprint** on [Render.com](https://render.com):

1. Push this repository to your GitHub account.
2. Go to [Render Dashboard](https://dashboard.render.com/) $\rightarrow$ Click **New +** $\rightarrow$ Select **Blueprint**.
3. Select your repository.
4. Fill in the MySQL connection details (`MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, etc.) from your cloud database provider (e.g. [TiDB Cloud](https://tidbcloud.com/) or [Aiven](https://aiven.io/)).
5. Click **Apply** to deploy!

---

## 🛠️ Tech Stack

- **Frontend**: React 19, TypeScript, Vite, Tailwind CSS 4, Lucide Icons
- **Backend**: Python 3, FastAPI, Uvicorn, PyMySQL, PyJWT, Eth-Account (EVM Blockchain simulation)
- **Database**: MySQL 8.0 / TiDB Cloud / Aiven MySQL
- **Deployment**: Render Blueprint (`render.yaml`)

---

## 🔑 Pre-Seeded Default Accounts

| Role | Officer / User ID | Password | Name |
| :--- | :--- | :--- | :--- |
| **Police Officer** | `PO-1042` | `police1042` | Inspector Rajesh Kumar |
| **Police Officer** | `PO-2055` | `police2055` | Officer Suresh Verma |
| **Lead Investigator** | `IN-8805` | `invest8805` | Senior Det. Anita Sharma |
| **Forensic Specialist** | `FO-4091` | `forensic4091` | Dr. Vikramaditya Roy |
| **Public Prosecutor (Lawyer)** | `LW-9120` | `lawyer9120` | Advocate Meera Deshmukh |

---

## 💻 Local Development

### 1. Prerequisites
- Node.js 20+
- Python 3.10+
- MySQL Server (running locally on port 3306)

### 2. Backend Setup
```bash
# Navigate to project root
cd Secure-Documents-Management-System

# Install Python requirements
pip install -r server/requirements.txt

# Configure environment variables
cp server/.env.example server/.env
# Edit server/.env with your MySQL credentials

# Run FastAPI backend
python server/main.py
```

### 3. Frontend Setup
```bash
# Install Node dependencies
npm install

# Start Vite development server
npm run dev
```

### 4. Build for Production
```bash
# Builds React frontend to dist/
npm run build

# Start production server
uvicorn server.main:app --host 0.0.0.0 --port 5000
```
