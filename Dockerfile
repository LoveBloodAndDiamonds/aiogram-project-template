FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Configure uv link mode
ENV UV_LINK_MODE=copy

# Copy dependency manifests
COPY uv.lock pyproject.toml /app/

# Install dependencies
RUN uv sync --no-dev

# Copy Alembic configuration
COPY alembic.ini /app/alembic.ini

# Copy application
COPY bot /app/bot
