class OnlyNumbersError(ValueError):
    def __init__(self, txt: str):
        self.txt = txt


d = input('Введите число, для остановки введите stop')
a = []

while d != 'stop':
    try:
        if not d.isdigit():
            raise OnlyNumbersError('Это не число')
        else:
            d = int(d)
            a.append(d)
    except OnlyNumbersError as e:
        print(e)
    print(a)
    d = input('Введите число, для остановки введите stop')
