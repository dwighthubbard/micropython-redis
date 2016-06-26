from .client import Client


class SortedSet(Client):

    def zadd(self, name, *args, **kwargs):
        """
        Set any number of score, element-name pairs to the key name. Pairs can be specified in two ways:

        As *args, in the form of: score1, name1, score2, name2

        Parameters
        ----------
        name : str
            Keyname of the list

        *args :
            Sequency of name,score values

        """
        new_args = [name]
        for index in range(0, len(args), 2):
            name = args[index]
            value = args[index+1]
            if isinstance(value, int):
                value = float(value)
            new_args.append(value)
            new_args.append(name)
        return self.execute_command('ZADD', *new_args)

    def zcard(self, *args):
        return self.execute_command('ZCARD', *args)

    def zcount(self, *args):
        return self.execute_command('ZCOUNT', *args)

    def zincrby(self, *args):
        return self.execute_command('ZINCRBY', *args)

    def zinterstore(self, *args):
        return self.execute_command('ZINTERSTORE', *args)

    def zlexcount(self, *args):
        return self.execute_command('ZLEXCOUNT', *args)

    def zrange(self, *args):
        return self.execute_command('ZRANGE', *args)

    def zrangebylex(self, *args):
        return self.execute_command('ZRANGEBYLEX', *args)

    def zrevrangebylex(self, *args):
        return self.execute_command('ZREVRANGEBYLEX', *args)

    def zrangebyscore(self, *args):
        return self.execute_command('ZRANGEBYSCORE', *args)

    def zrank(self, *args):
        return self.execute_command('ZRANK', *args)

    def zrem(self, *args):
        return self.execute_command('ZREM', *args)

    def zremrangebylex(self, *args):
        return self.execute_command('ZREMRANGEBYLEX', *args)

    def zremrangebyrank(self, *args):
        return self.execute_command('ZREMRANGEBYRANK', *args)

    def zremrangebyscore(self, *args):
        return self.execute_command('ZREMRANGEBYSCORE', *args)

    def zrevrange(self, *args):
        return self.execute_command('ZREVRANGE', *args)

    def zrevrangebyscore(self, *args):
        return self.execute_command('ZREVRANGEBYSCORE', *args)

    def zrevrank(self, *args):
        return self.execute_command('ZREVRANK', *args)

    def zscore(self, *args):
        return self.execute_command('ZSCORE', *args)

    def zunionstore(self, *args):
        return self.execute_command('ZUNIONSTORE', *args)

    def zscan(self, *args):
        return self.execute_command('ZSCAN', *args)
