from .client import Client


class Key(Client):
    def delete(self, *args):
        return self.execute_command('DEL', *args)

    def dump(self, *args):
        return self.execute_command('DUMP', *args)

    def exists(self, *args):
        return self.execute_command('EXISTS', *args)

    def expire(self, *args):
        return self.execute_command('EXPIRE', *args)

    def expireat(self, *args):
        return self.execute_command('EXPIREAT', *args)

    def get(self, *args):
        return self.execute_command('GET', *args)

    def keys(self, *args):
        if not args:
            args = ['*']
        return self.execute_command('KEYS', *args)

    def migrate(self, *args):
        return self.execute_command('MIGRATE', *args)

    def move(self, *args):
        return self.execute_command('MOVE', *args)

    def object(self, *args):
        return self.execute_command('OBJECT', *args)

    def persist(self, *args):
        return self.execute_command('PERSIST', *args)

    def pexpire(self, *args):
        return self.execute_command('PEXPIRE', *args)

    def pttl(self, *args):
        return self.execute_command('PTTL', *args)

    def randomkey(self, *args):
        return self.execute_command('RANDOMKEY', *args)

    def rename(self, *args):
        return self.execute_command('RENAME', *args)

    def renamenx(self, *args):
        return self.execute_command('RENAMENX', *args)

    def restore(self, *args):
        return self.execute_command('RESTORE', *args)

    def scan(self, *args):
        return self.execute_command('SCAN', *args)

    def set(self, *args):
        if self.execute_command('SET', *args) in [b'OK']:
            return True
        return False

    def sort(self, *args):
        return self.execute_command('SORT', *args)

    def ttl(self, *args):
        return self.execute_command('TTL', *args)

    def type(self, *args):
        return self.execute_command('TYPE', *args)

    def wait(self, *args):
        return self.execute_command('WAIT', *args)
