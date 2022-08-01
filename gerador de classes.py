# -*- coding: UTF-8 -*-
import random
caracteres = ['a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'k', 'L', 'm', 'N', 'o', 'P', 'q', 'R', '-', 's', 'T', 'u', 'V', 'w', 'X', 'y', 'Z', 'A', 'b', 'C', 'd',
              'E', 'f', '_', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z', '0', '9', '8', '7', '6', '5', '4', '3', '2', '1']
tamanho = 4
print("\n")
cont = 1
while cont <= tamanho:
    random.shuffle(caracteres)
    senha = random.choice(caracteres)
    cont += 1
    print(senha, end="")
print("\n")
