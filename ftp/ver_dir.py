from ftplib import FTP


# Acessa o servidor
# ftp = FTP(host='177.190.192.180', user='ti', passwd='best@123')   # connect to host, default port
ftp = FTP('177.190.192.180', 'ti', 'best@123')   # connect to host, default port


# Acessa a pasta
ftp.cwd('DICOM PRINT')
#ftp.retrlines('LIST')			# list directory contents 
#print(ftp.dir())    			# list directory contents 

# Pega o arquivo com a versão mais recente
filename = max(ftp.nlst())

# Cria um arquivo com mesmo nome que será baixado
localfile = open(filename, 'wb')

# Faz download do arquivo
ftp.retrbinary('RETR ' + filename, localfile.write)

# Fecha a conexão FTP
ftp.quit()

# Fecha o arquivo quando encerrar o download
localfile.close()