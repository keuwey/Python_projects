while True:
    numero = float(input("Digite o número: "))
    porcentagem = float(input("Digite a porcentagem: "))
    p = (numero / 100) * porcentagem
    print(f"{porcentagem:.2f}% de {numero:.2f} = {p:.2f}")
    continuar = input("Deseja continuar? Aperte 'Q' para sair ou [ENTER] para uma nova operação: ").lower()
    if continuar == 'q':
        break