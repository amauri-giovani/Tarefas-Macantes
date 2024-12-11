#Procura telefones e e-mail da área de transferência

import pyperclip, re


phones = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	)''', re.VERBOSE)


emails = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)


text = str(pyperclip.paste())

telefones_encontrados = []
emails_encontrados = []

for groups in phones.findall(text):
	phonenum = '-'.join([groups[1], groups[3], groups[5]])
	telefones_encontrados.append(phonenum)
if len(telefones_encontrados) > 0:
	pyperclip.copy('\n'.join(telefones_encontrados))
	print('\nForam encontrados ', len(telefones_encontrados), ' telefones.')
	print('Copiado da área de transferência(clipboard): ')
	print('\n'.join(telefones_encontrados))
else:
	print('\nNenhum telefone encontrado')


for groups in emails.findall(text):
	emails_encontrados.append(groups[0])
if len(emails_encontrados) > 0:
	pyperclip.copy('\n'.join(emails_encontrados))
	print('\nForam encontrados ', len(emails_encontrados), ' emails.')
	print('Copiado da área de transferência(clipboard): ')
	print('\n'.join(emails_encontrados))
else:
	print('\nNenhum email encontrado')

