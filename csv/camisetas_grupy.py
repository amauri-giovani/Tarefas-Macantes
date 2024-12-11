import csv


file = open("CamisetasGrupy-SP.csv")
fileReader = csv.reader(file)
dados = list(fileReader)

for row in dados:
	print(row[0])
	print(row[1])
	print(row[2])
	tam_val = row[3].split(' - ')
	tamanho = tam_val[0]
	valor = tam_val[1][3:].replace(',','.')
	print(tamanho)
	print(valor)
