import pytest

from app import inc

def test_inc_pos():
    assert inc(3) == 4

def test_inc_neg():
    assert inc(-1) == 0

def test_inc_zero():
    assert inc(0) == 1
