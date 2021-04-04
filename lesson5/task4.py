'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_lines = []

with open('task4_old', 'r', encoding='utf-8') as f_old:
    for i in f_old:
        i = i.split(' ', 1)
        new_lines.append(translate[i[0]] + ' ' + i[1])

with open('task4_new.txt', 'w') as f_new:
    f_new.writelines(new_lines)
