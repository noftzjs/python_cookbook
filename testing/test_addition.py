import addition
import pytest

def test_add():
    assert addition.add(4, 5) == 9

def test_sub():
    assert addition.sub(4, 5) == -2
    #pass will just pass the test

    #::function_name at the end of the script will run just that function