"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:(РЕШЕНО)
|--my_project
   |--settings
   |--mainapp
   |--adminapp_1
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);(РЕШЕНО)
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;(РЕШЕНО)
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?  """
import os


frogs = {
    'my_project': {'settings': ['__init__.py', 'dev.py', 'prod.py'],
                   'mainapp': ['__init__.py', 'models.py', 'views.py', {
                       'templates': ['base.html', 'index.html', {'mainapp': ['base.html', 'index.html']}]}],
                   'authapp': ['__init__.py', 'models.py,', 'views.py',
                               {'templates': {'authapp': ['base.html', 'index.html']}}],

                   }

}

add_fol = os.path.dirname(__file__)


def add_folder_file(data, addres):
    """ генерируют любую структуру папок и файлов, а yami не потянул"""
    for item in data:
        keys_fol = data.get(item)
        values_file = data.values()
        if isinstance(keys_fol, dict):
            folder = os.path.join(addres, item)
            add_folder_file(keys_fol, folder)
        else:
            folder = os.path.join(addres, item)
            os.makedirs(folder, exist_ok=True)
            for element in keys_fol:
                if isinstance(element, dict):
                    add_folder_file(element, folder)
                else:
                    os.makedirs(folder, exist_ok=True)
                    f = open(os.path.join(folder, element), 'x').close()


add_folder_file(frogs, add_fol)
