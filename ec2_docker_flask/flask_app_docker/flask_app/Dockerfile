FROM ubuntu:18.04
MAINTAINER sorush.kh68@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install -y apt-utils
RUN mkdir /app

COPY requirements.txt requirements.txt
COPY ./ /app/

RUN pip3 install -r requirements.txt

WORKDIR /app/

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "app:app"]



