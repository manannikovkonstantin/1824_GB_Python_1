num = 0
percentage = 0
i = 0
while i <= 20:
    if 1 == i:
        percentage = 'процент'
    elif 2 <= i < 5:
        percentage = 'процента'
    elif 5 <= i or i == 0:
        percentage = 'процентов'
    print("{} {}".format(i,percentage))
    i += 1











