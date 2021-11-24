""". Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt - получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера."""

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    zaq = []
    for i in f:
        remote_addr = i.split(' - - ')[0]
        piu_piu = i.split('"')[1]
        request_type = piu_piu.split()[0]
        requested_resource = piu_piu.split()[1]
        zaqzaq = remote_addr, request_type, requested_resource
        zaq.append(zaqzaq)
print(zaq)
