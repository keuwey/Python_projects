def reverter_algoritmo(algoritmo):
    movimentos = algoritmo.split()  # Divide o algoritmo em movimentos individuais
    movimentos_revertidos = []
    letras_duplas = set(['R2', 'L2', 'U2', 'D2', 'F2', 'B2'])

    # Percorre os movimentos na ordem inversa
    for movimento in reversed(movimentos):
        if movimento in letras_duplas:
            # Insere o movimento duplo no início
            movimentos_revertidos.insert(0, movimento)
        else:
            letra = movimento[0]

            if len(movimento) == 1 or movimento[1] != "'":
                # Adiciona a aspa se não houver
                movimentos_revertidos.insert(0, letra + "'")
            else:
                movimentos_revertidos.insert(
                    0, letra)  # Remove a aspa se houver

    algoritmo_revertido = ' '.join(
        movimentos_revertidos)  # Junta os movimentos

    return algoritmo_revertido


# Exemplo de uso
algoritmo = "R' U R' U' y R' F' R2 U' R' U R' F R F"
algoritmo_revertido = reverter_algoritmo(algoritmo)
print("Algoritmo: ", algoritmo)
print("Algoritmo revertido: ", algoritmo_revertido)
