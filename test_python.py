"""
В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math:
pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше

"""
import math

def test_filter():
    myf = lambda x : x > 0
    myl = [-1,2,1]
    assert list(filter(myf, myl)) == [2,1]
    assert list(filter(myf, [1,1,0])) == [1,1]
    myf = lambda x : x < 0
    assert list(filter(myf, myl)) == [-1]
    myf = lambda x : x in [-1,1]
    myl = [-1, 2, 1]
    assert list(filter(myf, myl)) == [-1,1]

def test_map():
    assert list(map(lambda x: x ** 2, [1,2,3])) ==  [1,4,9]
    assert list(map(lambda x,y: x*y, [1,2,3],[1,2,3,4,5])) == [1,4,9]

def test_sorted():
    assert list(sorted('mayo')) == ['a','m','o','y']
    assert list(sorted('mayo',reverse=True)) == ['y','o','m','a']
    assert list(sorted([22,21,196])) == [21,22,196]

def test_math():
    assert math.pi - 3.1415926 < 0.0000001

def test_sqrt():
    assert math.sqrt(100) == 10

def test_pow():
    assert pow(1,1) == 1
    assert pow(2,2) == 4
    assert pow(3,2) == 9
    assert pow(2,3) == 8

def test_hypot():
    assert math.hypot(2,5) == math.sqrt(2**2 + 5**2)
    assert math.hypot(5,0) == 5


