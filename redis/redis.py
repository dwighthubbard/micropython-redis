from .keys import RedisKeys
from .lists import RedisLists


class Redis(RedisKeys, RedisLists):
    pass
