from homework_parser.plugin import AbstractPlugin


class FooPlugin(AbstractPlugin):

    @staticmethod
    def read_from_file(stream):
        pass

    @staticmethod
    def write_to_file(stream, data):
        pass

