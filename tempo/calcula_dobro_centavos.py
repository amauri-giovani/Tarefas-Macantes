import time

start = time.time()

valor = 0.01
print('Dia 1 - ', valor)

for i in range(2,31):
	valor = valor * 2
	print('Dia %s - ' %(i), valor)
end = time.time()

print('Levou %s segundos.' %(end - start))