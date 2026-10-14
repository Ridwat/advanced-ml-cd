# Continuous Delivery Practice: Sentiment API

**Adetola Ridwat Odulaja** · Academic API & delivery project

A FastAPI application demonstrating input validation, automated tests, containerization, and a CI workflow.

**Focus:** API behavior · Automated checks · Delivery workflow

## What is implemented

- Status and health endpoints.
- A sentiment endpoint accepting text.
- Validation for empty text and text longer than 1,000 characters.
- Positive, negative, or neutral classification using keyword rules.
- Pytest tests, a Dockerfile, and a GitHub Actions workflow.

The API title references ONNX, but the current implementation does not load an ONNX model. The committed `app/model.onnx` is empty. This project demonstrates delivery mechanics around a rule-based service.

## Why it matters

Reliable automation requires explicit input behavior and repeatable checks. This exercise shows how those concerns can be integrated with a service and its build workflow.

## Run locally

From the repository root:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API schema.

```bash
PYTHONPATH=. pytest tests/
docker build -t advanced-ml-cd .
docker run -p 8000:8000 advanced-ml-cd
```

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Status message |
| GET | `/health` | Health response |
| POST | `/predict` | Keyword-based sentiment |

Example request:

```json
{"text": "I love this product"}
```

## Continuous integration

[The workflow](.github/workflows/ci.yml) runs tests, builds an image, starts a container, and requests its health endpoint after pushes to main. A configured workflow does not establish that the latest run passed; this documentation review did not execute tests or a container.

## Limitations & next steps

Substring matching does not reliably understand negation or context. `processing_time` currently records a timestamp, not elapsed processing duration. Blue-green and canary deployment are not implemented. Replace the rules with a validated model before describing this as ML inference.

[Explore my portfolio](https://github.com/Ridwat/Ethical-AI-Analysis/blob/main/PORTFOLIO.md)
