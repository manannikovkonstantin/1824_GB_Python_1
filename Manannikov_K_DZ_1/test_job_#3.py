percentage = 0
for i in range(1,101):
    num = str(i)
    num_11 = int(num)
    num = int(num[-1])
    if 5 <= num <= 9 or 11 <= num_11 <= 20:
        percentage = 'процентов'
    elif 2 <= num <= 4:
        percentage = 'процента'
    elif num == 1:
        percentage = 'процент'

    print("{} {}".format(i,percentage))