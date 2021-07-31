def add(x,y):
    return x+y

def test_add():
    total = add(1,2)
    assert total == 3    

def square(x):
    return x * x    

def test_square():
    result = square(2)
    assert result== 4