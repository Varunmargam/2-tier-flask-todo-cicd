# Use an official Python runtime as the base image
FROM python:3.9-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy all the files into the container
COPY . .

# Install app dependencies
RUN pip install --upgrade pip \
    && pip install mysqlclient \
    && pip install -r requirements.txt

# Specify the command to run your application
CMD ["python", "app.py"]

