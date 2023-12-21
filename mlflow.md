Protéger notre serveur : https://mlflow.org/docs/latest/auth/index.html
Sinon : https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/
Quelques idées pour créer un server mlflow sur openshift : https://github.com/pdemeulenaer/mlflow-on-kubernetes
Exemple d'image docker : https://github.com/pdemeulenaer/mlflow-image/blob/main/Dockerfile

Il est possible de se connecter à un server mlflow distant. Il faut que je teste ça une fois que je le prends en main.

Je vais tout de même tout de suite tester avec un mlflow openshift.

Une fois que c'est fait, j'aurai accès à MlFlow Tracking, project et model registry (normalement)

Comme si j'avais mon propre databricks

Les pipelines sont possibles ici : https://www.mlflow.org/docs/1.28.0/python_api/mlflow.pipelines.html

Le nouveau nom des pipelines est recipes : https://mlflow.org/docs/latest/recipes.html

Demo de coursera (nulle) https://github.com/alfredodeza/mlflow-demo

Demo de connection à un server mlflow distant : https://www.youtube.com/watch?v=K9se7KQON5k