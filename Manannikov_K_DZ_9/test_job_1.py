"""Создать класс TrafficLight (светофор):
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    __color = {'red': 'Красный', 'yellow': 'Жёлтый', 'green': 'Зелёный'}

    def running(self, work_red: int = 7, work_yellow: int = 2, work_green: int = 7):

        while work_red + work_yellow + work_green:
            if work_red >= 1:
                print(f"{TrafficLight.__color['red']}")
                work_red -= 1
            elif work_yellow >= 1:
                print(f"{TrafficLight.__color['yellow']}")
                work_yellow -= 1
            elif work_green >= 1:
                print(f"{TrafficLight.__color['green']}")
                work_green -= 1
            time.sleep(1)


# Создание экземпляра класса
a = TrafficLight()
# Вызов метода
a.running()
