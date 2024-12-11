import matplotlib.pyplot as plt


# Valores de entrada
input_values = [1, 2, 3, 4, 5]
# Alguns valores
squares = [1, 4, 9, 16, 25]
# Valores e a expessura da linha
plt.plot(input_values, squares, linewidth=5)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Mostra o gráfico
plt.show()
