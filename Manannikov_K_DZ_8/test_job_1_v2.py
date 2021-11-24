email = (
    'meummibeppoixu-6196@yopmail.com, день  qualleworanni-4579@yopmail.com, лень sassoittaussattau-9108@yopmail.com, '
    'gosouyousseuru-5228@yopmail.com, lapiprudoyoi-3253@yopmail.com, becoyexomei-5038@yopmail.com, '
    'moullassitovau-6149@yopmail.com, кофе литр два zuffabommepro-9581@yopmail.com, yoibreibogifrau-3886@yopmail.com, '
    'seikeutrouquaussu-3519@yopmail.com, peifreudautralla-7141@yopmail.com, tronneiqueunnotto-4096@yopmail.com, '
    'wedammaujase-3912@yopmail.com, feulesoijeho-6320@yopmail.com, brafrinobritre-8636@yopmail.com, '
    'generate@outlook.com, g.enerate@outlook.com, g.e.nerate@outlook.com, g.e.n.erate@outlook.com, '
    'g.e.n.e.rate@outlook.com, g.e.n.e.r.ate@outlook.com, g.e.n.e.r.a.te@outlook.com')
import re

def email_parse_full(item):  # вариант для парсинга почт в тексте
    pars_email = re.compile(r'[0-9a-zA-Z]{1}[0-9a-zA-Z._-]{4,}@[0-9a-zA-Z]{2,}\.[a-zA-Z]{2,}')  # паттерн почты
    list_email = pars_email.findall(item)  # ищет почты и превращает их в список
    spl_email = re.compile(r'@')  # паттерн разделителя
    d_email = {}
    for email in list_email:
        email_parse = spl_email.split(email)  # разделяет почты по паттерну
        username = [email_parse[0]]
        domain = [email_parse[1]]
        email_dict = dict(zip(username, domain))
        d_email.update(email_dict)
    return d_email

print(email_parse_full(email))