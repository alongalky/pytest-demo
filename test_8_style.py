from unittest.mock import patch
import pytest


def add(x, y):
    return x + y


@pytest.mark.parametrize("x, y",[(2,3), (-1, 1)])
def test_add_ugly_style(x, y):
    assert add(x, y) == x + y