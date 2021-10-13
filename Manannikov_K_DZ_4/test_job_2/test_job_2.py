"""Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.Можно ли, используя только методы класса str, решить поставленную задачу? -Функция должна возвращать результат числового типа, например float.Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?+Сильно ли усложняется код функции при этом?+Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. +Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? +В качестве примера выведите курсы доллара и евро. + """from cbr_parser.utils import extract_dataimport decimaldef currency_rates(val_cod):    """ Функция принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)и возвращающую курс этой валюты по отношению к рублю """    currency = dict(zip(extract_data('CharCode'), extract_data('Value')))  # создаёт словарь с ключами по коду валют    currency_get = currency.get(val_cod.upper())    currency_repl = decimal.Decimal(currency_get.replace(',', '.'))    return currency_replprint(currency_rates("usd"))print(currency_rates("USD"))print(currency_rates("eur"))print(currency_rates("EUR"))