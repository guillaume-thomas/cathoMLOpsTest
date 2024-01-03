#!/bin/bash
airflow db init && \
#airflow connections create-default-connections && \
cd /usr/local/lib/python3.11/site-packages/airflow
alembic upgrade heads && \
(airflow users create --username ktoairflow --lastname kto --firstname jon --email airflow@apache.org --role Admin --password ktomlops || true)