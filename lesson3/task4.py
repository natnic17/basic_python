def power_1(x, y):
    """
    Возведение действительного положительного числа в отрицательную степень c использованием **
    :param x: float
    :param y: int, n < 0
    :return: float
    """
    result = 1 / x ** abs(y)
    return result


print(power_1(float(input('Введите действительное положительное число: ')),
              int(input('Введите целое отрицательное число: '))))


def power_2(x, y):
    """
    Возведение действительного положительного числа в отрицательную степень c использованием цикла
    :param x: float
    :param y: int, y < 0
    :return: float
    """
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(power_2(float(input('Введите действительное положительное число: ')),
              int(input('Введите целое отрицательное число: '))))
