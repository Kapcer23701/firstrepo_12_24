from kod import *


def test_fizzbuzz_basic():
    assert fizzbus(1) == 1
    #assert fizzbus(2) == 1
    assert fizzbus(3) == 'Fizz'
    assert fizzbus(6) == 'Fizz'
    assert fizzbus(9) == 'Fizz'


def test_fizzbuss_buzz():
    assert fizzbus(5) == 'Buzz'
    assert fizzbus(10) == 'Buzz'
    assert fizzbus(35) == 'Buzz'


def test_fizzbuss_FizzBuzz():
    assert fizzbus(15) == 'FizzBuzz'
    assert fizzbus(45) == 'FizzBuzz'
    assert fizzbus(150) == 'FizzBuzz'
