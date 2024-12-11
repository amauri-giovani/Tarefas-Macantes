#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Acessa o arquivo e obtém o conteúdo da 1ª página.

import PyPDF2		#importa o módulo PyPDF2 para manipular arquivos com extensão .pdf.

pdfFileObj = open('img01.pdf', 'rb')		#abre o arquivo em modo leitura de arquivo binário.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)		#obtém um objeto PdfFileReader para leitura em pdfReader para representar esse PDF.
pdfReader.numPages									#calcula o número de páginas do arquivo.
pageObj = pdfReader.getPage(0)						#obtém um objeto Page para representar uma página, no caso, 0 corresponde à 1ª página.
a = pageObj.extractText()
#print(pageObj.extractText())						#extrai o texto da página expecificada.
# print('a=',a.encode('utf8'))
# b = a.encode("latin-1")
#print(b.decode("utf8"))
print(a)
pdfFileObj.close()