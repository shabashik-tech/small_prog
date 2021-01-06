import random


def create_passwords():
    """
    Функция генерирующая пароли
    :return: list
    """
    passwords = []
    for quantity in range(quantity_password):
        password = ''
        for length in range(length_password):
            password += random.choice(data_char)
        passwords.append(password)
    return passwords


def save_file(passwords, file_name):
    """
    Функция сохраняющая полученный list паролей в файл
    :param passwords: list
    :param file_name: str
    """
    with open(file_name, 'a', encoding='utf-8') as file:
        for item in passwords:
            file.write('%s\n' % item) 


length_password = int(input('Enter length your password: '))
quantity_password = int(input('Enter quantity your password: '))
data_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
out_file = 'passwords.txt'


def main():
    passwords = create_passwords()
    save_file(passwords, out_file)


if __name__ == '__main__':
    main()