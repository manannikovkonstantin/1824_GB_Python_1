duration = int(input('Введите кол-во секунд'))
day = duration // 86400
hour = duration // 3600 % 24
minutes = duration // 60 % 60
seconds = duration % 60
if day >= 0:
    print("{} дн {} час {} мин {} сек.".format(day,hour,minutes,seconds))
elif hour >= 0:
    print("{} час {} мин {} сек.".format(day, hour, minutes, seconds))
elif minutes >= 0:
    print("{} мин {} сек.".format(day, hour, minutes, seconds))
else:
    print("{} сек.".format(seconds))