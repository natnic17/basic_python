'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def size_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_size_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, measuring):
        self._measuring = measuring
        self._size_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def size_required(self):
        if not self._size_required:
            self._calc_size_required()

        return self._size_required

    @property
    def measuring(self):
        return self._measuring

    @measuring.setter
    def measuring(self, measuring):
        self._measuring = measuring
        self._size_required = None

    @property
    def total_size_required(self):
        return f"Всего для пошива потребуется {sum([item.size_required for item in self._clothes])} кв.м ткани"


class Coat(Clothes):
    def _calc_size_required(self):
        self._size_required = round(self.measuring / 6.5 + 0.5, 1)

    @property
    def V(self):
        return self.measuring

    @V.setter
    def V(self, size):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера требуется {self.size_required} кв.м ткани"


class Suit(Clothes):
    def _calc_size_required(self):
        self._size_required = round(2 * self.measuring * 0.01 + 0.3, 1)

    @property
    def H(self):
        return self.measuring

    @H.setter
    def H(self, height):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см требуется {self.size_required} кв.м ткани"


coat = Coat(3)
print(coat)
coat.V = 7
print(coat)

suit = Suit(158)
print(suit)
suit.H = 177
print(suit)

print(coat.total_size_required)
print(suit.total_size_required)
