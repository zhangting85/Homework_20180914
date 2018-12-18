import pytest

@pytest.fixture(scope="function",autouse=True)
def foo():
    print(" function setup")
    yield 100
    print(" function teardown")