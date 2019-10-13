from redis import StrictRedis, ConnectionPool
url = 'redis://:xiaoming98@localhost:6379/0'
url2 = 'rediss://:xiaoming98@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('name', 'Amy')
print(redis.hincrby('price', 'apple', 2))
