
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip

COPY . /app
WORKDIR /app

RUN pip3 install Flask Flask-RESTful

EXPOSE 5000

CMD ["python3", "app.py"]
