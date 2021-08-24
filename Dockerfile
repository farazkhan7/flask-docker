# pull official base image
FROM python:3.9.1-alpine

# set work directory
WORKDIR /src

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
