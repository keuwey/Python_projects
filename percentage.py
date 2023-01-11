def calculate_percentage(numero: float, porcentagem: float) -> float:
    return numero / 100 * porcentagem


def main():

    while True:
        numero = float(input("\nDigite o número: "))
        porcentagem = float(input("Digite a porcentagem: "))
        result = calculate_percentage(numero, porcentagem)
        print(f"{porcentagem:.2f}% de {numero:.2f} = {result:.2f}")
        continuar = input(
            "Deseja continuar? Aperte 'Q' para sair ou [ENTER] para uma nova operação: ")
        if continuar.lower() == 'q':
            break


if __name__ == "main":
    main()
