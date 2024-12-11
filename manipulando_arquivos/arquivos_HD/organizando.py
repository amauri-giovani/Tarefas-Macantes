#! python3
#Copiando, movendo, renomeando e excluindo arquivos do HD

#Copiando arquivos e pastas SEM verificar se o diretórios e os arquivos existem.
import shutil, os			#importa o módulo shutil para copiar, mover, renomear e exluir arquivos e o módulo os para acessar arquivos do OS.


#As linhas abaixo estão comentadas para não gerar erro caso a pasta já exista. Elas criam o diretório, copiam e renomeiam o arquivo.
#Como fazer as verificações estão mais abaixo.
'''
print('\n\n\nCopiando arquivos e pastas SEM verificar se o diretórios e os arquivos existem.\n')
print('Diretório ou Pasta atual: ', os.getcwd())				#exibe o diretório de trabalho atual.
os.chdir('C:\\')												#vai para o diretório C:\.
os.makedirs('C:\\spamPython')									#cria o diretório "delicious" em C:\.
shutil.copy('C:\\spam.txt', 'C:\\spamPython')					#copia o arquivo "spam.txt" para o diretório C:\spam com o mesmo nome.
shutil.copy('C:\\spam.txt', 'C:\\spamPython\\spam2.txt')		#copia o arquivo "spam.txt" para o diretório C:\spam alterando o nome para "spam2.txt".
shutil.copytree('C:\\spamPython', 'C:\\spamPython_BACKUP')		#copia a pasta "C:\spamPython" e seus arquivos criando a pasta "C:\spamPython_BACKUP".
shutil.move('C:\\spam_calc\\calc.exe', 'C:\\spam_calc\\novo_calc.exe')	#renomeia o arquivo "calc.exe" para "novo_calc.exe". Pode-se mover renomeando também.
shutil.move('C:\\spam_calc', 'C:\\spamPython')							#move a pasta "spam_calc" e seus arquivos para a pasta "C:\spamPyhton".
'''

'''
#Criando strings para os nomes de arquivos.
print('\n\n\nCriando strings para os nomes de arquivos.\n')		#exibe a mensagem para organizar o conteúdo do programa na saída.
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']		#cria uma lista com os nomes de arquivos.
for filename in myFiles:										#percorre a lista e armazena um índice por vez em "filename".
	print(os.path.join('C:\\', filename))						#exibe na tela a string "C:\"filename" onde filename é o nome do arquivo em filename.


#Lidando com paths absolutos e relativos.
# Path Absoluto: que sempre começa com a pasta-raiz.
# Path Relativo: que é relativo ao diretório de trabalho atual do programa.
print('\n\n\nLidando com paths absolutos e relativos.\n')				#exibe a mensagem para organizar o conteúdo do programa na saída.
os.chdir('C:\\Python34')												#vai para o diretório C:\Python34.
print('Diretório atual: ', os.getcwd())									#exibe o diretório de trabalho atual.
print('Path absoluto: ', os.path.abspath('.'))							#retorna uma string com o path absoluto referente ao argumento.
print('Path relativo: ', os.path.abspath('.\\Scripts'))					#retorna C:\Python34\Scripts. O ponto(.) é o diretório atual.
print('Absoluto(True) ou Relativo(False): ', os.path.isabs('.'))		#retorna True para path absoluto ou False para path relativo. Nesse caso "False".
print('Absoluto ou Relativo: ', os.path.isabs(os.path.abspath('.')))	#retorna True para path absoluto ou False para path relativo. Nesse caso "True".
print('Path Relativo: ', os.path.relpath('C:\\Windows', 'C:\\'))		#retorna uma string com o path relativo de "C:\Windows" em relação à "C:\".
print('Path Relativo: ', os.path.relpath('C:\\Python34', 'C:\\Scripts'))	#retorna uma string com o path relativo de "C:\Windows" em relação à "C:\".
																		#Se não for passado o segundo argumento, será levado em conta o diretório atual.
path = 'C:\\Windows\\System32\\calc.exe'								#armazena o path de "cal.exe".
print('Antes da última barra: ', os.path.dirname(path))					#retorna uma string contendo tudo que estiver antes da última barra.
print('Após a última barra: ', os.path.basename(path))					#retorna uma string contendo tudo que estiver após a última barra.

calcFilePath = 'C:\\Windows\\System32\\calc.exe'						#armazena o path em "calcFilePath".
print('Tupla (calcFilePath): ', os.path.split(calcFilePath))			#retorna uma tupla separando o diretório e o arquivo.
tupla = os.path.dirname(calcFilePath), os.path.basename(calcFilePath)	#armazena o diretório e o arquivo em uma tupla.
print('Tupla (tupla): ', tupla)									#retorna o mesmo que a linha acima, ou seja, uma tupla separando o diretório e o arquivo.
print('Tupla (os.path.sep): ', calcFilePath.split(os.path.sep))			#retorna uma tupla separando tudo que estiver separado por barra. A variável os.sep
												#é definida com a barra correta de separação de pastas para o computador que estiver executando o programa.

#Calculando o tamanho dos arquivos.
print('\n\n\nCalculando o tamanho dos arquivos.\n')							#exibe a mensagem para organizar o conteúdo do programa na saída.
print('Tamanho do arquivo: ', os.path.getsize('C:\\Python34\\python.exe'))	#retorna o tamanho do arquivo "calc.exe".
print('Arquivos do diretório: ', os.listdir('C:\\Python34'))				#retorna uma lista com os nomes dos arquivos contidos neste diretório.
totalSize = 0																#atribui o valor "0" à variável "totalSize".
for filename in os.listdir('C:\\Python34'):									#percorre todos os arquivos do diretório.
	totalSize += os.path.getsize(os.path.join('C:\\Python34', filename))	#acrescenta o tamanho do arquivo à variável "totalSize".
print(totalSize, '- Este é o tamanho da pasta em bytes')					#exibe o tamanho total da pasta 'C:\Python34'.


#Abrindo e lendo em arquivos.
print('\n\n\nAbrindo, lendo e escrevendo em arquivos.\n')					#exibe a mensagem para organizar o conteúdo do programa na saída.
file = open('C:\\spamPython\\spam.txt', 'r')		#abre o arquivo conforme o argumento path passado. O modo 'r' é padrão se não for informado e significa
													#que o arquivo será aberto em modo leitura e do tipo texto. Para arquivo binário informe: "rb".
fileContent = file.read()							#lê o conteúdo do arquivo e armazena o conteúdo em uma string, independente do tamanho do arquivo.
print('Conteúdo do arquivo com file.read():\n', fileContent)				#exibe o conteúdo do arquivo.
print('Tipo da variável: ', type(fileContent))								#exibe o tipo da variável.
file.close()										#fecha o arquivo. CASO NÃO FECHE O ARQUIVO, ELE FICARÁ ABERTO NO SISTEMA OPERACIONAL.
file = open('C:\\spamPython\\spam.txt', 'r')		#abre o arquivo conforme o argumento path passado. O modo 'r' é padrão se não for informado e significa
													#que o arquivo será aberto em modo leitura e do tipo texto. Para arquivo binário informe: "rb".
fileContentLines = file.readlines()					#lê o conteúdo do arquivo e armazena em uma lista separando as linhas em elementos.
print('\nConteúdo do arquivo com file.readlines():\n', fileContentLines)	#exibe o conteúdo do arquivo.
print('Tipo da variável: ', type(fileContentLines))							#exibe o tipo da variável.
file.close()										#fecha o arquivo. CASO NÃO FECHE O ARQUIVO, ELE FICARÁ ABERTO NO SISTEMA OPERACIONAL.


#Escrevendo em arquivos.
file = open('C:\\spamPython\\spam3.txt', 'w')		#abre o arquivo. O modo 'w' significa que o arquivo será aberto em modo escrita e do tipo texto. Esse
													#modo SOBRESCREVE o conteúdo que estiver no arquivo. Para arquivo binário informe: "wb".
file.write('Escrevendo em um arquivo para depois salvá-lo.')	#escreve a frase SOBRESCREVENDO O CONTEÚDO QUE ESTIVER no arquivo.
file.close()										#fecha o arquivo. CASO NÃO FECHE O ARQUIVO, ELE FICARÁ ABERTO NO SISTEMA OPERACIONAL.

file = open('C:\\spamPython\\spam3.txt', 'r')		#abre o arquivo conforme o argumento path passado. O modo 'r' é padrão se não for informado e significa
													#que o arquivo será aberto em modo leitura e do tipo texto. Para arquivo binário informe: "rb".
fileContent = file.read()							#lê o conteúdo do arquivo e armazena o conteúdo em uma string, independente do tamanho do arquivo.
print('\nConteúdo do arquivo "spam3.txt" após a escrita:\n', fileContent)		#exibe o conteúdo do arquivo.
file.close()

file = open('C:\\spamPython\\spam3.txt', 'a')		#abre o arquivo. O modo 'a' significa que o arquivo será aberto em modo escrita e do tipo texto. Esse
													#modo ACRESCENTA o que for escrito pelo programa com o conteúdo que estiver no arquivo.
file.write('\nAcrescentando essa frase arquivo para depois salvá-lo.')	#escreve a frase no arquivo ACRESCENTANDO-A AO CONTEÚDO QUE ESTIVER no arquivo.
file.close()										#fecha o arquivo. CASO NÃO FECHE O ARQUIVO, ELE FICARÁ ABERTO NO SISTEMA OPERACIONAL.

file = open('C:\\spamPython\\spam3.txt', 'r')		#abre o arquivo conforme o argumento path passado. O modo 'r' é padrão se não for informado e significa
													#que o arquivo será aberto em modo leitura e do tipo texto. Para arquivo binário informe: "rb".
fileContent = file.read()							#lê o conteúdo do arquivo e armazena o conteúdo em uma string, independente do tamanho do arquivo.
print('\nConteúdo do arquivo "spam3.txt" após a frase adicionada:\n', fileContent)		#exibe o conteúdo do arquivo.
file.close()


#Verificando a validade de um path.
print('\n\n\nVerificando a validade de um path.\n')						#exibe a mensagem para organizar o conteúdo do programa na saída.
print('A pasta ou arquivo existe? (True ou False): ', os. path.exists('C:\\Windows'))	#retorna "True" se o arquivo ou pasta existir e "False" caso contrário.
print('A pasta ou arquivo existe? (True ou False): ', os. path.exists('C:\\Windows\\System32\\testando.txt'))	#verifica se o arquivo ou pasta existe.
print('É uma pasta? (True ou False): ', os.path.isdir('C:\\Windows\\System32'))		#verifica se é uma pasta e retorna "True" ou "False".
print('É uma pasta? (True ou False): ', os.path.isdir('C:\\Windows\\System32\\calc.exe'))	#verifica se é um arquivo e retorna "True" ou "False".
print('É um arquivo? (True ou False): ', os.path.isfile('C:\\Windows\\System32\\calc.exe'))	#verifica se é um arquivo e retorna "True" ou "False".
print('Existe algo conectado na unidade D:?', os.path.exists('D:\\'))	#verifica se há um CD-ROM, pen drive, HD ou outro dispositivo na unidade "D:".
'''


#Apagando arquivos DEFINITIVAMENTE.
lista_arquivos = []													#cria uma lista vazia para armazenar os arquivos.
lista_pastas = []													#cria uma lista vazia para armazenar as pastas.
print('Os seguintes arquivos serão apagados:')						#exibe a mensagem para o usuário.
for filename in os.listdir(os.chdir('C:\spamPython_BACKUP')):		#percorre o diretório "C:\spamPython_BACKUP".
	if os.path.isfile(filename):									#verifica se é um arquivo.
		print(filename, 'é um arquivo.')							#exibe o nome do arquivo e informa que é um arquivo.
		lista_arquivos.append(filename)								#adiciona o arquivo à lista_arquivos.
	elif os.path.isdir(filename):									#verifica se é uma pasta.
		print(filename, 'é uma pasta.')								#exibe o nome da pasta e informa que é uma pasta.
		lista_pastas.append(filename)								#adiciona a pasta à lista_pastas.
#confirma = ''
#while confirma != 'não':											#enquanto a resposta for diferente de "não".
confirma = input('Deseja continuar (sim ou não): ')				#pergunta ao usuário e aguarda uma resposta.
if confirma == 'sim':											#verifica se a resposta foi "sim".
	for i in lista_arquivos:									#percorre a lista_arquivos.
		#os.unlink(i)											#apaga arquivo por arquivo conforme o loop.
		print(i)
elif confirma == 'não':											#verifica se a resposta foi "não".
	print('Operação cancelada pelo usuário.')					#exibe a mensagem e não apaga os arquivos.
else:															#se a resposta não foi digitada corretamente "sim" ou "não".
	print('Digite sim ou não. Tente novamente.')				#pede que o usuário digite corretamente.
print('Arquivos =', lista_arquivos)									#exibe o conteúdo da lista_arquivos.
print('Pastas =', lista_pastas)										#exibe o conteúdo da lista_pastas.
