#! python3
#Se o arquivo PDF possuir uma senha, a informa para acessá-lo.

import PyPDF2													#importa o módulo PyPDF2.
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))	#abre o arquivo em modo binário obtendo pdfReader para leitura como objeto 
																#PdfFileReader para representar esse PDF.
pdfReader.isEncrypted											#verifica se o arquivo está criptografado(possui senha). Resposta True ou False.
pdfReader.decrypt('rosebud')									#informa a senha correta para descriptografar o objeto pdfReader e não o arquivo PDF.
pageObj = pdfReader.getPage(0)									#obtém a 1ª página do arquivo se a senha estiver correta.
print(pageObj.extractText())									#extrai o texto da página expecificada. 