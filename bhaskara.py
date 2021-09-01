# -*- coding: utf-8; -*-
# Esse script resolve equações de segundo grau utilizando a famosa
# fórmula de Bháskara

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
delta = (b**2) - 4 * a * c
if a != 0:
    x1 = (-b + (delta ** (1/2))) / (2 * a)
    x2 = (-b - (delta ** (1/2))) / (2 * a)

print("As raízes são x' = ", x1, " e x'' = ", x2)
