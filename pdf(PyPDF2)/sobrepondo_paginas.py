#!python3
#Sobrepõe uma página sobre a outra. Pode ser utilizado para colocar marca d'água por exemplo.

import PyPDF2								#importa o módulo PyPDF2.

minutesFile = open('meetingminutes.pdf', 'rb')								#abre o arquivo do tipo binário em modo leitura.
pdfReader = PyPDF2.PdfFileReader(minutesFile)								#obtém o objeto PdfFileReader para leitura em pdfReader para representar esse PDF.
minutesFirstPage = pdfReader.getPage(0)										#obtém a 1ª página.
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))		#abre o arquivo que contém a marca d'água
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))					#une a 1ª página de watermark.pdf com a 1ª página de meetingminutes.pdf 
																			#em minutesFirstPage. Agora as duas páginas estão em uma só.
pdfWriter = PyPDF2.PdfFileWriter()													#obtém o objeto PdfFileWriter em pdfWriter para escrever posteriormente.
pdfWriter.addPage(minutesFirstPage)											#escreve a página que contém as outras duas sobrepostas.

for pageNum in range(1, pdfReader.numPages):								#percorre o restante das páginas(da 2ª até o final do arquivo).
	pageObj = pdfReader.getPage(pageNum)									#obtém o objeto Page com a página correspondente a pageNum iniciado em 0.
	pdfWriter.addPage(pageObj)												#adiciona a página ao objeto PdfFileWriter em pdfWriter.

resultPdfFile = open('watermarkcover.pdf', 'wb')							#cria um arquivo do tipo binário em modo escrita.
pdfWriter.write(resultPdfFile)												#escreve o conteúdo de pdfWriter no arquivo.

minutesFile.close()															#fecha o arquivo
resultPdfFile.close()														#fecha o arquivo
