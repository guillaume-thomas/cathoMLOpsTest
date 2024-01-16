ARG MLFLOW_RUN_ID
ARG MLFLOW_TRACKING_URI
ARG MLFLOW_S3_ENDPOINT_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

FROM python:3.11.2-bullseye as mlflow
ARG MLFLOW_RUN_ID
ARG MLFLOW_TRACKING_URI
ARG MLFLOW_S3_ENDPOINT_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV MLFLOW_TRACKING_URI=${MLFLOW_TRACKING_URI}
ENV MLFLOW_S3_ENDPOINT_URL=${MLFLOW_S3_ENDPOINT_URL}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

ENV APP_ROOT=/opt/app-root

WORKDIR ${APP_ROOT}

COPY --chown=${USER} cats_and_dogs/api ./cats_and_dogs/api

RUN pip install mlflow[extras]

RUN mlflow artifacts download -u runs:/${MLFLOW_RUN_ID}/models/data/model.h5 -d ./cats_and_dogs/api/resources

FROM python:3.11.2-bullseye as runtime

ENV APP_ROOT=/opt/app-root

WORKDIR ${APP_ROOT}

COPY --chown=${USER} boot.py ./boot.py
COPY --chown=${USER} packages ./packages
COPY --chown=${USER} setup_api_dependencies.sh ./setup_api_dependencies.sh
COPY --chown=${USER} --from=mlflow ${APP_ROOT}/cats_and_dogs/api ./cats_and_dogs/api

RUN chmod 777 ./setup_api_dependencies.sh
RUN ./setup_api_dependencies.sh

EXPOSE 8080

ENTRYPOINT ["python3", "boot.py"]