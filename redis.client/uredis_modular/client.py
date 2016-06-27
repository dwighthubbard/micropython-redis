#!/usr/local/bin/micropython
"""
Redis Client for embedded python environments
"""
class RedisError(Exception):
    pass


class InvalidResponse(RedisError):
    pass


class ConnectionError(Exception):
    pass

class Unsupported(Exception):
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
        try:
            import usocket as socket
        except ImportError
            import socket

        if not host:
            host = '192.168.4.2'

        self.host = host
        self.port = int(port)

        self.socket = socket.socket()
        self.socket.connect(socket.getaddrinfo(self.host, self.port)[0][-1])

        if use_ssl:
            try:  # pragma: no cover
                import ssl
                self.socket = ssl.wrap_socket(self.socket)
            except ImportError:  # pragma: no cover
                raise Unsupported('SSL support is not available')

    def disconnect(self):
        self.socket.close()

    def send_command(self, command, *args):
        self.socket.send(command.encode())
        for arg in args:
            self.socket.send(b' ')
            if isinstance(arg, str):
                self.socket.send(repr(arg).encode())
            else:
                self.socket.send(repr(arg))
        self.socket.send(b'\r\n')

    def readline(self):
        line_buffer = b''
        c = self.socket.recv(1)
        while c:
            line_buffer += c
            try:
                if len(line_buffer) > 1 and line_buffer[-2:] == b'\r\n':
                    break
            except IndexError:
                pass
            c = self.socket.recv(1)
        return line_buffer


class Client(object):
    def __init__(self, host=None, port=6379, password=None):
        if not host:
            host = '192.168.4.2'
        self.connection = Connection(host, port)

        if password:
            self.connection.send_command('AUTH', password)

    def send_redis_array_string(self, items):
        """
        Send a redis array string

        Parameters
        ----------
        items : list
            The items to be in the redis array string

        Returns
        -------
        bytes
            Redis RESP bytestream representation of the array
        """

        self.connection.socket.send(b'*')
        self.connection.socket.send(str(len(items)).encode())
        self.connection.socket.send(b'\r\n')

        # Add each element to the stream in turn
        for item in items:
            item_bytestream = self.convert_to_bytestream(item)

            # Add the item length to the stream
            self.connection.socket.send(b'$')
            self.connection.socket.send(str(len(item_bytestream)).encode())
            self.connection.socket.send(b'\r\n')
            self.connection.socket.send(item_bytestream)
            self.connection.socket.send(b'\r\n')

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
            if length == -1:
                return None
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
        self.send_redis_array_string(args)

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
