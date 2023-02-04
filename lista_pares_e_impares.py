numbers = input("Digite uma lista de números separados por vírgulas: ")
numbers = [int(x) for x in numbers.split(',')]

evens = []
odds = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

print("Números pares: ", evens)
print("Números ímpares: ", odds)
