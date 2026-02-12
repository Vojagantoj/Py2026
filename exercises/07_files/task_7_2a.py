# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = {"duplex", "alias", "configuration"}
from sys import argv

name_file = argv[1]

with open(name_file, 'r') as f:
    for line in f:
        if line.startswith('!') or len(line) == 0 or set(ignore).intersection(set(line.split())):
                pass
        else:
            print(line.rstrip())