#! python3
#Utilizando o módulo selenium.

from selenium import webdriver															#importa o módulo selenium.

#Utilizando selenium para encontrar o elemento <img>.
browser = webdriver.Firefox()															#abre o navegador Firefox.
browser.get('http://inventwithpython.com')												#acessa a URL especificada.
# try:																					#para tratar erro junto com except abaixo.
# 	elem = browser.find_element_by_class_name('bookcover')								#procura elemento pela classe, no caso, "bookcover".
# 	print('Encontrado o elemento <%s> com a classe bookcover' %(elem.tag_name))			#exibe mensagem quando encontrar o elemento.
# except:																					#caso ocorra um erro, exibe a mensagem abaixo.
# 	print('Não encontrado')																#exibe a mensagem caso não encontre o elemento.



#Clicando na página.
linkElem = browser.find_element_by_link_text('Videos')							#procura por um elemento chamado "Read It Online" em forma de link.
print(type(linkElem))																	#exibe o tipo de elemento.
linkElem.click()																		#"clica" no texto acima "Read It Online".