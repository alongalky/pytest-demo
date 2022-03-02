import pytest


def add(x, y):
    return x + y


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0.3, 0.3, 0.6),
    ],
)
def test_add(x, y, expected_result):
    assert add(x, y) == expected_result
