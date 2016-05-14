from .client import Client


class RedisKeys(Client):
    def get(self, *args):
        return self.execute_command('GET', *args)

    def keys(self, *args):
        if not args:
            args = ['*']
        return self.execute_command('KEYS', *args)

    def set(self, *args):
        if self.execute_command('SET', *args) in [b'OK']:
            return True
        return False
