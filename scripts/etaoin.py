# etaoin_practice

"""
псевдокод:
ввод строки пользователем
инициализация defaultdict(str)
цикл по списку
    добавление символа в defaultdict
вывод словаря на экран
"""
from collections import defaultdict
from pprint import pprint


def etaoin():
    """
    Столбчатый график бедняка
    Программа принимающая строку и отображающая сколько раз был повторен каждый символ
    """
    user_input = input('Введите предложение: ')
    chars_dict = defaultdict(str)

    for char in user_input:
        chars_dict[char.lower()] += char.lower()
    pprint(chars_dict)


if __name__ == '__main__':
    etaoin()