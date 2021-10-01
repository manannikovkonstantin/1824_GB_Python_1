i = 0
while i <= 9:
    num = i % 2
    if num != 0:
        degree = [int(a) for a in str(i ** 3)]
        sum = 0
        for q in degree:
            sum += q + 17
        del_7 = sum % 7
        if del_7 == 0:
            print(i)
    i += 1
