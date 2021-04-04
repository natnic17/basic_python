'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

f = open("task2", "r")
strings_from_file = f.readlines()
count_str = len(strings_from_file)
print(f"Число строк в файле: {count_str}")
counter = 0
f.seek(0)
for i in range(count_str):
    string_from_file = f.readline()
    counter += 1
    count_w = len(string_from_file.split(' '))
    if count_w % 10 == 1 and count_w % 100 != 11:
        print(f"Строка {counter} содержит {count_w} слово")
    elif count_w % 10 == 2 or count_w % 10 == 3 or count_w % 10 == 4:
        print(f"Строка {counter} содержит {count_w} слова")
    else:
        print(f"Строка {counter} содержит {count_w} слов")

f.close()
