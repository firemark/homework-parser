from plugin import AbstractPlugin
from file_parser import detect_plugin

import pytest


def test_detect_plugin():
    plugin = detect_plugin('foo')
    assert plugin.__name__ == 'FooPlugin'
    assert issubclass(plugin, AbstractPlugin)
    

def test_detect_unknown_plugin():
    plugin = detect_plugin('foobar')
    assert plugin is None

