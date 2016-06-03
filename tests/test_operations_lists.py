#!/usr/bin/env python3
"""
Tests to validate redis list functionality is working properly with micropython
"""
# Notes:
#
# 1. These tests should be run with a cpython interpreter with the redislite module installed.
# 2. The micropython executable should be accesible in the path.
import logging
import redislite
from unittest import main, TestCase
import uredis


class TestRedisListOperations(TestCase):
    redis_test_port = 7902

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': self.redis_test_port})
        self.uredis_client = uredis.Redis(host='127.0.0.1', port=self.redis_test_port)

    def tearDown(self):
        self.redis_server.shutdown()
        self.redis_server.shutdown()

    def test_lrange_empty_list(self):
        result = self.redis_server.lrange("testlist", 0, -1)
        uresult = self.uredis_client.lrange("utestlist", 0, -1)
        self.assertEqual(uresult, result)

    def test_blpop_empty_list_with_timeout(self):
        result = self.redis_server.blpop('testlist', timeout=1)
        uresult = self.uredis_client.blpop('utestlist', timeout=1)
        self.assertEqual(uresult, result)

    def test_brpop_empty_list_with_timeout(self):
        result = self.redis_server.brpop('testlist', timeout=1)
        uresult = self.uredis_client.brpop('utestlist', timeout=1)
        self.assertEqual(uresult, result)

    def test_lpush_new_list_integer_value(self):
        result = self.redis_server.lpush('testlist', 1)
        uresult = self.uredis_client.lpush('utestlist', 1)
        self.assertEqual(uresult, result)

    def test_brpop(self, *args):
        self.redis_server.rpush('testlist', 1)
        result = self.redis_server.brpop('testlist', timeout=1)
        self.redis_server.rpush('testlist', 1)
        uresult = self.uredis_client.brpop('testlist', timeout=1)
        self.assertEqual(uresult, result)

    def test_brpoplpush(self, *args):
        self.redis_server.rpush('testlist', 1)
        self.redis_server.rpush('utestlist', 1)
        result =self.redis_server.brpoplpush('testlist', 'testlistdest', timeout=1)
        uresult = self.uredis_client.brpoplpush('utestlist', 'utestlistdest', timeout=1)
        self.assertEqual(uresult, result)
        result = self.redis_server.lrange('testlistdest', 0, -1)
        uresult = self.redis_server.lrange('utestlistdest', 0, -1)
        self.assertEqual(uresult, result)

    def test_lpop_empty(self, *args):
        result = self.redis_server.rpop('testlist')
        uresult = self.uredis_client.lpop('testlist')
        self.assertEqual(uresult, result)

    def test_lpop(self, *args):
        self.redis_server.rpush('testlist', 1)
        result = self.redis_server.lpop('testlist')
        self.redis_server.rpush('testlist', 1)
        uresult = self.uredis_client.lpop('testlist')
        self.assertEqual(uresult, result)

    def test_rpop_empty(self, *args):
        result = self.redis_server.rpop('testlist')
        uresult = self.uredis_client.rpop('testlist')
        self.assertEqual(uresult, result)

    def test_rpop(self, *args):
        self.redis_server.rpush('testlist', 1)
        result = self.redis_server.rpop('testlist')
        self.redis_server.rpush('testlist', 1)
        uresult = self.uredis_client.rpop('testlist')
        self.assertEqual(uresult, result)

    def test_rpoplpush_empty(self, *args):
        result = self.redis_server.rpoplpush('testlist', 'testlistdest')
        uresult = self.uredis_client.rpoplpush('utestlist', 'utestlistdest')
        self.assertEqual(uresult, result)

    def test_rpoplpush(self, *args):
        self.redis_server.rpush('testlist', 1)
        result = self.redis_server.rpoplpush('testlist', 'testlistdest')
        self.redis_server.rpush('utestlist', 1)
        uresult = self.uredis_client.rpoplpush('utestlist', 'utestlistdest')
        self.assertEqual(uresult, result)

    # Todo
    # def test_lindex(self, *args):
    # def test_linsert(self, *args):
    # def test_llen(self, *args):
    # def test_lpush(self, *args):
    # def test_lpushx(self, *args):
    # def test_lrange(self, *args):
    # def test_lrem(self, *args):
    # def test_lset(self, *args):
    # def test_ltrim(self, *args):
    # def test_rpush(self, *args):
    # def test_rpushx(self, *args):


if __name__ == '__main__':
    logger = logging.getLogger('redislite')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    main()
