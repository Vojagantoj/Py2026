# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address = False
while not address:
    ad = input('Введите адрес: ')
    addr = []
    if ''.join(ad.split('.')).isdigit() and len(ad.split('.')) == 4:
        for i in ad.split('.'):
            if i != '' and 0 <= int(i) <= 255:
                addr.append(int(i))
        if len(addr) == 4:
            address = True
            if 1 < addr[0] < 223:
                print('unicast')
            elif 224 < addr[0] < 239:
                print('multicast')
            elif addr[0] == addr[1] == addr[2] == addr[3] == 255:
                print('local broadcast')
            elif addr[0] == addr[1] == addr[2] == addr[3] == 0:
                print('unassigned')
            else:
                print('unused')
        else:
            print("Неправильный IP-адрес")
    else:
        print("Неправильный IP-адрес")