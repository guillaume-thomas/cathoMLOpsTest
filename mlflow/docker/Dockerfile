FROM python:3.11-slim

RUN apt-get update -y && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    libczmq-dev \
    libssl-dev \
    inetutils-telnet \
    bind9utils \
    gcc \
    && apt-get clean

RUN pip install mlflow[extras]
RUN pip install mysqlclient
RUN pip install boto3

EXPOSE 8080

ENTRYPOINT ["mlflow", "server"]