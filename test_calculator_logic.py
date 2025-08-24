import calculator_logic as c
import pytest
def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1,1) == 0
    assert c.add(-1,-1) == -2

    with pytest.raises(TypeError):
        c.add(10, "5")
    with pytest.raises(TypeError):
        c.add("10", 5)
        


def test_subtract():
    assert c.subtract(10, 5) == 5
    assert c.subtract(-1,1) == -2
    assert c.subtract(-1,-1) == 0

    with pytest.raises(TypeError):
        c.subtract(10, "5")
    with pytest.raises(TypeError):
        c.subtract("10", 5)

def test_multiply():
    assert c.multiply(10, 5) == 50
    assert c.multiply(-1,1) == -1
    assert c.multiply(-1,-1) == 1


def test_divide():
    assert c.divide(10, 5) == 2
    assert c.divide(-1,1) == -1
    assert c.divide(-1,-1) == 1

    with pytest.raises(TypeError):
        c.divide(10, "5")
    with pytest.raises(TypeError):
        c.divide("10", 5)  

    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)

def test_square():
    for i in range(10):
        assert c.square(i) == i ** 2
        assert c.square(-i) == i ** 2
        assert c.square(0) == 0
        assert c.sqrt(i) == i ** 0.5
        assert c.sqrt(-i) == i ** 0.5
    with pytest.raises(ValueError):
        c.square("a")
        

                


test_add()
test_divide()
test_multiply(  )
test_subtract(  )


print("тест пройден успешно")


