def encontrarMinimo(lista):
    minimo = lista[0]
    for elem in lista:
        if (elem < minimo):
            minimo = elem
    return minimo


listaTeste = [2, 10, 3, 1, 4, 5]
menor = encontrarMinimo(listaTeste)
print('O menor elemento da lista é: [{}]'.format(menor))