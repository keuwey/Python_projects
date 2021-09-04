# -*- coding: utf-8; -*-
# Um script para checar se um dado número é primo
# Por definição, um número primo é todo número N inteiro
# que é divisível apenas por 1 e por ele mesmo
# Ex.: 3, 5, 7, 11 etc

numero = int(input("Digite um número: "))
n = numero - 1
if numero == 0:
    print("\n%d não é primo" % numero)
elif (n ** numero) % numero == n:
    print("\n%d é primo" % numero)
else:
    print("\n%d não é primo" % numero)
    
