FROM python:3.8-slim
MAINTAINER parkyes90
RUN pip install --upgrade pip
RUN pip install pipenv
WORKDIR /app

COPY Pipfile* /tmp/
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN cd /tmp && pipenv lock -d --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/