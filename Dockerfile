FROM python:3.11-slim
LABEL maintainer="Luke Tainton <luke@tainton.uk>"
LABEL org.opencontainers.image.source="https://github.com/luketainton/pypilot"
USER root

ENV PYTHONPATH="/run:/usr/local/lib/python3.11/lib-dynload:/usr/local/lib/python3.11/site-packages:/usr/local/lib/python3.11"
WORKDIR /run

RUN mkdir -p /.local && \
    chmod -R 777 /.local && \
    pip install -U pip poetry

COPY pyproject.toml /run/pyproject.toml
COPY poetry.lock /run/poetry.lock

RUN poetry config virtualenvs.create false && \
    poetry install --without dev

ENTRYPOINT ["python3", "-B", "-m", "app.main"]

ARG version="dev"
ENV APP_VERSION=$version

COPY ipilot /run/app
