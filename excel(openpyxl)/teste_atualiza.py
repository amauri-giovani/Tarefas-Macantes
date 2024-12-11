PRICE_UPDATES = {}

resp = ''

while resp != 'n':
	resp = input('\nAtualizar produto? (s para sim ou n para sair): ')
	try:
		if resp == 's':
			produto = input('Digite o produto: ')
			preco = input('Digite o valor: ')
			# if ',' or '.' not in preco:
			# 	preco = input('Digite um valor válido (ex.: 2,00): ')
			if ',' in preco:
				valor = preco.replace(',', '.')
				PRICE_UPDATES[produto] = float(valor)
			else:
				PRICE_UPDATES[produto] = float(preco)
		else:
			print('Digite s para alterar um produto e valor ou n para sair')
	except ValueError:
			preco = input('Digite um valor válido (ex.: 2,00): ')
			if not ValueError:
				pass
			else:
				print('O valor desse produto não será alterado devido ao valor inválido informado.')
print(PRICE_UPDATES)
