def imprimir_linha():
    print("-=-" * 25)

def calcular_imc(massa: float, altura: float) -> float:
    return massa / (altura ** 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "com o peso normal"
    elif imc < 30:
        return "acima do peso"
    elif imc < 35:
        return "obeso"
    else:
        return "com obesidade clínica"

def obter_dados() -> tuple:
    massa = float(input("\nDigite a sua massa em kg: "))
    altura = float(input("Digite a sua altura em metro: "))
    return massa, altura

imprimir_linha()
print("Bem-vindo(a) à calculadora de IMC.")
print("Quando for digitar seus dados, utilize o ponto no lugar da vírgula.")
imprimir_linha()

while True:
    massa, altura = obter_dados()
    if massa > 0 < altura:
        imc = calcular_imc(massa, altura)
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é de {imc:.2f}")
        print(f"Você está {classificacao}!")
        continuar = input("Digite ENTER para fazer um novo cálculo ou 'Q' para sair: ")
        if continuar.lower() == "q":
            break
    else:
        print("Valor de massa e/ou altura inválido!")
        break
