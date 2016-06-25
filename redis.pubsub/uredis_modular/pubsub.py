from .client import Client


class PubSub(Client):
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
        for channel in args[1:]:
            self.run_command('SUBSCRIBE', channel)
        while True:
            self.get_response()

    def unsubscribe(self, *args):
        return self.execute_command('UNSUBSCRIBE', *args)
