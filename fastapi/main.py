

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def get_health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)







