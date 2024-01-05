FROM python:3.11-slim

RUN pip install mlflow numpy pandas scikit-learn boto3

COPY train.py .
COPY wine-quality.csv .