import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

#z = [20, 5, 100, 33, 10] para mudar o tamanho dos pontos, coloca-se s=z no código


titulo = "Scatterplot: gráfico de dispersão"
eixox= "Eixo X"
eixoy = "Eixo Y"

#Titulo
plt.title("Gráfico teste")

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x, y, label="Meus pontos", color="red", marker= ".", s=200) #plt.scatter é para fazer o grafico de dispersão
plt.plot(x,y, color="k",) #plot liga as linmhas nos pontos

plt.legend()
plt.show()
#plt.savefig("graficoteste.png", dpi=300) #para salvar a imagem, dpi é a resolução