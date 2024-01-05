Attention à bien faire saisir : 

- le namespace de la sandbox dans kubernetes_job_template.yaml
- variabiliser vars.OPENSHIFT_SERVER, vars.QUAY_ROBOT_USERNAME, vars.OPENSHIFT_USERNAME
- mettre en secrets secrets.QUAY_ROBOT_TOKEN, secrets.OPENSHIFT_TOKEN
- Bien mettre l'url de mlflow dans train.py => remote_server_uri = "http://mlflow-gthomas59800-dev.apps.sandbox-m3.1530.p1.openshiftapps.com"