FROM python:3.11.1-alpine3.17 as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

FROM base as builder

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN apk update \
    && apk add --no-cache \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry export --without-hashes \
        -f requirements.txt \
        -o requirements.txt \
    && pip wheel \
        --no-cache-dir \
        --no-deps \
        --wheel-dir /usr/src/app/wheels \
        -r requirements.txt

FROM base as final

ARG PROJECT=web

WORKDIR /home/${PROJECT}/web

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
COPY . .

RUN addgroup -S ${PROJECT} \
    && adduser -S ${PROJECT} -G ${PROJECT} \
    && apk update \
    && apk add \
        libpq \
    && pip install --no-cache /wheels/* \
    && chown -R ${PROJECT}:${PROJECT} /home/${PROJECT}

USER web
