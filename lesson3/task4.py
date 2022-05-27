import os
import random
from functools import reduce


LINES_COUNT = STRING_SIZE = 10


def get_random_string():
    return reduce(lambda string, char: string + char, [chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_SIZE)])


def create_text_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w', encoding='utf-8') as d:
        numbers = [random.randint(0, 100) for _ in range(LINES_COUNT)]
        strings = [get_random_string() for _ in range(LINES_COUNT)]
        d.writelines(['{} {}\n'.format(number, text) for number, text in zip(numbers, strings)])
        return d


def print_text_file(desc):
    with open(desc.name, 'r', encoding='utf-8') as d:
        for line in d:
            print(line)


descriptor = create_text_file('newfile.txt')
if descriptor:
    print_text_file(descriptor)
