FROM python:3.12.0-slim

RUN apt update
RUN mkdir /sociality

WORKDIR /socialily

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["python", "src/manage.py", "runserver", "127.0.0.1:8000"]
