from Manannikov_K_DZ_4.utils_parser import extract_data, send_request
import decimal


def currency_rates(val_cod):
    """ Функция принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю """
    currency = dict(zip(extract_data('CharCode'), extract_data('Value')))  # создаёт словарь с ключами по коду валют
    currency_get = currency.get(val_cod.upper())
    currency_repl = decimal.Decimal(currency_get.replace(',', '.'))
    print(currency_repl)
    return 0


html_doc = send_request
print(html_doc)
