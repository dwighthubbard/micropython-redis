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

+---------------------+-----------------+-----------+
| Redis Command Group | Implemented     | Tests     |
+=====================+=================+===========+
| Cluster             | Not Planned     |           |
+---------------------+-----------------+-----------+
| Connection          | Complete        | No        |
+---------------------+-----------------+-----------+
| Geo                 | Not Implemented |           |
+---------------------+-----------------+-----------+
| Hashes              | Not Implemented |           |
+---------------------+-----------------+-----------+
| HyperLogLog         | Not Implemented |           |
+---------------------+-----------------+-----------+
| Keys                | Completed       | None      |
+---------------------+-----------------+-----------+
| Lists               | Complete        | Partial   |
+---------------------+-----------------+-----------+
| Publish/Subscribe   | Not Implemented |           |
+---------------------+-----------------+-----------+
| Scripting           | Not Planned     |           |
+---------------------+-----------------+-----------+
| Server              | Not Implemented |           |
+---------------------+-----------------+-----------+
| Sets                | Not Implemented |           |
+---------------------+-----------------+-----------+
| Sorted Sets         | Not Implemented |           |
+---------------------+-----------------+-----------+
| Strings             | Not Implemented |           |
+---------------------+-----------------+-----------+
| Transactions        | Not Implemented |           |
+---------------------+-----------------+-----------+
