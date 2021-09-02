# -*- coding: utf-8; -*-
# Este script é um gerador de senhas que trabalha usando a
# biblioteca de números pseudoaleatórios e nele é possível definir
# o tamanho da senha

import random
caracteres = [' ', '!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '£', '¢', '§', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '/', '?', '°', '[', '{', '~', '^', ']', 'º', ',', '.', ';', '<', '>', ':', '|', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
tam_senha = int(input("Qual o tamanho da senha: "))
print("\n")
cont = 0
while cont <= tam_senha:
  random.shuffle(caracteres)
  senha = random.choice(caracteres)
  cont += 1
  print(senha, end="")
print("\n")
