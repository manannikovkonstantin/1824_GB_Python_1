"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp_1
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);+
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;+
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)? """
import os
from sys import argv
"""принцип работы: команда python 'test_job_1.py' создаст директорию со стандартным набором папок, 
чтоб создать свой набор папок нужно указать их имена после команды 
'python test_job_1.py vasya petya kolya'
"""

fol_struc = ['settings', 'mainapp', 'adminapp_1', 'authapp']  # список файлов во вложении
add_fol = os.path.dirname(__file__)  # адресс дерикторрии скрипта
folder = os.path.join(add_fol, 'my_project')  # создает адресс дерикторрии для корневой папки
skr_nem, *zaq = argv
zaqzaq = []

if len(argv) == 1: # проверяет условие введение название новых папок
    zaqzaq = fol_struc
elif len(argv) > 2:
    zaqzaq = zaq


def add_folder(f):  # создаёт папки
    for i in f:
        dir_fol = os.path.join(folder, i)
        os.makedirs(dir_fol, exist_ok=True)


if os.path.exists(folder):  # проверяет на наличие корневой папки
    print(f'Директория {folder} существует! Удалите текущую директорию или измените название.')
else:
    os.makedirs(folder, exist_ok=True)  # создаёт коневую папу
    add_folder(zaqzaq)
