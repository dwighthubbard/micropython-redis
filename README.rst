.. image:: https://travis-ci.org/dwighthubbard/micropython-redis.svg?branch=master
    :target: https://travis-ci.org/dwighthubbard/micropython-redis

.. image:: https://img.shields.io/pypi/v/micropython-redis.svg
    :target: https://pypi.python.org/pypi/micropython-redis/

.. image:: https://img.shields.io/badge/python-micropython-blue.svg
    :target: https://pypi.python.org/pypi/micropython-redis/

.. image:: https://img.shields.io/pypi/l/micropython-redis.svg
    :target: https://pypi.python.org/pypi/micropython-redis/

---------------------------------------------------------------------

.. image:: https://readthedocs.org/projects/micropython-redis/badge/?version=latest
    :target: http://micropython-redis.readthedocs.io/en/latest/
    :alt: Documentation

-----------------------------------------------------------------------------------------------------------------------

micropython-redis
=================

A redis client implementation designed for use with micropython.

This module is a new redis-client written to be functional when using Micropython on embedded microcontrollers with
limited resources.

In order to function on microcontrollers without multitasking operating systems the implementation does not use
threading or multiprocessing.  As a result functionality that relies on these features such as connection pools
is not available.

This implementation can utilize ssl and floating point support if it is available but it will operate with reduced
functionality if it is not.

Current Status
==============

Currently this module is not feature complete, here is the current status

+---------------------+-----------------+-----------+------------------------+
| Redis Command Group | Implemented     | Tests     | Notes                  |
+=====================+=================+===========+========================+
| Cluster             | Not Planned     |           |                        |
+---------------------+-----------------+-----------+------------------------+
| Connection          | Complete        | 100%      |                        |
+---------------------+-----------------+-----------+------------------------+
| Geo                 | Complete        | 0%        |                        |
+---------------------+-----------------+-----------+------------------------+
| Hashes              | Complete        | 100%      |                        |
+---------------------+-----------------+-----------+------------------------+
| HyperLogLog         | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
| Keys                | Completed       | 0%        |                        |
+---------------------+-----------------+-----------+------------------------+
| Lists               | Complete        | 40%       |                        |
+---------------------+-----------------+-----------+------------------------+
| Publish/Subscribe   | Not Complete    | None      | API works differently  |
|                     |                 |           | than other             |
|                     |                 |           | functionality,         |
|                     |                 |           | so will likely use more|
|                     |                 |           | resources and require  |
|                     |                 |           | more work to implement.|
+---------------------+-----------------+-----------+------------------------+
| Scripting           | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
| Server              | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
| Sets                | Complete        | 20%       |                        |
+---------------------+-----------------+-----------+------------------------+
| Sorted Sets         | Complete        | 0%        |                        |
+---------------------+-----------------+-----------+------------------------+
| Strings             | Complete        | 0%        |                        |
+---------------------+-----------------+-----------+------------------------+
| Transactions        | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
