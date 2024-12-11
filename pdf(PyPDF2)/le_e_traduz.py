#! python3
#Lê documento em "pdf" e traduz, salvando em outro arquivo.

import PyPDF2, os		#importa o módulo PyPDF2.

pdfFile1 = open('API_Polycom.pdf', 'rb')						#abre o arquivo do tipo binário em modo leitura.
pdf1Reader = PyPDF2.PdfFileReader(pdfFile1)						#obtém o objeto PdfFileReader para leitura em pdf1Reader para representar esse PDF.
pdfWriter = PyPDF2.PdfFileWriter()							#obtém o objeto PdfFileWriter em pdfWriter para escrever posteriormente.

for pageNum in range(2,4):										#percorre as páginas do arquivo.
	pageObj = pdf1Reader.getPage(pageNum)						#obtém o objeto PdfFileReader em pageObj.
	#print(pageObj.extractText())
	pdfWriter.addPage(pageObj)									#adiciona a página no objeto pdfWriter.

pdfOutputFile = open('API_Polycom-Portugues.pdf', 'wb')		#cria um arquivo do tipo binário em modo escrita.
pdfWriter.write(pdfOutputFile)								#escreve o conteúdo de pdfWriter no arquivo.
# print('tamanho: ', os.path.getsize('API_Polycom.pdf'))
# print('tamanho: ', os.path.getsize('API_Polycom-Portugues.pdf'))
pdfOutputFile.close()											#fecha o arquivo
pdfFile1.close()												#fecha o arquivo

txtFile = open('API_Polycom-Portugues.txt', 'w')		#cria um arquivo do tipo binário em modo escrita.
txtFile.write(pageObj.extractText())								#escreve o conteúdo de pdfWriter no arquivo.
txtFile.close()											#fecha o arquivo

file = open('API_Polycom-Portugues.txt', 'rb')
leConteudoTxt = file.read()
#pdf2Reader = PyPDF2.PdfFileReader(file)						#obtém o objeto PdfFileReader para leitura em pdf1Reader para representar esse PDF.
#objPdf = PyPDF2.PdfFileWriter()
file.close()
#print(leConteudoTxt)

fileWrite = open('API_Polycom-traduzida.pdf', 'wb')
fileWrite.write(b'%s' %(leConteudoTxt))
fileWrite.close()
print('tamanho: ', os.path.getsize('API_Polycom.pdf'))
print('tamanho: ', os.path.getsize('API_Polycom-Portugues.txt'))
print('tamanho: ', os.path.getsize('API_Polycom-traduzida.pdf'))
