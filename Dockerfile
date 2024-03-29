FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver"]
