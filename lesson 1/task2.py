time_sec = int(input('Введите время в секундах: '))
minutes = time_sec // 60
sec = time_sec % 60
if minutes < 60:
    hours = 0
    print("%02d:%02d:%02d" % (hours, minutes, sec))
else:
    hours = minutes // 60
    mins = minutes % 60
    print("%02d:%02d:%02d" % (hours, mins, sec))
