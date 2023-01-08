num = int(input("Número: "))
soma = 0
while num != 0:
    r = num % 10
    soma += r
    num //= 10

print(soma)
