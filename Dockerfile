#start docker with python

FROM python:3.11.6-slim-bullseye

ENV PYTHONUNPUFFERED = 1

#isntall nedded li  braries

RUN apt-get update && apt-get -y install libpq-dev gcc

#create project folder

WORKDIR /app

#copy requirments file ---> app

COPY requirments.txt /app/requirments.txt

#install libraries

RUN pip install -r /app/requirments.txt

#COPY all files -->app

COPY . /app/

