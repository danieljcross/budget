'''
Test the functionality of the budget program
Author: Elf Fire Hydrant Group
'''
from budget import after, spring_income_25
import pytest

def test_after():
    assert after == -1600

def test_spring_income_25():
    assert spring_income_25 == 2500



pytest.main(["-v", "--tb=line", "-rN", __file__])
