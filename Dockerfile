FROM python:3.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    g++

WORKDIR /src

COPY requirements.txt .
RUN pip3 install --upgrade pip setuptools && pip3 install -r requirements.txt --proxy=${HTTP_PROXY}

COPY . .
