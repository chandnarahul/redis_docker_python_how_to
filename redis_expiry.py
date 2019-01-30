#!/usr/bin/env python3

import redis
import time

redisConnection = redis.StrictRedis(
    host="localhost", 
    port=6379, 
    password="", 
    decode_responses=True)

def redis_expiry_operations():
    try:
        redisConnection.set("ice", "I'm melting...")

        redisConnection.expire("ice", 5)
        
        time.sleep(1)
        for x in range(0, 5):
            print("")
            print("Exists ?")
            print(redisConnection.get("ice"))
            print(redisConnection.ttl("ice"))
            time.sleep(1)



        redisConnection.setex("ice", 5, "I'm melting...")

        print("")
        print("SETEX")
        print("")
        time.sleep(1)
        for x in range(0, 5):
            print("")
            print("Exists ?")
            print(redisConnection.get("ice"))
            print(redisConnection.ttl("ice"))
            time.sleep(1)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    redis_expiry_operations()