# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

ENV APP_DIR /usr/local/src/server

COPY . ${APP_DIR}/

WORKDIR ${APP_DIR}

RUN apt-get update && apt-get install -y pipenv && apt-get install -y libpq-dev

RUN pipenv install --system --deploy

EXPOSE 5000

ENV FLASK_APP ${APP_DIR}/app.py

CMD [ "python3", "app.py" ]