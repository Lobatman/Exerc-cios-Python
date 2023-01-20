from io import TextIOWrapper
from msilib.schema import File


menu = 0

def abrirArquivo():
    nome = input("Digite o nome do arquivo a ser aberto: ")

    arquivo = open(nome)

    return arquivo

def lerArquivo(arquivo: TextIOWrapper):
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)


while menu != "3":

    print("(1) Abrir arquivo\n(2) Ler arquivo aberto\n(3) Sair\n")
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:
        arquivo = abrirArquivo()

    elif menu == 2: 
        lerArquivo(arquivo)
        
   