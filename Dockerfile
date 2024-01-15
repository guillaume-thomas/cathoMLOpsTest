FROM python:3.11.2-bullseye

ENV APP_ROOT=/opt/app-root

WORKDIR ${APP_ROOT}

COPY boot.py ./boot.py
COPY packages ./packages
COPY init_packages.sh ./init_packages.sh
COPY cats_and_dogs/api ./cats_and_dogs/api

RUN chmod 777 ./init_packages.sh
RUN ./init_packages.sh

EXPOSE 8080

ENTRYPOINT ["python3", "boot.py"]