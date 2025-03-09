FROM python:3.11.2

ENV DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone && \
    apt-get update && apt install -y tzdata

RUN yes | apt-get install gcc ffmpeg

WORKDIR /code

COPY app/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY app /code

CMD ["python", "main.py"]