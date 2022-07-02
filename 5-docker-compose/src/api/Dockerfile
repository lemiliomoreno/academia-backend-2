FROM python:3.10

WORKDIR /api

ENV PYTHONBUFFERED 1

COPY project/ .
COPY poetry.lock .
COPY pyproject.toml .
COPY docker-entrypoint.sh .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

ENTRYPOINT /bin/bash docker-entrypoint.sh
