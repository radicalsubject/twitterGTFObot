FROM python:3.8-slim

# Install manually all the missing libraries
RUN apt-get update -qq && apt-get install -y tesseract-ocr

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
ADD . /app
WORKDIR /app

# CMD python /app/bot.py

# older version here
# # --no-capture-output supported only since anaconda 4.9, miniconda doesnt work yet
# FROM continuumio/miniconda3:latest 
# # FROM alpine:3.7
# WORKDIR /twibot
# # Create the environment:
# COPY env.yml .
# RUN conda update -n base -c defaults conda
# # install dependencies
# RUN conda env create -f env.yml
# RUN apt update && apt install -y libsm6 libxext6
# RUN apt-get -y install tesseract-ocr
# RUN conda run -n twibot conda install -y pytorch torchvision -c pytorch
# RUN pip install pillow
# RUN pip install pytesseract
# # copy all other files for bot
# COPY . .
# # Make RUN commands use the new environment: -- activate env doesnt work!!!
# # The SHELL instruction allows the default shell used for the shell form of commands to be overridden. The default shell on Linux is ["/bin/sh", "-c"], and on Windows is ["cmd", "/S", "/C"]. The SHELL instruction must be written in JSON form in a Dockerfile.
# SHELL ["conda", "run", "-n", "twibot", "/bin/bash", "-c"] 
