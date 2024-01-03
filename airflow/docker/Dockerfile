FROM python:3.11-slim

RUN pip install --upgrade pip

RUN pip install apache-airflow==2.8.0
RUN pip install 'apache-airflow[kubernetes]'
RUN pip install 'apache-airflow[postgres]'

COPY init.sh /tmp/init.sh

COPY bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh
ENTRYPOINT ["/bootstrap.sh"]