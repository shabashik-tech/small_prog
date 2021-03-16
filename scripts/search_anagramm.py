import sys

from open_files import load_file


file_name = '6of12.txt'
data = load_file(file_name)


def search_anagramm(data):
    """
    Функция находит в массиве анаграммы на слово введенное пользователем
    :param data: list
    """
    while True:
        user_word = input('Введите слово: ')

        for word in data:
            word_list = sorted(list(word))
            user_word = sorted(list(user_word))
            if word_list == user_word:
                print(f'Анаграмма найдена - {word}')

        try_again = input('Хотите продолжить? Если нет, наберите "н"')
        if try_again.lower() == 'н':
            sys.exit()


if __name__ == '__main__':
    search_anagramm(data)