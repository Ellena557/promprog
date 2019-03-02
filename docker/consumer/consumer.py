#!/usr/bin/env python
import pika
import sys
import random
import time


def do_sleeping():
    sleep_time = random.randint(10, 27)
    time.sleep(sleep_time)


def callback(ch, method, properties, body):
    print('Consumer received number ', body, flush = True)


def do_receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='random_rabbit')
    channel.basic_consume(callback, queue='random_rabbit')   
    return connection, channel 


def main():
    do_sleeping()
    print('Consumer starts working')
    connection, mychannel = do_receive() 

    while True:
        try:
            mychannel.start_consuming()
        except pika.exceptions.ConnectionClosed: 
            do_sleeping()
            print('Connection is closed, need to retry')
            mychannel.stop_consuming()

    connection.close()


if __name__ == '__main__':
    main()
