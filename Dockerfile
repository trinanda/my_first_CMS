FROM python:3.7.0a4-stretch

MAINTAINER Tri Nanda <zidanecr7kaka@gmail.com>

ENV INSTALL_PATH_DI_DALAM_DOCKER /aplikasi_web_docker

WORKDIR $INSTALL_PATH_DI_DALAM_DOCKER

COPY requirements.txt requirements_docker.txt

RUN pip install -r requirements_docker.txt


