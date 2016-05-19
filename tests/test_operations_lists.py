#!/usr/bin/env python3
"""
Tests to validate redis list functionality is working properly with micropython
"""
# Notes:
#
# 1. These tests should be run with a cpython interpreter with the redislite module installed.
# 2. The micropython executable should be accesible in the path.
import json
import os
import redislite
import subprocess
import tempfile
from unittest import main, TestCase
import redis
import uredis


class TestRedisListOperations(TestCase):
    redis_test_port = 7899

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': self.redis_test_port})

    def tearDown(self):
        self.redis_server.shutdown()

    def test_lrange_empty_list(self):
        result = redis.Redis(port=self.redis_test_port).lrange("testlist", 0, -1)
        uresult = uredis.Redis(port=self.redis_test_port).lrange("utestlist", 0, -1)
        self.assertEqual(uresult, result)

    def test_blpop_empty_list_with_timeout(self):
        result = redis.Redis(port=self.redis_test_port).blpop('testlist', timeout=1)
        uresult = uredis.Redis(port=self.redis_test_port).blpop('utestlist', timeout=1)
        self.assertEqual(uresult, result)


    def test_lpush_new_list_integer_value(self):
        result = redis.Redis(port=self.redis_test_port).lpush('testlist', 1)
        uresult = uredis.Redis(port=self.redis_test_port).lpush('utestlist', 1)
        self.assertEqual(uresult, result)


if __name__ == '__main__':
    main()
