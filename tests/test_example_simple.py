"""
`pytest` will run all files with test_*.py and *_test.py in current and subdirectories.
More information: https://docs.pytest.org/en/8.0.x/explanation/goodpractices.html#test-discovery
"""
import pytest

# This function won't count as a test case
def some_function():
    raise ValueError(f"Hey!! Value ERROR")

# This is the test case
def test_some_function_return_ValueError():
    # Expect that the function will raise `ValueError`
    with pytest.raises(ValueError):
        some_function()


# Define test case as a class
# Class name must start with `Test*`
class TestExample:
    # Same, this won't count as a test case
    def some_function(self):
        raise SystemError(f"Hey!! System ERROR")
    
    # This is a test case
    def test_some_function_return_SystemError(self):
        # Expect that the funciton will raise `SystemError`
        with pytest.raises(SystemError):
            self.some_function()

    def test_case_addition_1_1_equal_2(self):
        ans = 1 + 1
        assert 2 == ans, f"1 + 1 must be 2. Got {ans=}"

    ### Dependency: https://pypi.org/project/pytest-depends/ ### 
    # Sometime, some test case will surely fail if one of the test case is fail.
    # We call this, dependency.
        
    # Here, we create alias name as `a`
    @pytest.mark.depends(name="a")
    def test_a(self):
        # In the summary, it will show 1 failed
        assert True == False, f"This will fail"
    
    # Refer to the depen class using function name
    @pytest.mark.depends(on=['test_a'])
    def test_depend_on_a_real_name(self):
        # In this summary, it will show 2 skipped
        assert True == False, f"This will never run"
    
    # Refer to the depen class using function name
    @pytest.mark.depends(on=['a'])
    def test_depend_on_a_alias_name(self):
        # In this summary, it will show 2 skipped
        assert True == False, f"This will never run"