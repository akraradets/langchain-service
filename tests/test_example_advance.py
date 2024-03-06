"""
Now that you are interested in designing test script, start from reading this https://docs.pytest.org/en/latest/explanation/anatomy.html#test-anatomy.
In this advance, we take a look at `fixture`: https://docs.pytest.org/en/latest/explanation/fixtures.html#about-fixtures.
"""
import pytest
import time

### Caching result: https://docs.pytest.org/en/latest/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session ###
@pytest.fixture(scope="module")
def result():
    ans = 1 + 1
    # Simulate the time takes to calculate result
    time.sleep(3)
    return ans

# Although, we call result twice, the result only calculate once.
# This is because we set the life time of the fixture as `module`.
# The `result` fixture will exist without recalculating in this file (module)
def test_result_pass(result):
    assert result == 2

def test_result_fail(result):
    assert result != 3


# Here we show that the scope `class` will make the fixture recalculate every new class
@pytest.fixture(scope="class")
def result_2():
    ans = 2 + 2
    # Simulate the time takes to calculate result
    time.sleep(3)
    return ans

class TestClassOne:
    def test_result_2_1(self, result_2):
        assert result_2 == 4
    
    def test_result_2_2(self, result_2):
        assert result_2 == 4

class TestClassTwo:
    def test_result_2_3(self, result_2):
        assert result_2 == 4