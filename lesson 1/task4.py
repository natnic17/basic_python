n = int(input('Введите целое положительное число: '))
maxi = n % 10
while n != 0:
    last = n % 10
    if last > maxi:
        maxi = last
    n = n // 10
print('Максимальная цифра в Вашем числе равна', maxi)