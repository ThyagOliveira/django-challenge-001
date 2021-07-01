FROM python:3.9.4-buster

# RUN apt update -y && apt install -y gettext # Usado apenas para a geração de traduções
RUN useradd -ms /bin/bash challenge
USER challenge

ENV PYTHONUNBUFFERED 1
WORKDIR /home/challenge/app
ENV PATH $PATH:/home/challenge/.local/bin

RUN python -m pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000