import sys


def pig_latin():
    """
    Функция выводит перевод фразы с английского на pig latin
    :return: str
    """
    a_list = ['a', 'e', 'i', 'o', 'u', 'y']
    while True:
        user_words = input('Введите фразу на английском: ').lower()
        list_user_words = user_words.split(' ')
        res_list = []

        for word in list_user_words:
            if len(word) > 4:
                char = word[0]
                if char in a_list:
                    res_list.append(f'{word}{"way"}')
                else:
                    res_list.append(f'{word[1::]}{char}{"ay"}')
            else:
                res_list.append(word)

        res_str = ' '.join(res_list) + '.'
        print()
        print(res_str[0][0].upper() + res_str[1::], file=sys.stderr)

        try_again = input('Хотите продолжить? Если нет, наберите "н"')

        if try_again.lower() == 'н':
            sys.exit()


if __name__ == '__main__':
    pig_latin()