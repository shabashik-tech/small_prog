import os
import zipfile


def backup_to_zip(source, backup):
	if not os.path.exists(source):
		print(f'Сохраняемой директории не существует! - {source}')
	elif not os.path.exists(backup):
		print(f'Папки для сохранения бекапа не существует! - {backup}')
	
	counter = 1
	while True:
		name = os.path.basename(source) + '-' + str(counter) + '.zip'
		backup_name = os.path.join(backup, name)
		if not os.path.isfile(backup_name):
			break
		counter += 1
	
	print(f'Создание нового zip-файла - {backup_name}')
	zip_file = zipfile.ZipFile(backup_name, 'w')
	
	path_name = ''
	for dir, subdirs, files in os.walk(source):
		print(f'Добавление файлов из директории {dir}')
		path_name = '/'.join([path_name, os.path.basename(dir)]).strip('/')
		print(path_name)
		zip_file.write(dir, path_name)
		for file in files:
			file_name = path_name + '/' + file
			zip_file.write(os.path.join(dir, file), file_name)
	zip_file.close()
	print('Готово!')


source = 'd://Sets/'
backup = 'd://backup/'
if __name__ == '__main__':
	backup_to_zip(source, backup)
