'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    _direction = ''

    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} начал поездку')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        self._direction = direction
        if direction in ('направо', 'налево'):
            print(f'Автомобиль повернул {direction}')
        else:
            print(f'Неверное направление')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Автомобилем {self.name} превышена скорость на {self.speed - self.MAX_SPEED} км/ч!')
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Автомобилем {self.name} превышена скорость на {self.speed - self.MAX_SPEED} км/ч!')
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc1 = TownCar(90, 'blue', 'Audi', False)
tc2 = TownCar(45, 'white', 'Mercedes', False)
sc = SportCar(200, 'red', 'Ferrari', False)
wc1 = WorkCar(35, 'green', 'Ford', False)
wc2 = WorkCar(80, 'silver', 'Geely', False)
pc = PoliceCar(120, 'white', 'Chevrolet', True)

tc1.go()
print(f'Его цвет "{tc1.color}"')
tc1.show_speed()
tc2.go()
tc2.turn('направо')
print(f'Автомобиль {tc2.name} полицейская машина? {tc2.is_police}')
wc1.go()
wc1.show_speed()
wc2.go()
wc2.show_speed()
wc2.stop()
sc.go()
print(f'По дороге мчится {sc.name}. Его цвет "{sc.color}"')
pc.go()
pc.show_speed()
pc.turn('Прямо')
pc.stop()





