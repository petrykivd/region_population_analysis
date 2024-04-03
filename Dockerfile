FROM python:3.10-slim-buster
LABEL authors="petrykivd"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .