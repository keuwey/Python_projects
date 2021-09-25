print("-=-" * 25)
print("Bem-vindo(a) à calculadora de IMC.")
print("Quando for digitar seus dados, utilize o ponto no lugar da vígula")
print("-=-" * 25)

while True:
    massa = float(input("\nDigite a sua massa em kg: "))
    altura = float(input("Digite a sua altura em metro: "))
    if massa > 0 < altura:
        imc = massa / (altura ** 2)
        print(f"Seu IMC é de {imc:.2f}")
        continuar = input("Digite ENTER para fazer um novo cálculo ou 'Q' para sair: ")
        if continuar.lower() == "q":
            break
    else:
        print("Valor de massa e/ou altura inválido!")
        break
