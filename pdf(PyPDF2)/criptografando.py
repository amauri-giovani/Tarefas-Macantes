#! python3
#Criptografa o arquivo PDF com senha.

import PyPDF2														#importa o módulo PyPDF2.

pdfFile = open('meetingminutes.pdf', 'rb')							#abre o arquivo do tipo binário em modo leitura.
pdfReader = PyPDF2.PdfFileReader(pdfFile)							#obtém o objeto PdfFileReader para leitura em pdfReader para representar esse PDF.
pdfWriter = PyPDF2.PdfFileWriter()									#obtém o objeto PdfFileWriter em pdfWriter para escrever posteriormente.

for pageNum in range(pdfReader.numPages):							#percorre todas as páginas do arquivo PDF.
	pdfWriter.addPage(pdfReader.getPage(pageNum))					#adiciona todas as páginas do arquivo em pdfWriter.

pdfWriter.encrypt('swordfish')										#cria a senha "swordfish" para criptografar o arquivo PDF.
resultPdfFile = open('encryptedminutes.pdf', 'wb')					#cria um arquivo PDF do tipo binário em modo escrita.
pdfWriter.write(resultPdfFile)										#escreve o conteúdo de pdfWriter no arquivo PDF.
resultPdfFile.close()												#feacha o arquivo.

