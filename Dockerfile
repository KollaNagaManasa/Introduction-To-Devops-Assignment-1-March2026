FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

WORKDIR /app

# Install build deps (kept small) and runtime deps
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy application
COPY . /app

EXPOSE 8080

# Run the app with gunicorn for production-like server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app.app:create_app()"]
