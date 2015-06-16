from __future__ import absolute_import
from homework_parser.plugin import AbstractPlugin

import json


class JsonPlugin(AbstractPlugin):

    @staticmethod
    def read_from_file(stream):
        return json.load(stream)

    @staticmethod
    def write_to_file(stream, data):
        json.dump(data, stream)

