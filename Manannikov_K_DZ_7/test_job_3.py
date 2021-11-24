import os
from os.path import relpath
from shutil import copyfile

"""Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html 
   Примечание: исходные файлы необходимо оставить; обратите внимание, 
что html-файлы расположены в родительских папках (они играют роль пространств имён); 
предусмотреть возможные исключительные 
ситуации; это реальная задача, которая решена, например, во фреймворке django. """

add_fol = os.path.dirname(__file__)
anti_fol = os.path.join(add_fol, 'my_project/templates')

for root, dirs, files in os.walk(add_fol):
    if os.path.split(root)[-1] == 'templates' and anti_fol != root:
        for root_1, dirs_2, files_3 in os.walk(root):
            root_fol = os.path.join('my_project/templates', relpath(root_1, anti_fol)).replace('/../','/')#создание адреса
            os.makedirs(root_fol, exist_ok=True)#создание папок
            for file_1 in files_3:
                out_file = os.path.join(root_1, file_1)
                in_file = os.path.join(root_fol, file_1)
                copyfile(out_file, in_file) # копирование файлов
