FROM python:3.8.2

EXPOSE 5000

WORKDIR /code/src

COPY poetry.lock pyproject.toml /code/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /code/
