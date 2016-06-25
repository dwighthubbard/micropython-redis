from .client import Client


class String(Client):

    def append(self, *args):
        return self.execute_command('APPEND', *args)

    def bitcount(self, *args):
        return self.execute_command('BITCOUNT', *args)

    def bitfield(self, *args):
        return self.execute_command('BITFIELD', *args)

    def bitop(self, *args):
        return self.execute_command('BITOP', *args)

    def bitpos(self, *args):
        return self.execute_command('BITPOS', *args)

    def decr(self, *args):
        return self.execute_command('DECR', *args)

    def DECRBY(self, *args):
        return self.execute_command('DECRBY', *args)

    def get(self, *args):
        return self.execute_command('GET', *args)

    def getbit(self, *args):
        return self.execute_command('GETBET', *args)

    def getrange(self, *args):
        return self.execute_command('GETRANGE', *args)

    def getset(self, *args):
        return self.execute_command('GETSET', *args)

    def incr(self, *args):
        return self.execute_command('INCR', *args)

    def incrby(self, *args):
        return self.execute_command('INCRBY', *args)

    def incrbyfloat(self, *args):
        return self.execute_command('incrbyfloat', *args)

    def mget(self, *args):
        return self.execute_command('MGET', *args)

    def mset(self, *args):
        return self.execute_command('MSET', *args)

    def msetnx(self, *args):
        return self.execute_command('MSETNX', *args)

    def psetex(self, *args):
        return self.execute_command('PSETEX', *args)

    def set(self, *args):
        return self.execute_command('SET', *args)

    def setbit(self, *args):
        return self.execute_command('SETBIT', *args)

    def setex(self, *args):
        return self.execute_command('SETEX', *args)

    def setnx(self, *args):
        return self.execute_command('SETNX', *args)

    def setrange(self, *args):
        return self.execute_command('SETRANGE', *args)

    def strlen(self, *args):
        return self.execute_command('STRLEN', *args)
