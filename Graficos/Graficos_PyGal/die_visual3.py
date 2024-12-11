from die import Die
import pygal


# Cria um D6 (Dado de 6 lados)
die = Die()


# Faz alguns lançamentos e armazena os resultados em uma lista.
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# print(results)
# print(len(results))

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = " Resultados do dado de 6 lados rolando 1000 vezes"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Resultado"
hist.y_title = "Frequência do Resultado"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')		# Abra esse arquivo em um browser

