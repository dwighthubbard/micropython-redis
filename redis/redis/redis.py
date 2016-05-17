from .connection import Connection
# from .hash import Hash
# from .hyperloglog import HyperLogLog
from .key import Key
from .list import List
# from .pubsub import PubSub
# from .server import Server
# from .set import Set
# from .sortedset import SortedSet
# from .string import String
# from .transaction import Transaction


class Redis(
    Connection,
    # Geo,
    # Hash,
    # HyperLogLog,
    Key,
    List,
    # PubSub,
    # Server,
    # Set,
    # SortedSet,
    # String,
    # Transaction
):
    """
    Primary Redis Client Class.

    This class provides a Redis Client with all the functionality of the supported subclasses.

    This class is intended to be mostly compatible with the redis-py redis.Redis()/redis.StrictRedis() classes.
    """
    pass
