#! python3
#mcb.pyw - Salva e carrega porções de texto no clipboard.

#Usage:	py.exe mcb.pyw save <palavra-chave> - Salva clipboard na palavra-chave.
#		py.exe mcb.pyw <palavra-chave> - Carrega palavra-chave no clipboard.
#		py.exe mcb.pyw list - Carrega todas as palavras-chave no clipboard.

import shelve, pyperclip, sys											#importa o mósulo shelve para salvar variável em um arquivo.
																		#importa o mósulo pyperclip para área de transferência.
																		#importa o mósulo sys para ler a partir da linha de comando.

mcbShelf = shelve.open('mcb')											#abre o arquivo com o módulo shelve.

#Salva conteúdo do clipboard.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':				#verifica se o tamanho da linha de comando é igual a 3 e se foi digitado "save".
	mcbShelf[sys.argv[2]] = pyperclip.paste()							#copia a palavra chave para o arquivo shelf.
elif len(sys.argv) == 2:												#verifica se o tamanho da linha de comando é igual a 2.
	#Lista palavras-chave e carrega conteúdo.
	if sys.argv[1].lower() == 'list':									#verifica se foi digitado "list".
		pyperclip.copy(str(list(mcbShelf.keys())))						#copia a lista para o clipboard (área de transferência).
	elif sys.argv[1] in mcbShelf:										#verifica se a palavra chave existe no shelf como chave.
		pyperclip.copy(mcbShelf[sys.argv[1]])							#carrega o valor da chave no clipboard.

mcbShelf.close()														#fecha o arquivo.