def person(name, surname, year, city, email, phone):
    """
    Функция принимает данные о пользователе и выводит их одной строкой
    :param name: str
    :param surname: str
    :param year: int
    :param city: str
    :param email: str
    :param phone: str
    :return: str
    """
    return ' '.join([name, surname, year, city, email, phone])


print(person(name=input('Введите Ваше имя: '), surname=input('Введите Вашу фамилию: '),
             year=input('введите год рождения: '), city=input('Введите город: '), email=input('Введите email: '),
             phone=input('Введите номер телефона: ')))
