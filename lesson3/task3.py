def sum_of_max(var_1, var_2, var_3):
    """
    Функция принимает 3 числа (позиционных аргумента) и выводит сумму двух наибольших
    :param var_1: int
    :param var_2: int
    :param var_3: int
    :return: int
    """
    lst = [var_1, var_2, var_3]
    lst.sort()
    del lst[0]
    result = sum(lst)
    return result


print(sum_of_max(3, 6, 2))