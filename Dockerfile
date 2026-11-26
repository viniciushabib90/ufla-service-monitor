FROM python:3.14-slim

WORKDIR /app

COPY requirements.lock .

RUN pip install --no-cache-dir --only-binary=:all: --require-hashes -r requirements.lock

COPY app.py .

RUN useradd --uid 10001 --no-create-home appuser

USER 10001

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
