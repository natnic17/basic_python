'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


def digitsum():
    result = 0

    try:
        with open('task5.txt', 'w') as f:
            digits = input('Введите цифры через пробел: ')
            f.write(digits)

        with open('task5.txt', 'r') as f:
            data = f.read()

        for item in data.split():
            result += float(item)
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    except ValueError:
        print("Некорректные данные")
    print(result)


digitsum()
