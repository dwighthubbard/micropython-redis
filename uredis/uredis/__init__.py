# If we remove the following 2 lines we loose basic compatibility with the redis-py module
# but allow for importing only the redis functionality we need which should use less
# memory.
import os

__version__ = '0.0.29'
__copyright__ = "Copyright 2016 Dwight Hubbard"

all = []
for f in os.listdir(os.path.dirname(__file__)):
    if f.endswith('.py'):
        f=f.split('.')[0]
        all.append(f)

from .uredis import Redis, StrictRedis
