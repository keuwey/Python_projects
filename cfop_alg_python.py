def reverter_algoritmo(algoritmo):
    algoritmo_revertido = ''
    letras_com_aspas = ['R', 'L', 'U', 'D', 'F', 'B']
    
    # Percorre cada caractere do algoritmo
    i = 0
    while i < len(algoritmo):
        letra = algoritmo[i]
        
        # Verifica se é uma letra que precisa ter aspas adicionadas ou removidas
        if letra in letras_com_aspas:
            # Verifica se a letra já tem uma aspa
            if i + 1 < len(algoritmo) and algoritmo[i + 1] == "'":
                # Remove a aspa
                algoritmo_revertido += letra
                i += 2
            else:
                # Adiciona a aspa
                algoritmo_revertido += letra + "'"
                i += 1
        else:
            # Caractere não é uma letra do algoritmo
            algoritmo_revertido += letra
            i += 1
    
    return algoritmo_revertido

# Exemplo de uso
algoritmo = "R2 U R' U R' U' R U' R2 D U' R' U R D'"
algoritmo_revertido = reverter_algoritmo(algoritmo)
print("Algoritmo: ", algoritmo)
print("Algoritmo revertido: ", algoritmo_revertido)
