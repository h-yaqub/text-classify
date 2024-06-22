# Use an official Python runtime as a base image
FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install pip
RUN pip install pip==23.3.2

# Set the working directory in the container
WORKDIR /opt/code

# Copy the current directory contents into the container at /
COPY . ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
