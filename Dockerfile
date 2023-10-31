FROM python:3.10-bookworm

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV OPENAI_API_KEY $OPENAI_API_KEY
