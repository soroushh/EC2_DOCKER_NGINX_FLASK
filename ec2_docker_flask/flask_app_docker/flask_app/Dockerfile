FROM ubuntu:18.04
MAINTAINER sorush.kh68@gmail.com

RUN apt-get update -y
RUN apt-get install python2-pip -y
RUN apt-get install -y apt-utils

COPY requirements.txt requirements.txt
COPY ./ /opt/

RUN pip install -r requirements.txt

WORKDIR /opt/

CMD ['gunicorn','-b','0.0.0.0:8000','app:app']



