from .connection import RedisConnection
from .keys import RedisKeys
from .lists import RedisLists


class Redis(RedisConnection, RedisKeys, RedisLists):
    pass
