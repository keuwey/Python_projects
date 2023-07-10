def reverter_algoritmo(algoritmo):
    algoritmo_revertido = ''
    letras_com_aspas = ['R', 'L', 'U', 'D', 'F', 'B']
    
    i = len(algoritmo) - 1
    while i >= 0:
        letra = algoritmo[i]
        
        if letra in letras_com_aspas:
            if i - 1 >= 0 and algoritmo[i - 1] == "'":
                algoritmo_revertido += letra
                i -= 2
            else:
                algoritmo_revertido += letra + "'"
                i -= 1
        else:
            algoritmo_revertido += letra
            i -= 1
    
    return algoritmo_revertido[::-1]

# Exemplo de uso
algoritmo = "F R U' R' U' R U R' F' R U R' U' R' F R F'"
algoritmo_revertido = reverter_algoritmo(algoritmo)
print("Algoritmo: ", algoritmo)
print("Algoritmo revertido: ", algoritmo_revertido)
