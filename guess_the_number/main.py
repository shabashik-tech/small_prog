import random
import sys

print('КОМПЬЮТЕРНАЯ ИГРА "УГАДАЙ ЧИСЛО"')


def records():
    """
    Функция сортирующая результаты игры за сессию
    """
    table_result.append(attempt)
    table_result.sort()
    print(f'ЛУЧШИЙ РЕЗУЛЬТАТ - {table_result[0]}')
    main()


def the_game():
    """
    Функция реализующая логику игры
    """
    computer_question = random.randint(1, 100)
    global attempt
    attempt = 0
    while True:
        attempt += 1
        user_answer = int(input('ВВЕДИТЕ ЛЮБОЕ ЧИСЛО от 1 до 100: '))
        if user_answer < computer_question:
            print('НЕВЕРНО. ИСКОМОЕ ЧИСЛО БОЛЬШЕ, ПОПРОБУЙТЕ ЕЩЕ.')
        elif user_answer > computer_question:
            print('НЕВЕРНО. ИСКОМОЕ ЧИСЛО МЕНЬШЕ, ПОПРОБУЙТЕ ЕЩЕ.')
        elif user_answer == computer_question:
            print(f'ВЕРНО! ВЫ УГАДАЛИ ЧИСЛО {computer_question}, C {attempt} ПОПЫТКИ! ВЫ ПО-БЕ-ДИ-ТЕЛЬ!')
            main()


def main():
    """
    Функция принимающая выбор пользователя
    """
    print(head_message)
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


head_message = '''
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
table_result = []

if __name__ == '__main__':
    main()
