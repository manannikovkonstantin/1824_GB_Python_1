item_1 = input('Введите число: ')
item_2 = input('Введите число: ')


class zeroing(ZeroDivisionError):
    def __init__(self, txt: str):
        self.txt = txt


try:
    item_1 = int(item_1)
    item_2 = int(item_2)
    if item_2 == 0:
        raise zeroing('На ноль делить нельзя')

except ValueError:
    print('Введите число')
except zeroing as e:
    print(e)
else:
    print(item_1 / item_2)
