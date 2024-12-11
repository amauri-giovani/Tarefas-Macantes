#! python3

from selenium import webdriver
from bs4 import BeautifulSoup
import PyPDF2, requests

pdfFile1 = open('API_Polycom.pdf', 'rb')						#abre o arquivo do tipo binário em modo leitura.
pdf1Reader = PyPDF2.PdfFileReader(pdfFile1)						#obtém o objeto PdfFileReader para leitura em pdf1Reader para representar esse PDF.
pageObj = pdf1Reader.getPage(1)						#obtém o objeto PdfFileReader em pageObj.
#print(pageObj.extractText())

# 	pdfWriter.addPage(pageObj)									#adiciona a página no objeto pdfWriter.

# pdfOutputFile = open('API_Polycom-Portugues.pdf', 'wb')		#cria um arquivo do tipo binário em modo escrita.
# pdfWriter.write(pdfOutputFile)								#escreve o conteúdo de pdfWriter no arquivo.

# pdfOutputFile.close()											#fecha o arquivo


browser = webdriver.Firefox()
browser.get('https://translate.google.com.br/#en/pt/' + pageObj.extractText())
try:																					#para tratar erro junto com except abaixo.
	elem = browser.find_elements_by_id('result_box')								#procura elemento pela classe, no caso, "bookcover".
	print('Encontrado o elemento <%s> com o id "result_box"' %(elem.tag_name))			#exibe mensagem quando encontrar o elemento.
except:																					#caso ocorra um erro, exibe a mensagem abaixo.
	print('Não encontrado')																#exibe a mensagem caso não encontre o elemento.

# res = requests.get('https://translate.google.com.br/#en/pt/' + pageObj.extractText())
# # print(browser.raise_for_status())
# bsObj = BeautifulSoup(res.text, "html.parser")

# nameList = bsObj.findAll(id='result_box',recursive=True)
# # spanElem = res.select('span')[0]
# print(nameList[0].get_text())

# for name in nameList:
# 	print(name.get_text())


pdfFile1.close()