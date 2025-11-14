FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY portscanner_main.py ./

CMD [ "python3", "portscanner_main.py"]


