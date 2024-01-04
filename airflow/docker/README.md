docker build -t test/airflow .
docker images
docker tag 2392637219a7 quay.io/gthomas59800/kto/airflow-2023-2024:1.0.0
docker tag 2392637219a7 quay.io/gthomas59800/kto/airflow-2023-2024:latest
docker push quay.io/gthomas59800/kto/airflow-2023-2024:1.0.0
docker push quay.io/gthomas59800/kto/airflow-2023-2024:latest

