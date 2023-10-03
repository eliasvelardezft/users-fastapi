FROM python:3.11-slim-buster

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, disable to reduce image size
    PIP_NO_CACHE_DIR=1


WORKDIR /app

ARG DEV

RUN apt update && \
    apt upgrade -y && \
    apt install -y --no-install-recommends python3-pip && \
    apt autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock

RUN if [ "$DEV" ];then poetry install; else poetry install  --only main; fi

COPY ./src /app
