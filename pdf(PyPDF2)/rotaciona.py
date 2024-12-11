#! python3
#Gira a 1ª página em 90°. Pode ser passado os valores 90, 180 ou 270.

import PyPDF2			#importa o módulo.

minutesFile = open('meetingminutes.pdf', 'rb')			#abre o arquivo do tipo binário em modo leitura.
pdfReader = PyPDF2.PdfFileReader(minutesFile)			#obtém o objeto PdfFileReader para leitura em pdfReader para representar esse PDF.
page = pdfReader.getPage(0)								#obtém a 1ª página.
page.rotateClockwise(90)								#rotaciona a página em 90 graus.

pdfWriter = PyPDF2.PdfFileWriter()						#obtém o objeto PdfFileWriter em pdfWriter para escrever posteriormente.
pdfWriter.addPage(page)									#adiciona a página rotacionada no objeto pdfWriter.
resultPdfFile = open('rotatePage.pdf', 'wb')			#cria um arquivo do tipo binário em modo escrita.
pdfWriter.write(resultPdfFile)							#escreve a página no arquivo.

resultPdfFile.close()									#fecha o arquivo.
minutesFile.close()										#fecha o arquivo.
