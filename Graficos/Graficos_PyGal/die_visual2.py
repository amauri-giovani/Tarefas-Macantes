from die import Die


# Cria um D6 (Dado de 6 lados)
die = Die()


# Faz alguns lançamentos e armazena os resultados em uma lista.
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

print(results)
# print(len(results))

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)