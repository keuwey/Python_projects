while True:
    massa = float(input("\nDigite a sua massa em kg: "))
    altura = float(input("Digite a sua altura em metro: "))
    if massa > 0 < altura:
        imc = massa / (altura ** 2)
        if imc < 18.5:
            print(f"Seu IMC é de {imc:.2f}")
            print("Você está abaixo do peso!")
        elif imc < 25:
            print(f"Seu IMC é de {imc:.2f}")
            print("Você está com o peso normal")
        elif imc < 30:
            print(f"Seu IMC é de {imc:.2f}")
            print("Você está acima do peso")
        elif imc < 35:
            print(f"Seu IMC é de {imc:.2f}")
            print("Você está obeso")
        else:
            print(f"Seu IMC é de {imc:.2f}")
            print("Você está com obesidade clínica")
        continuar = input("Digite ENTER para fazer um novo cálculo ou 'Q' para sair: ")
        if continuar.lower() == "q":
            break
    else:
        print("Valor de massa e/ou altura inválido!")
        break
