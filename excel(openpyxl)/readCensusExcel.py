#! python3
#readCensusExcel.py - Cria uma tabela com a população e o número de setores censitários de cada condado.

import openpyxl, pprint

print ('Abrindo arquivo...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}

#TODO: Preenche countryData com a população e os setores de cada condado.

print ('Lendo...')

for row in range(2, sheet.max_row + 1):
	#Cada linha da planilha contém dados de um setor censitário.
	state 	= sheet['B' + str(row)].value
	county 	= sheet['C' + str(row)].value
	pop 	= sheet['D' + str(row)].value

	#Garante que a chave para este estado existe.
	countyData.setdefault(state, {})

	#Garante que a chave para este condado nesse estado existe.
	countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

	#Cada linha representa um setor censitário, portanto incrementa o valor de um.
	countyData[state][county]['tracts'] += 1

	#Soma a população desse setor censitário à população do condado.
	countyData[state][county]['pop'] += int(pop)



#TODO: Abre um novo arquivo e grava o conteúdo de countData nele.
print ('Gravando resultados...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = '+ pprint.pformat(countyData))
resultFile.close()
print ('Done.')
