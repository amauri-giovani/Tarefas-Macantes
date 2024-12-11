import census2010		#Importa arquivo gerado pelo arquivo readCensusExcel.py

print(census2010.allData['AK'])

print(census2010.allData['AK']['Anchorage'])		#Imprime dados desse estado.

populacao = census2010.allData['AK']['Anchorage']['pop']

print('A população de 2010 de Anchorage foi ' + str(populacao))

# for i in census2010.allData:
# 	print(census2010.allData['AK'].keys())