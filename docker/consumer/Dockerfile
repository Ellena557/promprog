FROM python:3
WORKDIR /home/user/promprog/docker/consumer

COPY requirements.txt /home/user/promprog/docker/consumer
COPY . .
RUN pip install -r /home/user/promprog/docker/consumer/requirements.txt

CMD [ "python", "./consumer.py" ]

