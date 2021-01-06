import random
import sys
from settings import head_message


class GuessNumber:
    def __init__(self):
        self.user_choice = 0
        self.head_message = head_message
        self.table_result = []
        self.attempt = 0

    def menu(self):
        """
        Функция принимающая выбор пользователя
        """
        print(self.head_message)
        try:
            self.user_choice = int(input('ВЫБОР: '))
            if self.user_choice == 1:
                self.cheking_user_choice()
            elif self.user_choice == 2:
                self.records()
            elif self.user_choice == 3:
                sys.exit()
            else:
                print('Введите число от 1 до 4.')
                self.menu()
        except Exception:
            print('ВВЕДИТЕ ЧИСЛО!')
            self.menu()

    def cheking_user_choice(self):
        """
        Функция реализующая логику игры
        """
        computer_question = random.randint(1, 100)
        self.attempt = 0
        while True:
            self.attempt += 1
            user_answer = int(input('ВВЕДИТЕ ЛЮБОЕ ЧИСЛО от 1 до 100: '))
            if user_answer < computer_question:
                print('НЕВЕРНО. ИСКОМОЕ ЧИСЛО БОЛЬШЕ, ПОПРОБУЙТЕ ЕЩЕ.')
            elif user_answer > computer_question:
                print('НЕВЕРНО. ИСКОМОЕ ЧИСЛО МЕНЬШЕ, ПОПРОБУЙТЕ ЕЩЕ.')
            elif user_answer == computer_question:
                print(f'ВЕРНО! ВЫ УГАДАЛИ ЧИСЛО {computer_question}, C {self.attempt} ПОПЫТКИ! ВЫ ПО-БЕ-ДИ-ТЕЛЬ!')
                self.table_result.append(self.attempt)
                self.menu()

    def records(self):
        """
        Функция сортирующая результаты игры за сессию
        """
        self.table_result.sort()
        print(f'ЛУЧШИЙ РЕЗУЛЬТАТ - {self.table_result[0]}')
        self.menu()


guess_number = GuessNumber()
if __name__ == '__main__':
    guess_number.menu()