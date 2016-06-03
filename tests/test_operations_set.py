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


class TestSetOperations(TestCase):
    redis_test_port = 7903

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': self.redis_test_port})
        self.uredis_client = uredis.Redis(host='127.0.0.1', port=self.redis_test_port)

    def tearDown(self):
        self.redis_server.shutdown()

    def test_sadd(self):
        result = self.redis_server.sadd("testset", 1)
        uresult = self.uredis_client.sadd("utestset", 1)
        self.assertEqual(uresult, result)

    def test_scard(self):
        result = self.redis_server.sadd("testset", 1)
        uresult = self.uredis_client.sadd("utestset", 1)
        result = self.redis_server.scard("testset")
        uresult = self.uredis_client.scard("utestset")
        self.assertEqual(uresult, result)

    def test_sdiff(self):
        result = self.redis_server.sadd("testset", 1, 2)
        result = self.redis_server.sadd("testset2", 2, 3)
        uresult = self.uredis_client.sadd("utestset", 1, 2)
        uresult = self.uredis_client.sadd("utestset2", 2, 3)

        result = self.redis_server.sdiff("testset", 'testset2')
        uresult = self.uredis_client.sdiff("utestset", 'utestset2')

        self.assertEqual(uresult, result)


if __name__ == '__main__':
    logger = logging.getLogger('redislite')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    main()
