FROM python:3
WORKDIR /home/user/promprog/docker/producer

COPY requirements.txt /home/user/promprog/docker/producer
COPY . .
RUN pip install -r /home/user/promprog/docker/producer/requirements.txt

CMD [ "python", "./producer.py" ]
