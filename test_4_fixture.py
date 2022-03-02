from dataclasses import dataclass
import pytest


@dataclass
class Food:
    name: str
    origin: str
    vegan: bool
    tasty: bool


@pytest.fixture
def banana():
    return Food(
        name="Banana",
        origin="Southeast Asia, probably the Philippines",
        vegan=True,
        tasty=True,
    )


def test_banana_is_tasty(banana):
    assert banana.tasty


def test_banana_is_not_tasty(banana):
    banana.tasty = False

    assert not banana.tasty
