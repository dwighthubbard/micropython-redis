redis_components = []
try:
    from ..uredis_modular.connection import Connection
    redis_components.append(Connection)
except ImportError:
    pass

try:
    from ..uredis_modular.geo import Geo
    redis_components.append(Geo)
except ImportError:
    pass

try:
    from ..uredis_modular.hash import Hash
    redis_components.append(Hash)
except ImportError:
    pass

# from .hyperloglog import HyperLogLog

try:
    from ..uredis_modular.key import Key
    redis_components.append(Key)
except ImportError:
    pass

try:
    from ..uredis_modular.list import List
    redis_components.append(List)
except ImportError:
    pass

try:
    from ..uredis_modular.pubsub import PubSub
    redis_components.append(PubSub)
except ImportError:
    pass

# from .server import Server

try:
    from ..uredis_modular.set import Set
    redis_components.append(Set)
except ImportError:
    pass

try:
    from ..uredis_modular.sortedset import SortedSet
    redis_components.append(SortedSet)
except ImportError:
    pass


try:
    from ..uredis_modular.string import String
    redis_components.append(String)
except ImportError:
    pass

# from .transaction import Transaction


class Redis(*redis_components):
    """
    Primary Redis Client Class.

    This class provides a Redis Client with all the functionality of the supported subclasses.

    This class is intended to be mostly compatible with the redis-py redis.Redis()/redis.StrictRedis() classes.
    """
    pass


class StrictRedis(Redis):
    pass
