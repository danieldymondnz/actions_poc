# Dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY api.py .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
