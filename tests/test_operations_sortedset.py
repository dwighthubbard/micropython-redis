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


class TestSortedSetOperations(TestCase):
    redis_test_port = 7905

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': self.redis_test_port})
        self.uredis_client = uredis.Redis(host='127.0.0.1', port=self.redis_test_port)

    def tearDown(self):
        self.redis_server.shutdown()

    def test_zadd(self):
        result = self.redis_server.zadd("testset", 'one', 1)
        uresult = self.uredis_client.zadd("utestset", 'one', 1)
        self.assertEqual(uresult, result)

    def test_zcard(self):
        result = self.redis_server.zadd("testset", 'one', 1)
        uresult = self.uredis_client.zadd("utestset", 'one', 1)
        result = self.redis_server.zcard("testset")
        uresult = self.uredis_client.zcard("utestset")
        self.assertEqual(uresult, result)


if __name__ == '__main__':
    logger = logging.getLogger('redislite')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    main()
