ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print("Bisexto")
    else:
        print("Não é bisexto")
else:
    print("Não é bisexto")