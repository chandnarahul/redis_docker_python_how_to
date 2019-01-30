#!/usr/bin/env python3

import redis

redisConnection = redis.StrictRedis(
    host="localhost", 
    port=6379, 
    password="", 
    decode_responses=True)

def redis_set_operations():
    try:
        redisConnection.sadd("news", "nytimes.com")
        redisConnection.sadd("news", "pragprog.com")

        print("")
        print("print in any order")
        print(redisConnection.smembers("news"))

        redisConnection.sadd("tech", "pragprog.com")
        redisConnection.sadd("tech", "apple.com")

        print("")
        print("print in any order")
        print(redisConnection.smembers("tech"))
        
        print("")
        print("intersection on set")
        print(redisConnection.sinter("news","tech"))
        
        print("")
        print("print non intersecting values from set")
        print(redisConnection.sdiff("news","tech"))
        
        print("")
        print("print unique union of set")
        print(redisConnection.sunion("news","tech"))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    redis_set_operations()