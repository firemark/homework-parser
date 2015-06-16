from homework_parser.plugin import AbstractPlugin

from urllib import urlencode
from urlparse import parse_qs


class UriPlugin(AbstractPlugin):

    @classmethod
    def read_from_file(cls, stream):
        return [
            {key: value[0] for key, value in parse_qs(line).items()}
            for line in cls.readlines(stream)
        ]

    @staticmethod
    def write_to_file(stream, data):
        for single_data in data:
            stream.write('%s\n' % urlencode(single_data))

    @staticmethod
    def readlines(stream):
        while True: # don't use readlines for very big files
            line = stream.readline()
            if not line:
                break
            yield line.strip()
