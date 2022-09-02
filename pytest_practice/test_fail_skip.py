import pytest
'''
If we mark test as xfail it will not be considered in pass as well as fail
and nothing will be printed 
For test marked with skip, the tests will be skipped
'''



@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

