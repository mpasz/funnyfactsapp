FROM python:3.9

ENV PYTHONUNBUFFERED 1
# ENV X_API_TOKEN= 
WORKDIR /app

COPY . .
RUN apt-get update \ 
    && apt-get install python3-dev default-libmysqlclient-dev gcc -y

RUN pip install --upgrade pip
RUN pip install pipenv

#Install dependencies
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev

COPY . /app/

EXPOSE 8000