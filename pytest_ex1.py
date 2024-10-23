import pytest
def fizzbuzz(n):
    if n<=0:
        raise ValueError ("value should be positive")
    elif n%3 ==0 and n%5==0:
        return "FizzBuzz"
    elif n%3 ==0:
        return "Fizz"
    elif n%5 ==0:
         return "Buzz"
    

def test_fizzbuzz():
    with pytest.raises(ValueError):
        fizzbuzz(-1)
    with pytest.raises(ValueError):
        fizzbuzz(0)
    assert fizzbuzz(9)=='Fizz'
    assert fizzbuzz(20)=="Buzz"
    assert fizzbuzz(15)=="FizzBuzz"