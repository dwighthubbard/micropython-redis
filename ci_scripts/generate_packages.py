#!/usr/bin/env python
import argparse
import contextlib
import os
import subprocess
import sys


@contextlib.contextmanager
def change_directory(path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)


def setup_in_directory(path, setup_arguments=[]):
    if not setup_arguments:
        setup_arguments = ['sdist']
    with change_directory(path):
        subprocess.check_call(
            [
                sys.executable,
                './setup.py'
            ] + setup_arguments
        )
        for f in os.listdir('dist'):
            filename = os.path.join('dist', f)
            dest_filename = os.path.join('../dist', f)
            if filename.endswith('.tar.gz'):
                print('Renaming: %r->%r' % (filename, dest_filename))
                os.rename(filename, dest_filename)


def setup_packages(setup_arguments=None):
    if not setup_arguments:
        setup_arguments = ['sdist']
    for directory in os.listdir('.'):
        if directory.startswith('redis.') or directory in ['uredis']:
            setup_in_directory(directory, setup_arguments=setup_arguments)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--setup_argument', nargs='*', default=['sdist'])
    args = parser.parse_args()
    setup_packages(setup_arguments=args.setup_argument)
