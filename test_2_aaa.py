def add(x, y):
    return x + y


def test_add():
    assert add(2, 3) == 5


def test_serious_add():
    # Arrange
    x = 2
    y = 3

    # Act
    result = add(x, y)

    # Assert
    assert result == 5
