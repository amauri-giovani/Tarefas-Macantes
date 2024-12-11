from die import Die
import pygal


# Cria um D6
die = Die()

# Faz alguns lançamentos e armazena os resultados em ma lista
results = []
for roll_num in range(1000):
	result = die.roll()			# roll devolve um número aleatório.
	results.append(result)
# print(results)

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
# 	print("frequency: ", frequency)
# 	print("frequencies: ", frequencies)

# print("Resultado final ==> ", frequencies)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
