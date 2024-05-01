import redis

redis_client = redis.StrictRedis(host='localhost', port=3106, db=0)

while True:
    message = redis_client.blpop('data', timeout=30)
    if message:
        print("------------------------")
        print("New data:", message[1].decode('utf-8'))
    else:
        print("There is no new data.")
