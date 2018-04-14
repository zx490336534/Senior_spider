import redis

r = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)

print(r.get('name'))
r.set('name','test111')
print(r.get('name'))

