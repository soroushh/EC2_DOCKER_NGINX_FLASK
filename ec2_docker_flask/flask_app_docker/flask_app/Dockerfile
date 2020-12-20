FROM ubuntu:18.04
MAINTAINER sorush.kh68@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install -y apt-utils
#RUN apt-get install gunicorn3

COPY requirements.txt requirements.txt
COPY ./ /opt/

RUN pip3 install -r requirements.txt

WORKDIR /opt/

CMD ['gunicorn','-b','0.0.0.0:8000','app:app']



