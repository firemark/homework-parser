class AbstractPlugin(object):

    @staticmethod
    def read_from_file(stream):
        raise NotImplementedError('read_to_file')

    @staticmethod
    def write_to_file(stream, data):
        raise NotImplementedError('write_to_file')

