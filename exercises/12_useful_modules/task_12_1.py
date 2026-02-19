# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

list_address = ['10.10.10.10','8.8.8.8']
def ping_ip_addresses(list_address):
    '''
    Описание выше
    '''
    avail = []
    unavail = []
    for ip_add in list_address:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_add],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='utf-8')
        if reply.returncode == 0:
            avail.append(ip_add)
        else:
            unavail.append(ip_add)
    result = [avail,unavail]
    return tuple(result)

if __name__ == '__main__':
    print(ping_ip_addresses(list_address))