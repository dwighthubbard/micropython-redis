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
    redis_test_port = 7904

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': self.redis_test_port})
        self.uredis_client = uredis.Redis(host='127.0.0.1', port=self.redis_test_port)

    def tearDown(self):
        self.redis_server.shutdown()


if __name__ == '__main__':
    logger = logging.getLogger('redislite')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    main()
