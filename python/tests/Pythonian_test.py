import pytest

import Caculate
#import use actual file name 
from Pythonian import *
from Pythonian import Calculate
from Pythonian import addArray

#import somefile
#from somefile import *
#from somefile import className 

def test_it_is_callable():
	assert callable(Calculate)
	assert callable(addArray)
	
test = [5, 5, 5, 5, 5]

def test_size5_with_5_5_5_5_5_input():
	assert addArray(test) == "The total is 25.00"
	
def test_Calculate_size_5_input_5_5_5_5_5():
	bomb = Calculate()
	assert addArray(bomb.list1) == "The total is 25.00"