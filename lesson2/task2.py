x = input('Введите элементы списка (через пробел): ')
my_list = [int(i) for i in x.split()]
print(my_list)
lst = []
if len(my_list) % 2 == 0:
    for i in range(0, len(my_list),2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    print(my_list)
else:
    for i in range(0, len(my_list) - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    print(my_list)