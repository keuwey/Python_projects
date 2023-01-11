print("\n")
print("-" * 60)
print("\nBem vindo(a)! Escolha uma das operações abaixo:\n")
print("Converter horas em segundos:\t\t\t1")
print("Converter horas em minutos:\t\t\t2")
print("Converter minutos em horas:\t\t\t3")
print("Converter minutos em segundos:\t\t\t4")
print("Converter segundos em horas:\t\t\t5")
print("Converter segundos em minutos:\t\t\t6\n")
print("-" * 60)
print("\n")
while True:
    operacao = input("\nDigite o número da operação ou Q para sair: ")
    if operacao.lower() == "q":
        break
    elif operacao == "1":
        tempo = float(input("Digite as horas: "))
        resultado = 3600 * tempo
        print("\n%.2f horas é igual a %.2f segundos" % (tempo, resultado))
    elif operacao == "2":
        tempo = float(input("Digite as horas: "))
        resultado = tempo * 60
        print("\n%.2f horas é igual a %.2f minutos" % (tempo, resultado))
    elif operacao == "3":
        tempo = float(input("Digite os minutos: "))
        resultado = tempo // 60
        minutos = tempo % 60
        # segundos = (tempo // 60) % 60
        print("\n%.2f minutos é igual a %.0fh %.0fm" % (tempo, resultado, minutos))
    elif operacao == "4":
        tempo = float(input("Digite os minutos: "))
        resultado = tempo * 60
        print("\n%.2f minutos é igual a %.2f segundos" % (tempo, resultado))
    elif operacao == "5":
        tempo = float(input("Digite os segundos: "))
        resultado = (tempo / 60) / 60
        minutos = (tempo / 60) % 60
        # segundos = ((tempo / 60) /60) % 60
        print(f"\n{tempo:.2f} segundos é igual a {resultado:.2f} hora(s) e {minutos:.2f} minutos") # e {segundos:.2f} segundos")
    elif operacao == "6":
        tempo = float(input("Digite os segundos: "))
        resultado = tempo / 60
        print("\n%.2f segundos é igual a %.2f minutos" % (tempo, resultado))
    else:
        print("\nDigite uma opção válida!\n")
        break
