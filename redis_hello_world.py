#!/usr/bin/env python3

import redis

redisConnection = redis.StrictRedis(
    host="localhost", 
    port=6379, 
    password="", 
    decode_responses=True)

def redis_hello_world():
    try:
        redisConnection.set("message", "Hello World.")
        
        print(redisConnection.get("message"))        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    redis_hello_world()