from die import Die


# Cria um D6 (Dado de 6 lados)
die = Die()


# Faz alguns lançamentos e armazena os resultados em uma lista.
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)

print(results)
# print(len(results))
