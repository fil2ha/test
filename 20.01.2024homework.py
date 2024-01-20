# Задачи на дом

from math import pi

def calculate(symbol, number):
    return (symbol == 's') * 4 * number + (symbol == 'c') * 2 * pi * number

# Примеры использования:
print(calculate('s', 10))
print(calculate('c', 7))


def is_prime(num):
    if len([i for i in range(1, num + 1) if num % i == 0]) == 2:
        return True
    else:
        return False

print(is_prime(5))
print(is_prime(8))
print(is_prime(97))
print(is_prime(56))
print(is_prime(1))


# Задание
# https://www.codewars.com/kata/52998bf8caa22d98b800003a/train/python
def manhattan_distance(pointA, pointB):
    if (pointB[0] >= pointA[0]):
        x = (pointB[0])- (pointA[0])
        if pointB[1] >= pointA[1]:
            y = (pointB[1]) - (pointA[1])
        else:
            y = (pointA[1]) - (pointB[1])
    else:
        x = (pointA[0])- (pointB[0])
        if pointB[1] >= pointA[1]:
            y = (pointB[1]) - (pointA[1])
        else:
            y = (pointA[1]) - (pointB[1])
    return x + y
# Решено
# https://prnt.sc/qWzpOhhBq95e


# Задание
# https://www.codewars.com/kata/55a7de09273f6652b200002e/python
def lucasnum(n):
    f, s = 2, 1
    if n >= 0:
        for i in range(n):
            f, s = s, f + s
        return f
    else:
        for i in range(abs(n)):
            f, s = s - f, f
        return f
# Решено
# https://prnt.sc/FMF3KmHYi2-g