import pytest


def inc(x):
    return x + 1


def test_answer_1():
    assert inc(3) == 5


def test_answer_2(foo):
    print(foo)
    assert inc(98) == foo


if __name__ == '__main__':
    pytest.main()