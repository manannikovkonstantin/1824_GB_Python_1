def function(value):
    degree = []
    sum_numers = 0
    for i in range(1, 1000, 2):
        degree.append(i ** 3 + value)
    for item in degree:
        str_degree = str(item)
        pred_sum = 0
        for x in str_degree:
            int_degree = int(x)
            pred_sum += int_degree
            del_7 = pred_sum % 7
        if del_7 == 0:
            sum_numers += int(str_degree)
    print(sum_numers)
function(0)
function(17)