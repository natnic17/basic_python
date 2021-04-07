'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

sum_wage = 0
sum_low_wage = 0
counter_all = 0
count_low = 0
poor_empl = []
with open("task3") as f:
    for line in f:
        items = line.split(':')
        sum_wage += int(items[1])
        counter_all += 1
        if int(items[1]) <= 20000:
            poor_empl.append(items[0])
            sum_low_wage += int(items[1])
            count_low += 1
avrg_inc = sum_wage / counter_all
avrg_low_inc = sum_low_wage / count_low
print(f"Сотрудники с окладом менее 20 тыс.: {poor_empl}")
print(f"Средний доход сотрудников: {avrg_inc}")
print(f"Средний доход сотрудников с окладом менее 20 тыс.: {avrg_low_inc}")
