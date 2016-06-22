# If we remove the following 2 lines we loose basic compatibility with the redis-py module
# but allow for importing only the redis functionality we need which should use less
# memory.
try:
    import os
except ImportError:
    import uos

__version__ = '0.0.0'
__copyright__ = "Copyright 2016 Dwight Hubbard"

from .uredis import Redis, StrictRedis
