# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
num_mac = input('Введите номер vlan: ')
mac_template = '''
{0:<8} {1:<8} {2:>11}
'''
mac = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if len(line) != 1 and line.split()[0].isdigit() and line.split()[0] == num_mac:
            l = line.split()[1:]
            l.insert(0,int(line.split()[0]))
            l.remove('DYNAMIC')
            mac.append(l)
    mac.sort()
    if len(mac) > 1:
        g = str()
        for i in mac:
            g = g + mac_template.format(i[0],i[1],i[2]).lstrip()
        print(g)
    else:
        print(mac_template.format(mac[0][0],mac[0][1],mac[0][2]).lstrip())