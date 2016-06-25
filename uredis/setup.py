import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup


setup(
    name='micropython-redis',
    version='0.0.46',
    description='redis module for MicroPython',
    long_description="""This is a redis client module implemented specifically for MicroPython.

As a result, this module does not support functionality not available on embedded environments and it is structured to
allow operating in environments with limited resources.

Note that this module is a work in progress and currently supports just a subset of all of the redis functionality

Please help with the development if you are interested in this module.""",
    url='https://github.com/dhubbard/micropython-redis',
    author='Dwight Hubbard',
    author_email="dwight@dwighthubbard.com",
    extras_require = {
        'all': [
            'micropython-redis.connection',
            'micropython-redis.geo',
            'micropython-redis.hash',
            'micropython-redis.key',
            'micropython-redis.list',
            'micropython-redis.pubsub',  # Pubsub works differently and isn't currently implemented
            'micropython-redis.set',
            'micropython-redis.sortedset',
            'micropython-redis.string',
        ]
    },
    install_requires=[
        'micropython-redis-modular',
        'micropython-redis.client',
    ],
    maintainer='Dwight Hubbard',
    maintainer_email='dwight@dwighthubbard.com',
    license='MIT',
    packages=['uredis'],
    zip_safe=True,
)
