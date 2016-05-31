redis_components = []
try:
    from .connection import Connection
    redis_components.append(Connection)
except ImportError:
    pass

try:
    from .geo import Geo
    redis_components.append(Geo)
except ImportError:
    pass

try:
    from .hash import Hash
    redis_components.append(Hash)
except ImportError:
    pass

# from .hyperloglog import HyperLogLog

try:
    from .key import Key
    redis_components.append(Key)
except ImportError:
    pass

try:
    from .list import List
    redis_components.append(List)
except ImportError:
    pass

# from .pubsub import PubSub
# from .server import Server
# from .set import Set
# from .sortedset import SortedSet
# from .string import String
# from .transaction import Transaction


class Redis(*redis_components):
    """
    Primary Redis Client Class.

    This class provides a Redis Client with all the functionality of the supported subclasses.

    This class is intended to be mostly compatible with the redis-py redis.Redis()/redis.StrictRedis() classes.
    """
    pass
