import sys


def load_file(file):
    """
    функция принимает текстовый файл и делит его содержимое на отдельные слова в списке
    :param file: txt
    :return: list
    """
    try:
        with open(file, 'r', encoding='utf-8') as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as err:
        print(f'Программа завершилась ошибкой: {err}', file=sys.stderr)
    sys.exit(1)