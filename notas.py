# -*- coding: utf-8; -*-
# Um simples script para realizar a média de um dado número
# de notas
# Para digitar notas com casas decimais, utilize o ponto (.)
# Ex.: 5.4, 7.3 etc

notas = []
num_notas = int(input("Quantas notas você quer tirar a média: "))
for i in range(num_notas):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    
media = sum(notas) / num_notas
print("A média é: %.1f" %media)
