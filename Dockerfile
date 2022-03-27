FROM python:3.10.2-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN python3.10 -m pip install -U pip
COPY . /app
WORKDIR /app
RUN python3.10 -m pip install -U -r requirements.txt
CMD bash HELL
