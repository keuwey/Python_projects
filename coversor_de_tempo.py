# coding: -*- utf-8; -*-
print("\n")
print("-" * 50)
print("\nBem vindo(a)! Escolha uma das operações abaixo:\n")
print("Converter horas em segundos: 1")
print("Converter horas em minutos: 2")
print("Converter minutos em horas: 3")
print("Converter minutos em segundos: 4")
print("Converter segundos em horas: 5")
print("Converter segundos para minutos: 6\n")
print("-" * 50)
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
        resultado = tempo / 60
        print("\n%.2f minutos é igual a %.2f hora(s)" % (tempo, resultado))
    elif operacao == "4":
        tempo = float(input("Digite os minutos: "))
        resultado = tempo * 60
        print("\n%.2f minutos é igual a %.2f segundos" % (tempo, resultado))
    elif operacao == "5":
        tempo = float(input("Digite os segundos: "))
        resultado = (tempo / 60) / 60
        print("\n%.2f segundos é igual a %.2f hora(s)" % (tempo, resultado))
    elif operacao == "6":
        tempo = float(input("Digite os segundos: "))
        resultado = tempo / 60
        print("\n%.2f segundos é igual a %.2f minutos" % (tempo, resultado))
    else:
        print("\nDigite uma opção válida!\n")
        break
