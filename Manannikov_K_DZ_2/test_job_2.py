data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
data_final = ''
for i in data:
    if i[-1].isdigit():  # нашли значения с цифрами
        item_1 = ''
        plus = ''
        if int(i) >= 17:
            i = '"' + i + '"'
        for c in i:  # перебрали значения и вытащили цифры
            if c.isdigit():
                item_1 = item_1 + c
            else:
                plus = c
        num = int(item_1)
        if num < 10:  # добавили к значениям 0
            i = '"' + plus + '0' + item_1 + '"'
    data_final += i + ' '
print(data_final)
