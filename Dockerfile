# syntax=docker/dockerfile:1

FROM python:3.10-slim@sha256:48991dce6601b7c3b8f08f21dc211608a1c233c76945e5435df4bae626a5f648

WORKDIR /usr/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"] 