goods = []
while input("Хотите добавить товар? Введите да или нет: ") == 'да':
    number = int(input("Введите номер товара: "))
    info = {}
    while input("Хотите добавить информацию о товаре? Введите да или нет: ") == 'да':
        info_key = input("Введите наименование характеристики: ")
        info_value = input("Введите значение: ")
        info[info_key] = info_value
    goods.append(tuple([number, info]))
print(goods)
analitics = {}
for good in goods:
    for info_key, info_value in good[1].items():
        if info_key in analitics:
            analitics[info_key].append(info_value)
        else:
         analitics[info_key] = [info_value]
print(analitics)