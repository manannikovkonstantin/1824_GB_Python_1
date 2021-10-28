"""Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
 значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3
a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?"""


def val_checker(s):
    def wrap(func):
        def called(*args, **kwargs):
            for item in args:
                b = s(item)
                if b is not True:
                    msg = f'wrong val: {item}'
                    raise ValueError(msg)
            result = func(*args, **kwargs)
            return result

        return called

    return wrap


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(55)
print(a)

a = calc_cube(-5)


