"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
1
#>>> next(odd_to_15)
3
...
#>>> next(odd_to_15)
15
#>>> next(odd_to_15)
...StopIteration...
"""

n = 15


def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_nums(n)
print(type(odd_to_15))

for i in range(n):
    print(next(odd_to_15))
