def bubble_sort(lista: list) -> list:
    """Ordena uma lista usando o algoritmo bubble sort."""
    for passnum in range(len(lista) - 1, 0, -1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ordenada = bubble_sort(lista)
print(ordenada)
