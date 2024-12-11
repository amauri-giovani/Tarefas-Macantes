#! python3
#Utilizando o módulo pprint para salvar em um arquivo.py, gerando assim um módulo próprio chamado "myCats.


#Esse trecho comentado cria o módulo que não será necessário ser criado novamente.
'''
import pprint																				#importa o módulo para salvar de forma mais elegante.

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name':'Pooka', 'desc':'fluffy'}]			#cria uma lista com os respectivos valores.
fileObj = open('myCats.py', 'w')															#abre o arquivo do tipo texto simples em modo escrita.
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')										#salva a lista no arquivo.
fileObj.close()																				#fecha o arquivo.
'''

import myCats																				#importa o módulo criado anteriormente.

print(myCats.cats)																			#exibe a lista completa.
print(myCats.cats[0])																		#exibe o índice 0 da lista.
print(myCats.cats[1])																		#exibe o índice 1 da lista.
print(myCats.cats[0]['name'])																#exibe o nome com índice 0 da lista.
print(myCats.cats[1]['name'])																#exibe o nome com índice 1 da lista.
print(myCats.cats[0]['desc'])																#exibe o desc com índice 0 da lista.
print(myCats.cats[1]['desc'])																#exibe o desc com índice 1 da lista.