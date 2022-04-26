FROM python:3

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY src /app/src
COPY app.py /app
WORKDIR /app

ENV TWITTER_BEARER XX

CMD ["python3",  "/app/app.py"]
