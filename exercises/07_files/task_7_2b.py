# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = {"duplex", "alias", "configuration"}
from sys import argv

src_file = argv[1]
dst_file = argv[2]
with open(src_file, 'r') as src:
    with open(dst_file, 'w') as dest:
        for line in src:
            if line.startswith('!') or set(ignore).intersection(set(line.split())):
                pass
            else:
                dest.write(line)