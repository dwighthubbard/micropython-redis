# If we remove the following 2 lines we loose basic compatibility with the redis-py module
# but allow for importing only the redis functionality we need which should use less
# memory.
from .redis import Redis
from .redis import Redis as StrictRedis

__version__ = '0.0.1'
__copyright__ = "Copyright 2016 Dwight Hubbard"