from .client import Client


class Set(Client):
    def sadd(self, *args):
        return self.execute_command('SADD', *args)

    def scard(self, *args):
        return self.execute_command('SCARD', *args)

    def sdiff(self, *args):
        return set(self.execute_command('SDIFF', *args))

    def sdiffstore(self, *args):
        return self.execute_command('SDIFFSTORE', *args)

    def sinter(self, *args):
        return self.execute_command('SINTER', *args)

    def sinterstore(self, *args):
        return self.execute_command('SINTERSTORE', *args)

    def sismember(self, *args):
        return self.execute_command('SISMEMBER', *args)

    def smembers(self, *args):
        return self.execute_command('SMEMBERS', *args)

    def smove(self, *args):
        return self.execute_command('SMOVE', *args)

    def spop(self, *args):
        return self.execute_command('SPOP', *args)

    def srandmember(self, *args):
        return self.execute_command('SRANDMEMBER', *args)

    def srem(self, *args):
        return self.execute_command('SREM', *args)

    def sunion(self, *args):
        return self.execute_command('SUNION', *args)

    def sunionstore(self, *args):
        return self.execute_command('SUNIONSTORE', *args)

    def sscan(self, *args):
        return self.execute_command('SCAN', *args)
