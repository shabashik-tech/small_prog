from scripts.open_files import load_file

file_name = '6of12.txt'
data = load_file(file_name)
result = [word for word in data if word == word[::-1] and len(word) > 2]

print(*result, sep='\n')
print(f'Всего найдено палиндромов: {len(result)}')