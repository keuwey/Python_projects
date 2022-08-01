while True:
    porcentagem = float(input("\nDigite a porcentagem: "))
    numero = float(input("Digite um número: "))
    p = (numero / 100) * porcentagem
    print("\n", p)
    continua = input("Deseja continuar? (s ou n) ")
    if continua.lower() == "n":
        break
