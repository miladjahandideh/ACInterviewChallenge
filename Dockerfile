FROM ubuntu:latest

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update -y && \
    apt install -y python3-pip python3-dev

CMD [ "mkdir", "/usr/src/app/" ]

WORKDIR /usr/src/app

COPY src/* /usr/src/app/

CMD [ "python3", "/usr/src/app/main.py" ]