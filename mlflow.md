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

Il est parfaitement possible d'executer un projet mlflow dans kubernetes avec : https://mlflow.org/docs/latest/projects.html#kubernetes-execution
Du coup, je ne pense plus avoir besoin de airflow qui reste trop compliqué à installer et à instrumentaliser (même si je pense ne pas être loin ...)

Il faut utiliser les environnements Docker : https://towardsdatascience.com/create-reusable-ml-modules-with-mlflow-projects-docker-33cd722c93c4
https://github.com/gnovack/celeb-cnn-base-image
https://github.com/gnovack/celeb-cnn-project


https://towardsdatascience.com/create-reusable-ml-modules-with-mlflow-projects-docker-33cd722c93c4
https://github.com/gnovack/celeb-cnn-base-image
https://github.com/gnovack/celeb-cnn-project
https://mlflow.org/docs/latest/docker.html
https://blog.noodle.ai/introduction-to-mlflow-for-mlops-part-2-docker-environment/
https://mlflow.org/docs/latest/projects.html
https://mlflow.org/docs/latest/projects.html#kubernetes-execution
https://mlflow.org/docs/latest/projects.html#building-multistep-workflows

https://www.google.com/search?q=mlflow+dataset&rlz=1C1CHBD_frFR1008FR1008&oq=mlflow+dataset&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDQzODVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://mlflow.org/docs/latest/getting-started/logging-first-model/step5-synthetic-data.html
https://mlflo.org/docs/latest/python_api/mlflow.data.html

https://medium.com/@haythemtellili/end-to-end-ml-pipelines-with-mlflow-projects-63a11baa2dd1