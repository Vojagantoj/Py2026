# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re

def get_ints_without_description(config_file):
    '''
    Описание выше
    '''

    regex = (r'interface (?P<interf>\S+)'
             r'|\s+description (?P<descr>.+)'
            )
    result = {}
    with open(config_file, 'r') as f:
        for line in f:
            match = re.match(regex, line)
            if match:
                if match.lastgroup == 'interf':
                    interf = match.group(match.lastgroup)
                    result[interf] = {}
                elif interf:
                    result[interf] = match.group(match.lastgroup)
        keys = list(result.keys())
        for j in keys:
            if result[j]:
                del result[j]
    return list(result.keys())

if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))