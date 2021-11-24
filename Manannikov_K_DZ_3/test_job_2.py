"""*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#>>> num_translate_adv("One")
"Один"
#>>> num_translate_adv("two")
"два"
"""

nuns_trans = {'zero': 'ноль',
              'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'
              }


def num_translate(num):
    if num[0].isupper():
        print(f'"{nuns_trans.get(num.lower()).title()}"')
    else:
        print(f'"{nuns_trans.get(num)}"')


num_translate('Seven')
num_translate('six')
