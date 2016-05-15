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


base_redis_command = """import json
import sys
sys.path.insert(0, '{cwd}')
from redis import Redis
r=Redis(port={port})
result = None
{command}
r.set('command_result', json.dumps(result))
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
            result += '%4.4d:%s\n' % (count, line.strip())
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
                print(error.output)
                raise error('Micropython command failed')
            result = json.loads(self.redis_server.get('command_result').decode())
            return result

    def test_lrange_empty_list(self):
        command = self.generate_redis_script('result = r.lrange("testlist", 0, -1)')
        micropython_result = self.micropythonRun(command)
        redis_py_result = self.redis_server.lrange('testlist2', 0, -1)
        self.assertEqual(micropython_result, redis_py_result)

    def test_blpop_empty_list_with_timeout(self):
        command = self.generate_redis_script('result = r.blpop("testlist", timeout=1)')
        micropython_result = self.micropythonRun(command)
        redis_py_result = self.redis_server.blpop('testlist2', timeout=1)
        self.assertEqual(micropython_result, redis_py_result)

    def test_lpush_new_list_integer_value(self):
        command = self.generate_redis_script('result = r.lpush("testlist", 1)')
        micropython_result = self.micropythonRun(command)
        redis_py_result = self.redis_server.lpush('testlist2', 1)
        self.assertEqual(micropython_result, redis_py_result)
        result = self.redis_server.lrange('testlist', 0, -1)
        self.assertEqual(result, [b'1'])


if __name__ == '__main__':
    main()
