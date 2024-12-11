#! python3

import smtplib, pprint

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

print(type(smtpObj))
respConnection = smtpObj.ehlo()
if respConnection[0] != 250:
	print('Servidor não encontrado.', smtpObj.ehlo())
else:
	print('Conectado', smtpObj.ehlo())
# print(smtpObj.starttls())
	respTLS = smtpObj.starttls()
	if respTLS[0] != 220:
		print('\nCriptografia TLS(porta: 587) não iniciada.')#, respTLS)
	else:
		print('\nCriptografia TLS(porta: 587) iniciada com sucesso.')#, respTLS)
		#password = input('\nDigite a senha do email: ')
		respLogin = smtpObj.login('amauri.giovani@gmail.com', 'a31p20lf')
		if respLogin[0] != 235:
			print('Não foi possível conectar a essa conta de email.')#, respLogin)
		else:
			print('Conta conectada.')#, respLogin)
			# #smtpObj.sendmail('amauri.giovani@gmail.com', 'amauri.giovani@gmail.com', 'Subject: TESTE\nIsso é um teste.'.encode('utf-8'))
			# imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
			# imapObj.login('amauri.giovani@gmail.com', 'a31p20lf')
			# pprint.pprint(imapObj.list_folders())



smtpObj.quit()