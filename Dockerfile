# Base image - Python3.6 for Debian 9
FROM python:3.7-stretch
MAINTAINER Audhi Aprilliant <audhiaprilliant@gmail.com>

# Run updates, install basics, and cleanup
RUN apt-get update -qq \
    && apt-get install -y gcc make apt-transport-https ca-certificates build-essential --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Checkout our Python environment
RUN python3 --version
RUN pip3 --version

# Create application source code directory
RUN mkdir -p /web-scraping-covid-kompas

# Set the working directory for containers
WORKDIR /web-scraping-covid-kompas

# Install Python dependencies
COPY . /web-scraping-covid-kompas
RUN pip3 install --no-cache-dir -r requirements.txt

# Set volume for sharing data
VOLUME /web-scraping-covid-kompas/Datasets

# Running Python Application
ENTRYPOINT ["python3","'Web Scraping Covid-19 Kompas News.py'"]
