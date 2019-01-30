#!/usr/bin/env python3

import redis

redisConnection = redis.StrictRedis(
    host="localhost", 
    port=6379, 
    password="", 
    decode_responses=True)

def redis_list_operations():
    try:
        redisConnection.delete("eric:wishlist")
        redisConnection.delete("eric:visited")
        
        print(redisConnection.rpush("eric:wishlist", "7wks"))
        print(redisConnection.rpush("eric:wishlist", "gog"))
        print(redisConnection.rpush("eric:wishlist", "prag"))
        
        temp = redisConnection.rpop("eric:wishlist")
        
        redisConnection.lpush("eric:visited",temp)

        print("VISITED Items "+str(redisConnection.lrange("eric:visited",0,-1)))
        print("WISHLIST Items "+str(redisConnection.lrange("eric:wishlist",0,-1)))               
        #atomic pop and push
        redisConnection.rpoplpush("eric:wishlist","eric:visited")

        print("VISITED Items "+str(redisConnection.lrange("eric:visited",0,-1)))
        print("WISHLIST Items "+str(redisConnection.lrange("eric:wishlist",0,-1)))       
    except Exception as e:
        print(e)

if __name__ == '__main__':
    redis_list_operations()