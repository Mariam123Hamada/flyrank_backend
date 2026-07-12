# flyrank_backend

A simple FastAPI backend project for the flyrank application.

## Features

- Home endpoint returning a welcome message
- About endpoint returning basic profile information
- Basic pytest coverage for the API endpoints

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/about

## Run tests

```bash
python -m pytest -q
```

## Project structure

- main.py - FastAPI app and route definitions
- test/test_app.py - API tests
- requirements.txt - Python dependencies