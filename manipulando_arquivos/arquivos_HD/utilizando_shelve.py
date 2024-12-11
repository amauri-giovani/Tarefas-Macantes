#! python3
#Salvando variáveis em arquivos com o módulo shelve.
#Salva variáveis em programas Python em arquivos shelf binários. No Windows são criados 3 arquivos: ".bak", ".dat" e ".dir".
#O módulo shelve permite adicionar funcionalidades como "Salvar" e "Abrir" no programa.

import shelve, os			#importa o módulo shelve para salvar as variáveis em arquivos do tipo shelf e o módulo os para acessar o arquivo.

#Salvando as variáveis no arquivo shelf.
shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
cats = ['Zophie', 'Pooka', 'Simon']											#atribui os valores à "cats".
cat = ['Pooka']																#atribui os valores à "cat".
cat2 = ['Simon']															#atribui os valores à "cat2".
shelfFile['cats'] = cats													#salva a variável "cats" no arquivo.
shelfFile['cat'] = cat 														#salva a variável "cat" no arquivo.
shelfFile['cat2'] = cat2 													#salva a variável "cat2" no arquivo.
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.

#Abrindo o arquivo shelf e exibindo os valores das variáveis.
shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
print('\nConteúdo da variável "cats": ', shelfFile['cats'])					#exibe os valores de "cats".
print('Conteúdo da variável "cat": ', shelfFile['cat'])						#exibe os valores de "cat".
print('Conteúdo da variável "cat2": ', shelfFile['cat2'])					#exibe os valores de "cat2".
print('Chaves do arquivo "mydata": ', list(shelfFile.keys()))				#exibe as chaves da variável "cats".
print('Valores do arquivo "mydata": ', list(shelfFile.values()))			#exibe os valores da variável "cats".
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.



'''
#****************************************************************************************************************************************#
# A PARTIR DESTA LINHA PODERÁ SER COMENTADA ATÉ O FINAL DO PROGRAMA POIS SERVE APENAS PARA VERIFICAR O FUNCIONAMENTO DOS ARQUIVOS SHELF. #
# 											CASO HAJA INTERESSE, DESCOMENTE PARA VER O RESULTADO. 										 #
#****************************************************************************************************************************************#

#Exibe o tamanho dos arquivos utilizando os.path.join() para unir a string do diretório atual com o arquivo desejado.
print('\nTamanho do arquivo "mydata.mak"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.bak')))
print('Tamanho do arquivo "mydata.dat"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dat')))
print('Tamanho do arquivo "mydata.dir"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dir')))

file = open('C:\\Users\\Amauri\\Dropbox\\Python\\tarefas_macantes\\manipulando_arquivos\\arquivos_HD\\mydata.bak')	#abre o arquivo do tipo texto.
content = file.read()														#lê o conteúdo do arquivo e armazena em "content".
print('\nConteúdo do arquivo "mydata.bak":\n', content)						#exibe o conteúdo do arquivo.
file.close()																#fecha o arquivo do tipo texto.

#Alterando o valor de uma variável salva em um arquivo shelf.
shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
cats = ['Tom', 'Frajola']													#atribui novos valores à "cats".
shelfFile['cats'] = cats													#salva a variável "cats" no arquivo.
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.

shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
print('\nConteúdo da variável "cats": ', shelfFile['cats'])					#exibe os valores de "cats".
print('Conteúdo da variável "cat": ', shelfFile['cat'])						#exibe os valores de "cat".
print('Conteúdo da variável "cat2": ', shelfFile['cat2'])					#exibe os valores de "cat2".
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.

#Exibe o tamanho dos arquivos utilizando os.path.join() para unir a string do diretório atual com o arquivo desejado.
print('\nTamanho do arquivo "mydata.mak"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.bak')))
print('Tamanho do arquivo "mydata.dat"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dat')))
print('Tamanho do arquivo "mydata.dir"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dir')))

file = open('C:\\Users\\Amauri\\Dropbox\\Python\\tarefas_macantes\\manipulando_arquivos\\arquivos_HD\\mydata.bak')	#abre o arquivo do tipo texto.
content = file.read()														#lê o conteúdo do arquivo e armazena em "content".
print('\nConteúdo do arquivo "mydata.bak":\n', content)						#exibe o conteúdo do arquivo.
file.close()																#fecha o arquivo do tipo texto.

#Acrescentando mais valores à variável salva em um arquivo shelf.
shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
cats.append('Garfield')														#acrescenta novo valor à "cats".
cats.append('Molly')														#acrescenta novo valor à "cats".
shelfFile['cats'] = cats													#salva a variável "cats" no arquivo.
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.

shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
print('\nConteúdo da variável "cats": ', shelfFile['cats'])					#exibe os valores de "cats".
print('Conteúdo da variável "cat": ', shelfFile['cat'])						#exibe os valores de "cat".
print('Conteúdo da variável "cat2": ', shelfFile['cat2'])					#exibe os valores de "cat2".
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.

#Exibe o tamanho dos arquivos utilizando os.path.join() para unir a string do diretório atual com o arquivo desejado.
print('\nTamanho do arquivo "mydata.mak"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.bak')))
print('Tamanho do arquivo "mydata.dat"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dat')))
print('Tamanho do arquivo "mydata.dir"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dir')))

file = open('C:\\Users\\Amauri\\Dropbox\\Python\\tarefas_macantes\\manipulando_arquivos\\arquivos_HD\\mydata.bak')	#abre o arquivo do tipo texto.
content = file.read()														#lê o conteúdo do arquivo e armazena em "content".
print('\nConteúdo do arquivo "mydata.bak":\n', content)						#exibe o conteúdo do arquivo.
file.close()																#fecha o arquivo do tipo texto.

numeros = []																#cria a lista "numeros" vazia.
for i in range(600):														#para um range de 0 a 599.
	numeros.append(i)														#acrescenta novo valor de "i" à "numeros".
shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
shelfFile['numeros'] = numeros												#salva a variável "numeros" no arquivo.
shelfFile.close()															#fecha o arquivo do tipo shelf utilizando o módulo shelve.

shelfFile = shelve.open('mydata')											#abre o arquivo do tipo shelf utilizando o módulo shelve.
print('\nConteúdo da variável "numeros": ', shelfFile['numeros'])			#exibe os valores de "cats".
shelfFile.close()

#Exibe o tamanho dos arquivos utilizando os.path.join() para unir a string do diretório atual com o arquivo desejado.
print('\nTamanho do arquivo "mydata.mak"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.bak')))
print('Tamanho do arquivo "mydata.dat"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dat')))
print('Tamanho do arquivo "mydata.dir"(bytes): ', os.path.getsize(os.path.join('.', 'mydata.dir')))

file = open('C:\\Users\\Amauri\\Dropbox\\Python\\tarefas_macantes\\manipulando_arquivos\\arquivos_HD\\mydata.bak')	#abre o arquivo do tipo texto.
content = file.read()														#lê o conteúdo do arquivo e armazena em "content".
print('\nConteúdo do arquivo "mydata.bak":\n', content)						#exibe o conteúdo do arquivo.
file.close()																#fecha o arquivo do tipo texto.

'''