def reverter_algoritmo(algoritmo):
    movimentos = algoritmo.split()  # Divide o algoritmo em movimentos individuais
    movimentos_revertidos = []
    letras_com_aspas = set(['R', 'L', 'U', 'D', 'F', 'B'])

    # Percorre os movimentos na ordem inversa
    for movimento in reversed(movimentos):
        if len(movimento) == 1 or movimento[1] != "'":
            # Adiciona a aspa se não houver
            movimentos_revertidos.append(movimento + "'")
        else:
            movimentos_revertidos.append(
                movimento[:-1])  # Remove a aspa se houver

    # Inverte e junta os movimentos
    algoritmo_revertido = ' '.join(movimentos_revertidos[::-1])

    return algoritmo_revertido


# Exemplo de uso
algoritmo = "R' U R' U' y R' F' R2 U' R' U R' F R F"
algoritmo_revertido = reverter_algoritmo(algoritmo)
print("Algoritmo: ", algoritmo)
print("Algoritmo revertido: ", algoritmo_revertido)
