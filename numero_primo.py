def is_prime(number):

    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    number = int(input("Digite um número: "))

    if is_prime(number):
        print(f"{number} é primo")
    else:
        print(f"{number} não é primo")


print(is_prime(5))
print(is_prime(7))
print(is_prime(710))

if __name__ == 'main':
    main()
