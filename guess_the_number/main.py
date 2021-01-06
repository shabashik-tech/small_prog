import random
import sys

print('КОМПЬЮТЕРНАЯ ИГРА "УГАДАЙ ЧИСЛО"')


def records():
    """
    Функция сортирующая результаты игры за сессию
    """
    table.append(attempt)
    table.sort()
    print(f'ЛУЧШИЙ РЕЗУЛЬТАТ НА СЕГОДНЯ - {table[0]}')
    main()


def the_game():
    """
    Функция реализующая логику игры
    """
    comp = random.randint(1, 100)
    global attempt
    attempt = 0
    while True:
        attempt += 1
        usr = int(input('ВВЕДИТЕ ЛЮБОЕ ЧИСЛО от 1 до 100: '))
        if usr < comp:
            print('НЕВЕРНО. ИСКОМОЕ ЧИСЛО БОЛЬШЕ, ПОПРОБУЙТЕ ЕЩЕ.')
        elif usr > comp:
            print('НЕВЕРНО. ИСКОМОЕ ЧИСЛО МЕНЬШЕ, ПОПРОБУЙТЕ ЕЩЕ.')
        elif usr == comp:
            print(f'ВЕРНО! ВЫ УГАДАЛИ ЧИСЛО {comp}, C {attempt} ПОПЫТКИ! ВЫ ПО-БЕ-ДИ-ТЕЛЬ!')
            main()


def main():
    """
    Функция принимающая выбор пользователя
    """
    print(head)
    try:
        a = int(input('ВЫБОР: '))
        for key, value in choice_dict.items():
            if a == key:
                value()
            else:
                print('ВВЕДИТЕ ЧИСЛО ОТ 1 ДО 3!')
                main()
    except Exception:
        print('ВВЕДИТЕ ЧИСЛО ОТ 1 ДО 3!')
        main()


head = '''
        ---------------------------------
        | 1. НОВАЯ ИГРА | 2. РЕКОРДЫ      |
        ---------------------------------
        |            3. ВЫХОД             |
        ---------------------------------
        '''
choice_dict = {
    1: the_game,
    2: records,
    3: sys.exit,
}
table = []

if __name__ == '__main__':
    main()
