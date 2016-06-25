from .client import Client


class Hash(Client):
    def hdel(self, *args):
        return self.execute_command('HDEL', *args)

    def hexists(self, *args):
        return self.execute_command('HEXISTS', *args)

    def hget(self, *args):
        return self.execute_command('HGET', *args)

    def hgetall(self, *args):
        """"
        Returns all fields and values of the hash stored at key.

        Returns
        -------
        dict
            Dictionary of all key/values from the field
        """
        result_dict = {}
        result = self.execute_command('HGETALL', *args)
        for value in range(0, len(result), 2):
            result_dict[result[value]] = result[value+1]
        return result_dict

    def hincrby(self,  key, field, increment):
        """
        Increments the number stored at field in the hash stored at key by increment. If key does not exist, a new
        key holding a hash is created. If field does not exist the value is set to 0 before the operation is performed.

        The range of values supported by HINCRBY is limited to 64 bit signed integers.

        Parameters
        ----------
        key : str
            Hash key to increment

        field : str
            Hash field to increment

        increment : int
            Amount to increment

        Returns
        -------
        int
            The value at field after the increment operation.
        """
        return self.execute_command('HINCRBY', key, field, int(increment))

    def hincrbyfloat(self, *args):
        return float(self.execute_command('HINCRBYFLOAT', *args))

    def hkeys(self, *args):
        return self.execute_command('HKEYS', *args)

    def hlen(self, *args):
        return self.execute_command('HLEN', *args)

    def hmget(self, *args):
        return self.execute_command('HMGET', *args)

    def hset(self, *args):
        return self.execute_command('HSET', *args)

    def hsetnx(self, *args):
        return self.execute_command('HSETNX', *args)

    def hstrlen(self, *args):
        return self.execute_command('HSTRLEN', *args)

    def hvals(self, *args):
        return self.execute_command('HVALS', *args)

    def hscan(self, *args):
        return self.execute_command('HSCAN', *args)
