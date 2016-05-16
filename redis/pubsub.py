from .client import Client


class RedisPubSub(Client):
    def psubscribe(self, *args):
        return self.execute_command('PSUBSCRIBE', *args)

    def pubsub(self, *args):
        return self.execute_command('PUBSUB', *args)

    def publish(self, *args):
        return self.execute_command('PUBLISH', *args)

    def punsubscribe(self, *args):
        return self.execute_command('PUNSUBSCRIBE', *args)


    def psubscribe(self, *args):
        return self.execute_command('PSUBSCRIBE', *args)

    def subscribe(self, *args):
        return self.execute_command('SUBSCRIBE', *args)

    def unsubscribe(self, *args):
        return self.execute_command('UNSUBSCRIBE', *args)
