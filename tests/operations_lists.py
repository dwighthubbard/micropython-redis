#!/usr/bin/env python3
"""
Tests to validate redis list functionality is working properly with micropython
"""
# Notes:
#
# 1. These tests should be run with a cpython interpreter with the redislite module installed.
# 2. The micropython executable should be accesible in the path.
import os
import redislite
import subprocess
import tempfile
from unittest import main, TestCase


base_redis_command = """import sys
sys.path.insert(0, '{cwd}')
from redis.redis import Redis
r=Redis(port={port})
{command}
"""

class TestRedisListOperations(TestCase):
    redis_test_port = 7899
    micropython_executable = 'micropython'

    def setUp(self):
        self.redis_server = redislite.Redis(serverconfig={'port': 7899})

    def tearDown(self):
        self.redis_server.shutdown()

    def generate_redis_script(self, command):
        return base_redis_command.format(
            cwd=os.getcwd(),
            port=self.redis_test_port,
            command=command
        )

    def add_line_numbers(self, output):
        result = ''
        count = 1
        for line in output.split('\n'):
            result += '%4.4d:%s' % (count, line.strip())
            count += 1
        return result

    def micropythonRun(self, commands):
        """
        Execute commands using the micropython interpreter

        Parameters
        ----------
        commands : str
            The commands to run with micropython
        """
        with tempfile.NamedTemporaryFile(suffix='.py') as script_file_handle:
            script_file_handle.write(commands.encode())
            script_file_handle.flush()
            try:
                subprocess.check_call(
                    [
                        self.micropython_executable,
                        script_file_handle.name
                    ]
                )
            except subprocess.CalledProcessError as error:
                print(self.add_line_numbers(commands))
                raise error('Micropython command failed')


    def test_lpush_new_list_integer_value(self):
        command = """import sys
sys.path.insert(0, '{cwd}')
from redis.redis import Redis
r=Redis(port={port})
r.lpush("testlist", 1)""".format(
            port=self.redis_test_port, cwd=os.getcwd()
        )
        command = self.generate_redis_script('r.lpush("testlist", 1)')
        self.micropythonRun(command)

        result = self.redis_server.lrange('testlist', 0, -1)
        self.assertEqual(result, [b'1'])


if __name__ == '__main__':
    main()
