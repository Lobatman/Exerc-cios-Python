import matplotlib.pyplot as plt
from io import TextIOWrapper

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x,y, color="k", linestyle="--")
plt.title("crescimento da população brasileira 1980-2016")
plt.xlabel("Ano", color="red")
plt.ylabel("População x100.000.000", color="red")
#plt.show()

plt.savefig("populacao_brasileira.png", dpi=300)