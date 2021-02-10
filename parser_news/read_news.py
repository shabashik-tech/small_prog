file_name = 'newsru.txt'


def read_news():
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)


if __name__ == '__main__':
    read_news()