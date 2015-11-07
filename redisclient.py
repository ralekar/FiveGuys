import redis

redisobj = redis.StrictRedis(host='localhost', port=6379, db=0)
redisobj.set("alakr","Ad")
print redisobj.get("alakr")
