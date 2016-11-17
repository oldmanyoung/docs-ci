FROM alpine:latest
MAINTAINER Steve Young (smyoung@cisco.com)

RUN apk update
RUN apk add python
RUN apk add py-pip
RUN pip install --upgrade pip
RUN pip install mkdocs
