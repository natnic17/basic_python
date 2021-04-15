'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Date:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def convert_date(cls, d_m_y):
        fragments = d_m_y.split('-')
        my_date = [int(i) for i in fragments]

        return my_date

    @staticmethod
    def validate(my_date):

        if not 0 < my_date[1] <= 12:
            print("Неверное число месяцев в году: значение должно быть от 1 до 12!")

        elif not 0 < my_date[0] <= 31:
            print('Нарушено количество дней в месяце!')

        else:
            print(f'Данные прошли валидацию! Ваша дата в виде списка: {my_date}')


print(Date.convert_date('11 - 11 - 2022'))
a = Date.convert_date('34 - 11 - 2015')
print(Date.validate(a))
b = Date.convert_date('15 - 15 - 2020')
print(Date.validate(b))
c = Date.convert_date('17 - 10 - 2021')
print(Date.validate(c))
