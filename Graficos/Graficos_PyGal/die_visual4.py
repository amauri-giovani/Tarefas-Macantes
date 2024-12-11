from random import randint
import pygal


class Die():
	""" Uma classe que representa um único dado. """

	def __init__(self, num_sides=6):
		""" Supõe que seja um dado de 6 lados. """
		self.num_sides = num_sides

	def roll(self):
		""" Devolve um valor aleatório entre 1 e o número de lados. """
		return randint(1, self.num_sides)


# Cria um dado de acordo com o número escolhido
lados = int(input("Digite a quantidade de dados que deseja lançar: "))
die = Die(lados)

# Faz lançamentos de acordo com a quantidade de vezes informada e armazena os resultados em uma lista.
vezes = int(input("Quantas vezes irá lançar o dado?: "))
results = [die.roll() for roll_num in range(vezes)]
# for roll_num in range(vezes):
# 	result = die.roll()
# 	results.append(result)

# print(results)
# print(len(results))


# Analisa os resultados
# =====================

# Cria uma lista com a quantidade de vezes que cada foi escolhido de acordo com o número de lados escolhido
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
# for value in range(1, die.num_sides+1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)

# print(frequencies)


# Visualiza os resultados
# =======================

# Tipo de Gráfico
hist = pygal.Bar()

# Títulos do Grafico
hist.title = " Resultados do dado de {} lados rolando {} vezes".format(die.num_sides, vezes)
hist.x_title = "Número de Lados"
hist.y_title = "Frequência do Resultado"

# Cria uma lista com os nomes que serão colocados no eixo x de acordo com o número de lados
hist.x_labels = [x for x in [cada for cada in range(1,die.num_sides+1)]]

# Acrescenta uma série de valores a ser adicionado e uma lista dos valores que aparecerão no gráfico
hist.add('D6', frequencies)

# Cria o arquivo .svg para ser visualizado em qualquer tamanho
# Abra esse arquivo em um browser
hist.render_to_file('die_visual.svg')