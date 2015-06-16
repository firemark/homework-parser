from plugin import AbstractPlugin
from file_parser import detect_plugin
from cStringIO import StringIO

import pytest


def test_detect_plugin():
    plugin = detect_plugin('foo')
    assert plugin.__name__ == 'FooPlugin'
    assert issubclass(plugin, AbstractPlugin)
    

def test_detect_unknown_plugin():
    plugin = detect_plugin('foobar')
    assert plugin is None


def test_load_json():
    plugin = detect_plugin('json')
    stream = StringIO(
        '[{"a": 0, "b": 1}, {"a": 0, "b": 1}]'
    )
    data = plugin.read_from_file(stream)
    assert data == [{"a": 0, "b": 1}, {"a": 0, "b": 1}]


def test_write_json():
    plugin = detect_plugin('json')
    data = [{"a": 0, "b": 1}, {"a": 0, "b": 1}]
    stream = StringIO()
    plugin.write_to_file(stream, data)
    assert stream.getvalue() == (
        '[{"a": 0, "b": 1}, {"a": 0, "b": 1}]'
    )

def test_load_uri():
    plugin = detect_plugin('uri')
    stream = StringIO(
        'a=0&b=1\na=0&b=1'
    )
    data = plugin.read_from_file(stream)
    assert data == [{"a": '0', "b": 1}, {"a": '0', "b": '1'}]


def test_write_uri():
    plugin = detect_plugin('uri')
    data = [{"a": 0, "b": 1}, {"a": 0, "b": 1}]
    stream = StringIO()
    plugin.write_to_file(stream, data)
    assert stream.getvalue() == (
        'a=0&b=1\na=0&b=1\n'
    )
    
