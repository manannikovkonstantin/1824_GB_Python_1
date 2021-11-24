"""Выяснить тип результата выражений:
                15 * 3
                15 / 3
                15 // 2
                15 ** 2
"""

item_1 = 15 * 3
item_2 = 15 / 3
item_3 = 15 // 2
item_4 = 15 ** 2

print('{} {} {}'.format('15 * 3 =', item_1, type(item_1), ))
print('{} {} {}'.format('15 / 3 =', item_2, type(item_2), ))
print('{} {} {}'.format('15 // 2 =', item_3, type(item_3), ))
print('{} {} {}'.format('15 ** 2 =', item_4, type(item_4), ))
