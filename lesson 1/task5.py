gain = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
fin_rez = gain - costs
if fin_rez > 0:
    print('Ваша прибыль составила', fin_rez)
    rent = fin_rez / gain
    num_emp = int(input('Введите численность сотрудников: '))
    profit_emp = fin_rez / num_emp
    print('Рентабельность выручки', rent, 'прибыль на одного сотрудника', profit_emp)
else:
    print('Ваш убыток составил', fin_rez)