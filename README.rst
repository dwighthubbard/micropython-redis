.. image:: https://travis-ci.org/dwighthubbard/micropython-redis.svg?branch=master
    :target: https://travis-ci.org/dwighthubbard/micropython-redis

-----------------------------------------------------------------------------------------------------------------------

micropython-redis
=================

A redis client implementation designed for use with micropython.

This module is a new redis-client written to be functional when using Micropython on embedded microcontrollers with
limited resources.

In order to function on microcontrollers without multitasking operating systems the implementation does not use
threading or multiprocessing.  As a result functionality that relies on these features such as connection pools
are not available.

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
| Geo                 | Complete        | None      |                        |
+---------------------+-----------------+-----------+------------------------+
| Hashes              | Complete        | 100%      |                        |
+---------------------+-----------------+-----------+------------------------+
| HyperLogLog         | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
| Keys                | Completed       | None      |                        |
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
| Strings             | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
| Transactions        | Not Implemented |           |                        |
+---------------------+-----------------+-----------+------------------------+
