'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

import traceback


class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


a = input("Введите число: ")
b = input("Введите число: ")
try:
    res = int(a) / int(b)
    if b == 0:
        raise OwnError("Деление на ноль запрещено!")
except ValueError:
    print("Вы ввели не число!")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления {round(res, 3)}")


def division(a, b):
    return print(f'Результат деления составляет {round((int(a) / int(b)), 3)}')


try:
    a = input("Введите число: ")
    b = input("Введите число: ")
    division(a, b)
except Exception as exc:
    print(f"Ошибка:\n {traceback.format_exc()}")
