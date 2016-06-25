from .client import Client


class Connection(Client):
    def auth(self, password):  # pragma: no cover
        """
        Authenticate to the server

        Parameters
        ----------
        password : str
            The password to authenticate with
        """
        return self.execute_command('AUTH', password)

    def echo(self, *args):
        """Echo the given string

        Parameters
        ----------
        message : str
            The string to echo
        """
        return self.execute_command('ECHO', *args)

    def ping(self, *args):
        """Ping the server"""
        try:
            result = self.execute_command('PING', *args)
        except:
            result = None

        if result == b'PONG':
            return True
        return False

    def select(self, *args):  # pragma: no cover
        """
        Change the selected database

        Parameters
        ----------
        index : int
            The redis database number to switch to
        """
        return self.execute_command('SELECT', *args)

    def quit(self, *args):
        """Close the connection"""
        return self.execute_command('QUIT', *args)