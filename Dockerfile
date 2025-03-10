FROM python:3.12

COPY requirements.txt /temp/requirements.txt

COPY stripe_project /stripe_project

WORKDIR /stripe_project

EXPOSE 8000

RUN pip install -r /temp/requirements.txt
