FROM python:3.12.2

WORKDIR /app

COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

RUN pip install poetry
RUN poetry install

COPY . .

CMD ["python"], ["hw_2.py"] ]

