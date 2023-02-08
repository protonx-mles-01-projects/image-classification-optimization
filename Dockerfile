FROM ubuntu:20.04

RUN apt install python3 python3-pip nano

COPY requirements.txt app/requirements.txt
RUN pip3 install -r app/requirements.txt

WORKDIR /app
COPY . /app

ENV FLASK_APP=app.py

CMD ["flask", "run"]

