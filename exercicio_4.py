lista = [1, 3, 5, 10, 8, 9, 6, 7, 4, 2 ]

for i in range(len(lista)):

        menor = i

        for j in range (i + 1, len(lista)):

            if lista [j] < lista[menor]:
                menor = j
        if lista [i]!= lista[menor]:
            aux = lista [i]
            lista[i] = lista[menor]
            lista[menor] = aux

print (lista)