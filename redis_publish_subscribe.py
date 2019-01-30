#!/usr/bin/env python3

import redis
import time
import traceback

redisConnection = redis.StrictRedis(
host="localhost", 
port=6379, 
password="", 
decode_responses=True)

def redis_subscribe_operations():
    print("subscribing")
    try:
        pubsub = redisConnection.pubsub()
        pubsub.subscribe("comments")
        while True:
            message = pubsub.get_message()
            if message:
                print("Message Received is[%s]" % message['data'])
            time.sleep(2)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    redis_subscribe_operations()

#in docker cli execute:
# publish 'comments' 'bla'
