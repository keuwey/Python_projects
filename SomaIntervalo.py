def somar_ate(limite: int) -> int:
    """
    Esse programa soma os números inteiros naturais até um dado limite.
    Ex.: 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
    """
    soma = 0
    for numero in range(1, limite + 1):
        soma += numero
    return soma
    
if __name__ == '__main__':
    limite = int(input("Digite um número: "))
    print(somar_ate(limite))
