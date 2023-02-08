FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y 

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python", "app.py"]