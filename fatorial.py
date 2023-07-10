# -*- coding: utf-8; -*-
# Este é um simples script para calcular o fatorial
# de um número real e inteiro

fat = int(input("Digite um número: "))
f = 1
for x in range(fat, f, -1):
    f *= x

print(f)
