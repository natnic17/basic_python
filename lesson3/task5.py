def my_sum():
    """
    Функция суммирует вводимые пользователем через пробел числа и выводит промежуточный результат,
    пока пользователь не введет символ. После этого выводит итоговую сумму.
    :return: сумма
    """
    sum_res = 0
    symbol = False
    while symbol == False:
        number = input('Введите числа через пробел или Q для выхода: ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                symbol = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Итоговая сумма {sum_res}')
    return


my_sum()
