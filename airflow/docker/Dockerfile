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

RUN pip install --upgrade pip

RUN pip install apache-airflow==2.8.0
RUN pip install 'apache-airflow[kubernetes]'
RUN pip install 'apache-airflow[mysql]'
RUN pip install mysqlclient

COPY init.sh /tmp/init.sh

COPY bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh
ENTRYPOINT ["/bootstrap.sh"]