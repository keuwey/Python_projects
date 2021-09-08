"""

This script solves quadratic equations using the
Bhaskara's formula

"""

print()
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
delta = (b**2) - 4 * a * c
if a != 0:
    x1 = (-b + (delta ** (1/2))) / (2 * a)
    x2 = (-b - (delta ** (1/2))) / (2 * a)
else:
    print("a precisa ser diferente de zero (a ≠ 0)")

print()
print("As raízes são x' = %.2f e x'' = %.2f" % (x1, x2))
print()
