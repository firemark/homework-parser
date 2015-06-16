class AbstractPlugin(object):

    @staticmethod
    def read_from_file(raw_data):
        raise NotImplementedError('read_to_file')

    @staticmethod
    def write_to_file():
        raise NotImplementedError('write_to_file')

