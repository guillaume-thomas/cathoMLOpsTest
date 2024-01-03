This example is build from this tutorial : https://www.bhavaniravi.com/apache-airflow/deploying-airflow-on-kubernetes

This is the link to the sources : https://github.com/bhavaniravi/airflow-kube-setup

Many Thanks to Bhavani Ravi !!

Be warn with airflow.cfg => secret-key has to be a "secure" value : https://stackoverflow.com/questions/73068358/error-while-upgrading-airflow-1-11-to-1-15
Use : openssl rand -hex 30 and replace in the config map