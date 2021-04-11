def division(var_1, var_2):
    """
    Возвращает частное от деления чисел, введенных пользователем

    :param var_1: делитель, int
    :param var_2: делимое, int
    :return: частное, float
    """
    try:
        var_1 = int(input('Введите делитель: '))
        var_2 = int(input('Введите делимое: '))
        result = var_1 / var_2
    except ValueError:
        return "Должны быть только числа!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!!!"
    return result


print(division(1, 5))
