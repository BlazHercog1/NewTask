import main

def test_add():
    assert main.add(2, 2) == 4
    assert main.add(5, 2) == 7

def test_pow():
    assert main.power(2, 2) == 4
    assert main.power(200, 1) == 200

def test_divide():
    assert main.divide(10, 2) == 5
    assert main.divide(15, 5) == 3
    assert main.divide(10, 0) == "Error: Division by zero"