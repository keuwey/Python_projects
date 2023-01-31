def bhaskara(a: float, b: float, c: float) -> any:
    """
    Este programa usa a fórmula de Bháskara para resolver
    equações quadráticas.
    """
    delta = b ** 2 - 4 * a * c
    if a == 0:
        raise ValueError("'a' precisa ser diferente de zero (a ≠ 0)")
    if delta < 0:
        return "A raiz quadrada de um número negativo não pertence ao intervalo dos números reais",
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    return x1, x2


a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
try:
    raizes = bhaskara(a, b, c)
except ValueError as ve:
    print(ve)
else:
    if isinstance(raizes, tuple) and len(raizes) == 1:
        print(raizes[0])
    else:
        print(f"As raízes são x' = {raizes[0]:.2f} e x'' = {raizes[1]:.2f}")
