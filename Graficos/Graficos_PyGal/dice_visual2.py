from die import Die
import pygal


lados_1 = int(input("Digite a quantidade de lados do primeiro dado: "))
lados_2 = int(input("Digite a quantidade de lados do segundo dado: "))
# Cria dois dados cada um com uma quantidade de dados escolhida
die_1 = Die(lados_1)
die_2 = Die(lados_2)

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)
# print(len(results))

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Resultados do lançamento de dois dados rolando 1000 vezes"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [x for x in range(2, max_result + 1)]
hist.x_title = "Resultado"
hist.y_title = "Frequência do Resultado"

hist.add('{} + {}'.format(die_1.num_sides, die_2.num_sides), frequencies)
hist.render_to_file('die_visual.svg')       # Abra esse arquivo em um browser
