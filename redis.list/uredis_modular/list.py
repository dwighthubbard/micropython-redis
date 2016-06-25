from .client import Client


class List(Client):
    """
    Redis Client with support for all Redis List operations
    """
    def blpop(self, *keys, timeout=0):
        """
        Remove and get the first element of a list or block until one is available

        Parameters
        ----------
        *keys
            Key or keys to get the first element from

        timeout : int, optional
            Maximum time to block waiting for the key, if not specified will wait forever.

        Returns
        -------
        First element from the list, or None
        """
        if timeout:
            keys = tuple(list(keys) + [timeout])
        result = self.execute_command('BLPOP', *keys)
        if result == []:
            return None
        return result

    def brpop(self, *keys, timeout=0):
        """
        Remove and get the last element of a list or block until one is available

        Parameters
        ----------
        *keys
            Key or keys to get the first element from

        timeout : int, optional
            Maximum time to block waiting for the key, if not specified will wait forever.

        Returns
        -------
        First element from the list, or None
        """
        if timeout:
            keys = tuple(list(keys) + [timeout])
        result = self.execute_command('BRPOP', *keys)
        if result == [] or result == ():
            return None
        return tuple(result)

    def brpoplpush(self, src, dst, timeout=0):
        """
        Remove and get the last element of a list and push it to the front of another list, blocking if there is no
        value to available.

        Parameters
        ----------
        src : str
            Key to pop the value from

        dst : str
            Key to prepend the value to

        timeout : int, optional
            Maximum time to block waiting for a key, if not specified or the value is 0, will wait forever.

        Returns
        -------
        bytes
            The bytestring of the value retrievied from the src
        """
        result = self.execute_command('BRPOPLPUSH', src, dst, timeout)
        if result == []:
            return None
        return result

    def lindex(self, *args):
        return self.execute_command('LINDEX', *args)

    def linsert(self, *args):
        return self.execute_command('LINSERT', *args)

    def llen(self, *args):
        return self.execute_command('LLEN', *args)

    def lpop(self, *args):
        return self.execute_command('LPOP', *args)

    def lpush(self, *args):
        return self.execute_command('LPUSH', *args)

    def lpushx(self, *args):
        return self.execute_command('LPUSHX', *args)

    def lrange(self, *args):
        return self.execute_command('LRANGE', *args)

    def lrem(self, *args):
        return self.execute_command('LREM', *args)

    def lset(self, *args):
        return self.execute_command('LSET', *args)

    def ltrim(self, *args):
        return self.execute_command('LTRIM', *args)

    def rpop(self, name):
        """
        Remove and get the last element of a list

        Parameters
        ----------
        name : str
            Key to pop the value from

        Returns
        -------
        bytes
            The bytestring of the value retrievied from the src
        """
        return self.execute_command('RPOP', name)

    def rpoplpush(self, *args):
        return self.execute_command('RPOPLPUSH', *args)

    def rpush(self, *args):
        return self.execute_command('RPUSH', *args)

    def rpushx(self, *args):
        return self.execute_command('RPUSHX', *args)
