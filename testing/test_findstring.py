# from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent('AL')

def test_nodigit():
    assert findstring.nodigit("N7")