from importlib import import_module


def detect_plugin(name):
    module_name = 'homework_parser.plugins.%s' % name #todo modules from another project
    try:
        module = import_module(module_name)
    except ImportError:
        return None
    return getattr(module, '%sPlugin' % name.capitalize(), None) 

