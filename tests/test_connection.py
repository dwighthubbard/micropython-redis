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

    def test_auth(self):
        redis_server = redislite.Redis(
            serverconfig={
                'requirepass': 'test',
                'port': self.redis_test_port+1
            },
            password='test'
        )


        # This shouldn't generate an exception
        redis_client = redis.Redis(host='127.0.0.1', port=self.redis_test_port+1, password='test')
        uredis_client = uredis.Redis(host='127.0.0.1', port=self.redis_test_port+1, password='test')

    def test_echo(self):
        result = self.redis_server.echo("test")
        uresult = self.uredis_client.echo("test")
        self.assertEqual(uresult, result)

    def test_ping(self):
        result = self.redis_server.ping()
        uresult = self.uredis_client.ping()
        self.assertEqual(uresult, result)

    def test_quit(self):
        uresult = self.uredis_client.quit()
        self.uredis_client.ping()  # This should fail since the server is now shutdown


if __name__ == '__main__':
    logger = logging.getLogger('redislite.client')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    main()
