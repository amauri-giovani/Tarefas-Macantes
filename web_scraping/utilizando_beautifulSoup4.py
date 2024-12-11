#! python3
#Utilizando BeautifulSoup para extrair informações HTML.

import requests, bs4										#importa requests para download da página e bs4 para retornar um objeto BeautifulSoup.

res = requests.get('http://nostarch.com')						#faz o download da página e armazena em "res".
res.raise_for_status()											#verifica se ocorreu algum erro.
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")		#cria um objeto BeautifulSoup e armazena em "noStarchSoup".
print(type(noStarchSoup))										#exibe o tipo, no caso, <class 'bs4.BeautifulSoup'>.

# O BeautifulSoup é um módulo usado para extrair informações de uma página HTML (e é muito melhor para isso do que as expressões regulares). O
# BeautifulSoup faz parse(ou seja, analisa e identifica partes) de um arquivo HTML no disco rígido. A função bs4.BeautifulSoup() deve ser chamada
# com uma string contendo o HTML em que o parse será feito. Essa função retorna um objeto BeautifulSoup.


# Carregando um arquivo HTML do disco rígido.
exampleFile = open('example.html')									#carrega o arquivo.
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")			#cria um objeto BeautifulSoup e armazena em "exampleSoup".
elems = exampleSoup.select('#author')								#extrai o elemento com "id=author" do arquivo.
print()																#pula uma linha.
print(type(elems))													#exibe o tipo de "elems".
print(len(elems))													#exibe o tamanho de "elems".
print(type(elems[0]))												#exibe o tipo do elemento de índice 0 em "elems".
print(elems[0].getText())											#retorna o texto de elemento de índice 0 em "elems".
print(str(elems[0]))												#retorna as tags de abertura e fechamento e o texto do elemento.
print(elems[0].attrs)												#fornece um dicionário com o atributo "id" do elemento e o valor "author".
print()																#pula uma linha.
print(exampleSoup)													#exibe o conteúdo do arquivo armazenado em "exampleSoup".

print()																#pula uma linha.
pElems = exampleSoup.select('p')									#extrai o elemento <p> do arquivo.
print(str(pElems[0]))												#exibe o elemento 0 com as tags no formato string.
print(pElems[0].getText())											#exibe somente o texto do elemento 0 sem as tags.
print(str(pElems[1]))												#exibe o elemento 0 com as tags no formato string.
print(pElems[1].getText())											#exibe somente o texto do elemento 1 sem as tags.
print(str(pElems[2]))												#exibe o elemento 0 com as tags no formato string.
print(pElems[2].getText())											#exibe somente o texto do elemento 2 sem as tags.

print()																#pula uma linha.
spanElem = exampleSoup.select('span')[0]							#extrai o elemento <span> de índice 0 do arquivo.
print(str(spanElem))												#retorna: <span id="author">Al Sweigart</span>
print(spanElem.get('id'))											#retorna: author
print(spanElem.get('some_nonexistent_addr') == None)				#retorna: True
print(spanElem.attrs)												#retorna: {'id': 'author'}
print(spanElem.getText())											#retorna o texto de span: "Al Sweigart".


#################################################################################################################################################
#															EXEMPLO DE SELETORES CSS 															#
#################################################################################################################################################
#	SELETOR PASSADO AO MÉTODO select()	#									CORRESPONDE A...													#
#***************************************#*******************************************************************************************************#
# 	soup.select('div')					#	Todos os elementos de nome <div>.																	#
#***************************************#*******************************************************************************************************#
#  	soup.select('#author')				#	O elemento com um atributo id igual a author. 														#
#***************************************#*******************************************************************************************************#
#	soup.select('.notice')				#	Todos os elementos que utilizem um atributo class de CSS chamado notice.							#
#***************************************#*******************************************************************************************************#
#  	soup.select('div span')				#	Todos os elementos de nome <span> que estejam em um elemento chamado <div>.							#
#***************************************#*******************************************************************************************************#
#	soup.select('div > span')			#	Todos os elementos de nome <span> que estejam diretamente em um elemento chamado <div>, sem que 	#
#										#	haja outros elementos intermediários.																#
#***************************************#*******************************************************************************************************#
#  	soup.select('input[name]')			#	Todos os elementos de nome <input> que tenham um atributo name com qualquer valor. 					#
#***************************************#*******************************************************************************************************#
#  	soup.select('input[type="button"]')	#	Todos os elementos de nome <input> que tenham um atributo chamado type com o valor button. 			#
#################################################################################################################################################