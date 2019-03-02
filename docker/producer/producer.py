#!/usr/bin/env python
import pika
import sys
import random
import time


def do_sleeping():
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)


def do_generating(channel):
    number = random.randint(-2**31, 2**31 - 1)
    print('Producer is sending number ', number, flush=True)
    channel.basic_publish(exchange='',
                          routing_key='random_rabbit',
                          body=str(number))


def do_connect():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()

    channel.queue_declare(queue = 'random_rabbit')
    return connection, channel


def main():
    do_sleeping()
    print('Producer starts working')

    while True:
        try:
            connection, mychannel = do_connect()
            while True:
                do_sleeping()
                do_generating(mychannel)
        except pika.exceptions.ConnectionClosed:
            do_sleeping()
            print('Connection is closed, need to retry')

    connection.close()


if __name__ == '__main__':
    main()
