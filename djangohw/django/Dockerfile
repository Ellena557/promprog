FROM python:3
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . .
CMD ["/bin/sh", "/app/run.sh"]
