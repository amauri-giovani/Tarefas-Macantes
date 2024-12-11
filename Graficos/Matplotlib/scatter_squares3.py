import matplotlib.pyplot as plt


# Valores de x e y
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Plota uma linha vermelha, sem contorno, e expessura s=40
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# ou a cor em RGB
plt.scatter(x_values, y_values, c=(0.8, 0, 0), edgecolor='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.show()
