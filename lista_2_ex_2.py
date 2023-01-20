nome = input("Digite o nome do arquivo para ser aberto: ")

arquivo = open(nome)

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)