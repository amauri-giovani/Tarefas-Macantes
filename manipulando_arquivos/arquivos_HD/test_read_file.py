import os
import re



# print(os.getcwd())

texto = 'left-to-right'

# @profile
def substitui_texto(texto):
	os.chdir('/home/amauri/')
	with open('test_read_file.txt', 'r') as filer:
		fr = filer.read()
	with open('test_read_file.txt', 'w') as file:
		reg = re.sub(texto, 'right-to-left', fr)
		file.write(reg)
	# print(reg)
	# reg = re.search(texto, file.read())
	# inicio = reg.start()
	# file.seek(inicio, 0)
	# f = file.read(len(texto))
	# print(file.tell())
	# print(f)
	# print('\n', reg, '\n', reg.start())

substitui_texto(texto)