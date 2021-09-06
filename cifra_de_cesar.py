# -*- coding: utf-8; -*-
# Um script que cifra mensagens utilizando a cifra de César

def cesar(data, key, mode):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alfabeto.find(c)
        if index == -1:
            # Caractere não encontrado
            new_data += c
        else:
            new_index = index + key if mode == 1 else index - key
            new_index = new_index % len(alfabeto)
            new_data += alfabeto[new_index:new_index+1] # Adicionando o novo caractere na posição calculada
    return "\n" + new_data
data = input("Digite a mensagem: ")
key = int(input("\nDigite a chave da cifra: "))
mode = int(input("\nDigite o modo (cifrar = 1, decifrar = 0): " ))
    
print(cesar(data, key, mode))
