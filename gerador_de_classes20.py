# -*- coding: UTF-8 -*-
import random

def gerar_senha():
    caracteres = ['a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'k', 'L', 'm', 'N', 'o', 'P', 'q', 'R', 's', 'T', 'u', 'V', 'w', 'X', 'y', 'Z', 'A', 'b', 'C', 'd',
                  'E', 'f', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z']
    tamanho = 4
    senha = ""
    while len(senha) < tamanho:
        random.shuffle(caracteres)
        caracter = random.choice(caracteres)
        senha += caracter
    return senha

print("\n" + gerar_senha())
