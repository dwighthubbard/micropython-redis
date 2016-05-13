#!/usr/local/bin/micropython
"""
Redis Client for embedded python environments
"""
import logging
import socket
try:
    import ssl
    ssl_support = True
except ImportError:
    ssl_support = False


logger = logging.getLogger(__name__)


class RedisError(Exception):
    pass


class InvalidResponse(RedisError):
    pass


class ConnectionError(Exception):
    pass



class Connection(object):
    def __init__(self, host=None, port=6379, use_ssl=False, timeout=10):
        """
        Redis Server Connection

        Parameters
        ----------
        host : str, optional
            Hostname or IP address of the redis server, default='localhost'

        port : int, optional
            Port number of the redis server, default=6379

        use_ssl : bool, optional
            Use SSL for the connection, default=False

        timeout : int, optional
            Socket timeout in seconds, default=10
        """
        if not host:
            host = '127.0.0.1'

        self.host = host
        self.port = int(port)

        # self.host = socket.gethostbyname(host)
        # except socket.gaierror:
        #     raise ConnectionError('DNS Lookup failed')

        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.socket.settimeout(timeout)
        self.socket = socket.socket()
        self.socket.connect(socket.getaddrinfo(self.host, self.port)[0][-1])

        if ssl_support and use_ssl:
            self.socket = ssl.wrap_socket(self.socket)


    def disconnect(self):
        self.socket.close()

    def send_command(self, command, *args):
        com = command.encode()
        for arg in args:
            com += b' '
            if isinstance(arg, str):
                com += repr(arg).encode()
            else:
                com += arg
        com += b'\r\n'
        logger.debug('command: ' + com.decode().strip())
        self.socket.send(com)

    def readline(self):
        line_buffer = b''
        c = self.socket.recv(1)
        while c:
            line_buffer += c
            try:
                if line_buffer and line_buffer[-2:] == b'\r\n':
                    break
            except IndexError:
                pass
            c = self.socket.recv(1)
        return line_buffer


class Redis(object):
    def __init__(self, host=None, port=6379):
        if not host:
            host = 'localhost'
        self.connection = Connection(host, port)

    def execute_command(self, command, *args):
        self.connection.send_command(command, *args)
        return self.get_response()

    def get_response(self):
        response = self.connection.readline()
        response_type = response[:1].decode()
        response_value = response[1:-2]
        if response_type == '+':
            return response[1:-2]
        elif response_type == '-':
            raise RedisError(response[1:-2])
        elif response_type == ':':
            return int(response[1:-2])
        elif response_type == '$':
            length = int(response_value)
            bulk_string = self.connection.socket.recv(length)
            self.connection.readline()
            return bulk_string
        elif response_type == '*':
            return [self.get_response() for item in range(int(response_value))]
        else:
            raise InvalidResponse('Protocol Error: %s' % response.decode())

    def blpop(self, *args):
        return self.execute_command('BLPOP', *args)

    def get(self, *args):
        return self.execute_command('GET', *args)

    def keys(self, *args):
        return self.execute_command('KEYS', *args)

    def lset(self, *args):
        return self.execute_command('LSET', *args)

    def save(self):
        return self.execute_command('SAVE')

    def set(self, *args):
        if self.execute_command('SET', *args) in [b'OK']:
            return True
        return False


if __name__ == '__main__':
    r = Redis('localhost', 6666)
    # print(r.keys('*'))
    # print(r.set('key1', 'value1'))
    # print(r.get('key1'))
    r.lset('testlist', "0", 'foo')
    print(r.keys('*'))