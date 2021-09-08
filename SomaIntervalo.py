"""

This script sums the natural numbers up to a given limit.
Ex.: 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

"""

def somaAte(limite):
    soma = 0
    numero = 1
    while numero <= limite:
        soma += numero
        numero += 1
    return "\n" + soma
    
if __name__ == '__main__':
    print(somaAte(int(input("Digite um número: "))))
