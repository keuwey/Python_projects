def reverter_algoritmo(algoritmo):
    algoritmo_revertido = ''
    letras_com_aspas = ['R', 'L', 'U', 'D', 'F', 'B']

    movimentos = algoritmo.split()  # Divide o algoritmo em movimentos individuais

    # Percorre os movimentos na ordem inversa
    for movimento in reversed(movimentos):
        letra = movimento[0]

        if letra in letras_com_aspas:
            if len(movimento) == 1:
                algoritmo_revertido += letra + "'"  # Adiciona a aspa se não houver
            else:
                algoritmo_revertido += letra  # Remove a aspa se houver
        else:
            algoritmo_revertido += movimento

        algoritmo_revertido += ' '  # Adiciona um espaço entre os movimentos

    return algoritmo_revertido.strip()  # Remove espaços em branco no início ou fim


# Exemplo de uso
algoritmo = "R' U R' U' y R' F' R2 U' R' U R' F R F"
algoritmo_revertido = reverter_algoritmo(algoritmo)
print("Algoritmo: ", algoritmo)
print("Algoritmo revertido: ", algoritmo_revertido)
