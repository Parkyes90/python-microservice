FROM python:3.8-slim
MAINTAINER parkyes90
RUN pip install --upgrade pip
RUN pip install pipenv
WORKDIR /app

COPY Pipfile* /tmp/
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y gcc postgresql-client python3-dev libc-dev libpq-dev
RUN apt-get clean

RUN cd /tmp && pipenv lock -d --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/