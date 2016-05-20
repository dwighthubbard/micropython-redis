#!/usr/bin/env python3
"""
Tests to validate redis list functionality is working properly with micropython
"""
# Notes:
#
# 1. These tests should be run with a cpython interpreter with the redislite module installed.
# 2. The micropython executable should be accesible in the path.
import logging
import redis
import redislite
from unittest import main, TestCase
import uredis


class TestRedisConnection(TestCase):
    redis_test_port = 7899

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': self.redis_test_port})
        self.uredis_client = uredis.Redis(host='127.0.0.1', port=self.redis_test_port)

    def tearDown(self):
        if self.redis_server:
            self.redis_server.shutdown()

    def test_hset(self):
        result = self.redis_server.hset("testkey", 'key', 'value')
        uresult = self.uredis_client.hset("testkey2", 'key', 'value')
        self.assertEqual(uresult, result)

    def test_hdel(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hdel("testkey", 'key', 'value')
        self.redis_server.hset("testkey2", 'key', 'value')
        uresult = self.uredis_client.hdel("testkey2", 'key', 'value')
        self.assertEqual(uresult, result)

    def test_hexists(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hexists("testkey", 'key')
        self.redis_server.hset("testkey2", 'key', 'value')
        uresult = self.uredis_client.hexists("testkey2", 'key')
        self.assertEqual(uresult, result)

    def test_hget(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hget("testkey", 'key')
        self.redis_server.hset("testkey2", 'key', 'value')
        uresult = self.uredis_client.hget("testkey2", 'key')
        self.assertEqual(uresult, result)

    def test_hgetall(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hgetall("testkey")
        self.redis_server.hset("testkey2", 'key', 'value')
        uresult = self.uredis_client.hgetall("testkey2")
        self.assertEqual(uresult, result)

    def test_hincrby(self, *args):
        self.redis_server.hset("testkey", 'key', 1)
        result = self.redis_server.hincrby("testkey", 'key', 1)
        self.redis_server.hset("testkey2", 'key', 1)
        uresult = self.uredis_client.hincrby("testkey2", 'key', 1)
        self.assertEqual(uresult, result)

    def test_hincrbyfloat(self, *args):
        self.redis_server.hset("testkey", 'key', 1.0)
        result = self.redis_server.hincrbyfloat("testkey", 'key', .1)
        self.redis_server.hset("testkey2", 'key', 1.0)
        uresult = self.uredis_client.hincrbyfloat("testkey2", 'key', .1)
        self.assertEqual(uresult, result)

    def test_hkeys(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hkeys("testkey")
        uresult = self.uredis_client.hkeys("testkey")
        self.assertEqual(uresult, result)

    def test_hlen(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hlen("testkey")
        uresult = self.uredis_client.hlen("testkey")
        self.assertEqual(uresult, result)

    def test_hmget(self, *args):
        self.redis_server.hset("testkey", 'key', 'value')
        result = self.redis_server.hmget("testkey", 'key')
        uresult = self.uredis_client.hmget("testkey", 'key')
        self.assertEqual(uresult, result)

    def test_hsetnx(self, *args):
        result = self.redis_server.hsetnx("testkey", 'key', 'value')
        uresult = self.uredis_client.hsetnx("testkey2", 'key', 'value')
        self.assertEqual(uresult, result)

    def hstrlen(self, *args):
        result = self.redis_server.hstrlen("testkey", 'key', 'value')
        uresult = self.uredis_client.hstrlen("testkey2", 'key', 'value')
        self.assertEqual(uresult, result)

    def hvals(self, *args):
        result = self.redis_server.hset("testkey", 'key', 'value')
        uresult = self.uredis_client.hset("testkey2", 'key', 'value')
        self.assertEqual(uresult, result)

    def hscan(self, *args):
        result = self.redis_server.hset("testkey", 'key', 'value')
        uresult = self.uredis_client.hset("testkey2", 'key', 'value')
        self.assertEqual(uresult, result)


if __name__ == '__main__':
    logger = logging.getLogger('redislite.client')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    main()
