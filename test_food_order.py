import pytest
from food_order import food_order

def test_order1():
    assert food_order(10, 2) == 20

def test_order2():
    assert food_order(15, 2) == 30

def test_order3():
    assert food_order(25, 4) == 100

def test_order4():
    assert food_order(5, 2) == 10

def test_invalid_price():
    assert food_order(-5, 2) == "invalid price"
    assert food_order("abc", 2) == "invalid price"   
def test_invalid_quantity():
    assert food_order(10, 0) == "invalid quantity"
    assert food_order(10, -3) == "invalid quantity"
    assert food_order(10, "two") == "invalid quantity"  
