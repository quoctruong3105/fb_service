import redis

redis_client = redis.StrictRedis(host='localhost', port=3106, db=0)

while True:
    message = redis_client.blpop('data', timeout=30)
    if message:
        print("Nhận tin nhắn:", message[1].decode('utf-8'))
    else:
        print("Không có tin nhắn mới trong hàng đợi.")
