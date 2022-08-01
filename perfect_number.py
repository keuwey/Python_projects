numero = int(input())
soma = 0 # contador que fará a soma dos números divisíveis e irá comparar com o número original
for x in range(1, numero): # Tem de começar de 1 porque não existe divisão por 0
    if numero % x == 0:
        soma = soma + x
if soma == numero:
    print("True")
else:
    print("False")