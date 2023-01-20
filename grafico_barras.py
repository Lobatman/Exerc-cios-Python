import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Gráfico de  barras"
eixox= "Eixo X"
eixoy = "Eixo Y"

#Titulo
plt.title("Gráfico teste")

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# para o gráfico de barras se utiliza plt.bar
plt.bar(x, y)
plt.show()