gain = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
fin_result = gain - costs
if fin_result > 0:
    print('Ваша прибыль составила', fin_result)
    rent = fin_result / gain
    num_emp = int(input('Введите численность сотрудников: '))
    profit_emp = fin_result / num_emp
    print('Рентабельность выручки', rent, 'прибыль на одного сотрудника', profit_emp)
else:
    print('Ваш убыток составил', fin_result)