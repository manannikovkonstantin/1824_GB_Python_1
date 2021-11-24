"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
 email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru"""

import re


def email_parse(p_bret):
    patrn_email = re.compile(r'^[0-9a-zA-Z]{1}[0-9a-zA-Z._-]{4,}@[0-9a-zA-Z]{2,}\.[a-zA-Z]{2,}')  # паттерн почты
    zaqzaq = {}
    if patrn_email.match(p_bret) is not None:
        email_parse = p_bret.split('@')
        zaqzaq['username'] = email_parse[0]
        zaqzaq['domain'] = email_parse[1]
    else:
        msg = f'wrong email: {p_bret}'
        raise ValueError(msg)
    return zaqzaq


print(email_parse('someone@geekbrains.ru'))
