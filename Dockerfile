FROM python:3.12.0-slim

RUN apt update && mkdir /sociality

WORKDIR /socialily

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

EXPOSE 8000

CMD ["python", "src/manage.py", "runserver", "0:8000"]