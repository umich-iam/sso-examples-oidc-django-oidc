# FROM directive instructing base image to build upon
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Installs needed Linux packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential git && \
    apt-get clean -y

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app/
COPY . /app/

# Sets the local timezone of the Docker image
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["/bin/bash", "start.sh"]

# Done!