# Dockerfile for deploying the machine learning model
FROM python:3.6

copy . /deploy
WORKDIR /deploy

RUN pip3 install -r requirements.txt
CMD ["python", "fask_deployement.py"]
