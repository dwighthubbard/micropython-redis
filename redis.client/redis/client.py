#!/usr/local/bin/micropython
"""
Redis Client for embedded python environments
"""
import socket
try:
    import ssl
    ssl_support = True
except ImportError:
    ssl_support = False


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
                com += repr(arg)
        com += b'\r\n'
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
        print(line_buffer)
        return line_buffer


class Client(object):
    def __init__(self, host=None, port=6379):
        if not host:
            host = 'localhost'
        self.connection = Connection(host, port)

    def create_redis_array_string(self, items):
        """
        Generate a redis array string

        Parameters
        ----------
        items : list
            The items to be in the redis array string

        Returns
        -------
        bytes
            Redis RESP bytestream representation of the array
        """
        stream = '*{0}\r\n'.format(len(items)).encode()

        # Add each element to the stream in turn
        for item in items:
            item_bytestream = self.convert_to_bytestream(item)

            # Add the item length to the stream
            stream += b'$' + str(len(item_bytestream)).encode() + b'\r\n'

            # Now add the data
            stream += item_bytestream + b'\r\n'

        return stream

    def execute_command(self, command, *args):
        self.run_command(command, *args)
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

    def run_command(self, command, *args):
        # self.connection.send_command(command, *args)
        args = [command] + list(args)
        bytestream = self.create_redis_array_string(args)
        self.connection.socket.send(bytestream)

    def convert_to_bytestream(self, value):
        """
        Return a bytestream of the value

        Parameters
        ----------
        value

        Returns
        -------
        bytes
            A bytestream of the value
        """
        try:
            if isinstance(value, float):
                return repr(value).encode()
        except NameError:
            # Platform doesn't support floating point
            pass
        if isinstance(value, bytes):
            return value
        elif isinstance(value, int):
            return str(value).encode()
        elif isinstance(value, str):
            return value.encode()
        return str(value).encode()

    def save(self):
        return self.execute_command('SAVE')
