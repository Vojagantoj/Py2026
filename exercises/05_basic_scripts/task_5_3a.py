# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""
result = dict(
access = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
,
trunk = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
)
ask = dict(access = 'Введите номер VLAN: ', trunk = 'Введите разрешенные VLANы: ')
tp = input('Введите режим работы интерфейса (access/trunk): ')
it = input('Введите тип и номер интерфейса: ')
vl = input('{}'.format(ask[tp]))

print('interface ' + it)
print('\n'.join(result[tp]).format(vl))