#!/usr/bin/env python3

import redis

redisConnection = redis.StrictRedis(
    host="localhost", 
    port=6379, 
    password="", 
    decode_responses=True)

def redis_broadcast_operations():
    try:
        print(redisConnection.brpop("comments", "300"))
        
        # On redis docker CLI type:
        # LPUSH comments "Prag is a great publisher!"
    except Exception as e:
        print(e)

if __name__ == '__main__':
    redis_broadcast_operations()