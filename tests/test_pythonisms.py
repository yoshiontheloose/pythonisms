import py
import pytest
from pythonisms.generator import Stack, Node

from pythonisms import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_for_in():
    cats = Stack(("Tifa","Beans","Meow"))
    cats_list = []
    for cat in cats:
        cats_list.append(cat)
    assert cats_list == ["Tifa","Beans","Meow"]

def test_list_comprehension():
    cats = Stack(("Tifa","Beans","Meow"))
    cats_list = [cat.upper() for cat in cats]
    assert cats_list == ["TIFA","BEANS","MEOW"]
