FROM rendyprojects/python:latest

WORKDIR /app/

RUN apt -qq update
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    unzip \
    wget \
    python3-pip \
    ffmpeg

COPY . .

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt

CMD [ "bash", "./start" ]
