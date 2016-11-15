FROM alpine:3.4

RUN apk update 
RUN apk add python
RUN apk add py-pip
RUN apk add python-dev
RUN apk add py-requests

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY acicobra-1.3_2h-py2.7.egg /opt/
COPY acimodel-1.3_2h-py2.7.egg /opt/
#RUN easy_install-2.7 -Z /opt/acicobra-1.3_2h-py2.7.egg
#RUN easy_install-2.7 -Z /opt/acimodel-1.3_2h-py2.7.egg
EXPOSE 5000

