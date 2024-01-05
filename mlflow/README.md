This example is build from this tutorial : https://github.com/pdemeulenaer/mlflow-on-kubernetes

Many Thanks to Philippe de Meulenaer !!


docker build -t test/mlflow .
docker images
docker tag 2392637219a7 quay.io/gthomas59800/kto/mlflow-2023-2024:1.0.0
docker tag 2392637219a7 quay.io/gthomas59800/kto/mlflow-2023-2024:latest
docker push quay.io/gthomas59800/kto/mlflow-2023-2024:1.0.0
docker push quay.io/gthomas59800/kto/mlflow-2023-2024:latest