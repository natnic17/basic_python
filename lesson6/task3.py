'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


data = [
    {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'position': 'Director',
        'wage': 150000,
        'bonus': 50000
    },
    {
        'name': 'Petr',
        'surname': 'Petrov',
        'position': 'Teacher',
        'wage': 90000,
        'bonus': 15000
    },
    {
        'name': 'Irina',
        'surname': 'Pavlova',
        'position': 'Secretary',
        'wage': 60000,
        'bonus': 10000
    },
]

for item in data:
    position = Position(**item)
    print(position.get_full_name())
    print('Должность: ', position.position)
    print('Полный доход сотрудника: ', position.get_total_income())
