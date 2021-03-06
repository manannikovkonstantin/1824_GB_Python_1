"""Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
#>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    dict_names = {}
    for i in args:
        dict_names.setdefault(i[0],[])
        dict_names[i[0]].append(i)
        sorted_dict = {}
        for item in sorted(dict_names):
            sorted_dict[item] = dict_names[item]
    print(sorted_dict)


thesaurus("Иван", "Мария", "Петр", "Илья", "Остапий", "Оксана", "Вася", "Василиса")
