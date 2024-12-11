from random import randint
import pygal


class Die():

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


lados = int(input("Digite a quantidade de dados que deseja lançar: "))
die = Die(lados)

vezes = int(input("Quantas vezes irá lançar o dado?: "))
results = [die.roll() for roll_num in range(vezes)]
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

hist = pygal.Bar()
hist.title = "Resultados do lançamento de um dado de {} lados rolando {}\
    vezes".format(die.num_sides, vezes)
hist.x_title = "Número de Lados"
hist.y_title = "Frequência do Resultado"
hist.x_labels = [x for x in [cada for cada in range(1, die.num_sides + 1)]]
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
