ARG PYTHON_VERSION=3.13

FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:${PATH}"

RUN apk update
RUN apk add --no-cache curl

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN uv sync --no-cache --no-dev

COPY . .