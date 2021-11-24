""" Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""

import os
from collections import defaultdict

folder = os.path.dirname(__file__)

bret_pit = {
    10: 0,
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}

skan_folder = os.scandir(folder)

django_files = defaultdict(list)

for item in skan_folder:
    i = item.stat().st_size
    if i < 10:
        bret_pit[10] += 1
    if 10 < i < 100:
        bret_pit[100] += 1
    if 100 < i < 1000:
        bret_pit[1000] += 1
    if 1000 < i < 10000:
        bret_pit[10000] += 1
print(bret_pit)







"""size_10 = [item.name for item in os.scandir(folder) if item.stat().st_size <= 10 ]
size_100 = [item.name for item in os.scandir(folder) if item.stat().st_size > 10 <= 100]
size_1000 = [item.name for item in os.scandir(folder) if item.stat().st_size > 100 <= 1000]
size_10000 = [item.name for item in os.scandir(folder) if item.stat().st_size > 1000 <= 10000]
size_100000 = [item.name for item in os.scandir(folder) if item.stat().st_size> 10000 <= 100000]"""

"""print(len(size_10))
print(len(size_100))
print(len(size_1000))
print(len(size_10000))
print(len(size_100000))"""
