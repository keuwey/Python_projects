def resolver_equacao_quadratica(a: float, b: float, c: float) -> tuple:
    """
    Este programa usa a fórmula de Bháskara para resolver equações quadráticas.
    """
    delta = b ** 2 - 4 * a * c
    if a != 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        return x1, x2
    else:
        raise ValueError("'a' precisa ser diferente de zero (a ≠ 0)")


a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
raizes = resolver_equacao_quadratica(a, b, c)
print(f"As raízes são x' = {raizes[0]:.2f} e x'' = {raizes[1]:.2f}")
