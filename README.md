# Flyrank Backend

This repository contains two backend services:
- `NodeJS/` — an Express-based Task API with Swagger UI documentation
- `fastapi/` — a FastAPI-based Task API served by Uvicorn

## Node.js Service

### What was added
- `NodeJS/index.js` implements a simple task REST API
- Express is used for routing and JSON body parsing
- Swagger UI is served at `/docs` using `swagger-ui-express`
- The service listens on port `3000`

### Run Node.js

1. Open a terminal and go to the NodeJS folder:
   ```powershell
   cd NodeJS
   ```
2. Install dependencies if not already installed:
   ```powershell
   npm install
   ```
3. Start the service:
   ```powershell
   npm run dev
   ```

### Access Node.js API
- Base URL: `http://localhost:3000`
- Swagger docs: `http://localhost:3000/docs`
- Home: `http://localhost:3000/`
- Health: `http://localhost:3000/health`
- Tasks: `http://localhost:3000/tasks`

### Example `curl` commands
```powershell
curl http://localhost:3000/
curl http://localhost:3000/health
curl http://localhost:3000/tasks
curl http://localhost:3000/tasks/1
curl -X POST http://localhost:3000/tasks -H "Content-Type: application/json" -d "{\"title\": \"New task\"}"
curl -X PUT http://localhost:3000/tasks/1 -H "Content-Type: application/json" -d "{\"done\": true}"
curl -X DELETE http://localhost:3000/tasks/1
```

## FastAPI Service

### What was added
- `fastapi/main.py` implements a task REST API with FastAPI
- Uses `uvicorn` to run the app
- The service listens on port `8000`
- FastAPI automatically provides OpenAPI docs at `/docs`

### Run FastAPI

1. Open a terminal and go to the fastapi folder:
   ```powershell
   cd fastapi
   ```
2. Activate the Python virtual environment (Windows PowerShell):
   ```powershell
   .\env\Scripts\Activate.ps1
   ```
   If you use CMD, run:
   ```cmd
   .\env\Scripts\activate.bat
   ```
3. Install requirements if needed:
   ```powershell
   pip install -r requirements.txt
   ```
4. Start the service:
   ```powershell
   python main.py
   ```

### Access FastAPI
- Base URL: `http://localhost:8000`
- OpenAPI docs: `http://localhost:8000/docs`
- Home: `http://localhost:8000/`
- Health: `http://localhost:8000/health`
- Tasks: `http://localhost:8000/tasks`

### Example `curl` commands
```powershell
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/tasks
curl http://localhost:8000/tasks/1
curl -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"title\": \"New task\"}"
curl -X PUT http://localhost:8000/tasks/1 -H "Content-Type: application/json" -d "{\"done\": true}"
curl -X DELETE http://localhost:8000/tasks/1
```

## Notes
- The Node.js service uses port `3000`.
- The FastAPI service uses port `8000`.
- Both services use in-memory task lists, so data resets when the server restarts.
