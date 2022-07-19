FROM python:3.10

ENV PYTHONBUFFERED 1

WORKDIR /code

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-dev

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
