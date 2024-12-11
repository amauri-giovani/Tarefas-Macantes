#! python3
#Cria um arquivo unindo o conteúdo de dois outros arquivos.

import PyPDF2		#importa o módulo PyPDF2.

pdfFile1 = open('programas_instalados.txt', 'rb')				#abre o 1º arquivo do tipo binário em modo leitura.
# pdf1Reader = PyPDF2.PdfFileReader(pdfFile1)				#obtém o objeto PdfFileReader para leitura em pdf1Reader para representar esse PDF.
pdfWriter = PyPDF2.PdfFileWriter()						#obtém o objeto PdfFileWriter em pdfWriter para escrever posteriormente.

# for pageNum in range(pdf1Reader.numPages):				#percorre as páginas do arquivo.
# 	pageObj = pdf1Reader.getPage(pageNum)				#obtém o objeto PdfFileReader em pageObj.
# 	pdfWriter.addPage(pageObj)							#adiciona a página no objeto pdfWriter.


pdfOutputFile = open('combinedminutes.pdf', 'wb')		#cria um arquivo do tipo binário em modo escrita.
pdfWriter.write(pdfOutputFile)							#escreve o conteúdo de pdfWriter no arquivo.

pdfOutputFile.close()									#fecha o arquivo
pdfFile1.close()										#fecha o arquivo
