FROM python:3

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD src /app/src
ADD data /app/data
ADD app.py /app
WORKDIR /app

ENV AM_I_IN_A_DOCKER_CONTAINER Yes

CMD ["python3",  "/app/app.py"]
