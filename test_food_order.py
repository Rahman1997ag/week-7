import pytest
from food_order import food_order

def test_order1():
    """اختبار الإجمالي الصحيح 20"""
    assert food_order(10, 2) == 20

def test_order2():
    """اختبار الإجمالي الصحيح 30"""
    assert food_order(15, 2) == 30

def test_order3():
    """اختبار الإجمالي الصحيح 100"""
    assert food_order(25, 4) == 100

def test_order4():
    """اختبار الإجمالي الصحيح 10"""
    assert food_order(5, 2) == 10

def test_invalid_price():
    """اختبار السعر غير الصحيح (سلبي أو نص)"""
    assert food_order(-5, 2) == "invalid price"
    assert food_order("abc", 2) == "invalid price"   # نوع غير رقمي

def test_invalid_quantity():
    """اختبار الكمية غير الصحيحة (صفر، سالب، أو نص)"""
    assert food_order(10, 0) == "invalid quantity"
    assert food_order(10, -3) == "invalid quantity"
    assert food_order(10, "two") == "invalid quantity"  # نوع غير صحيح
