# -*- coding: utf-8; -*-
# Este é um algoritmo gerador de senha por substituição, onde é necessário
# apenas uma chave base para gerar uma senha
# Ex.: Julinha = -$=ç§(0

chave = input("Digite a base da sua senha: ")
senha = ""
for letra in chave:
    if letra in "Aa":
        senha += "0"
    elif letra in "Bb":
        senha += "@"
    elif letra in "Cc":
        senha += "#"
    elif letra in "Dd":
        senha += "$"
    elif letra in "Ee":
        senha += "%"
    elif letra in "Ff":
        senha += "&"
    elif letra in "Gg":
        senha += "6"
    elif letra in "Hh":
        senha += "("
    elif letra in "Ii":
        senha += "ç"
    elif letra in "Jj":
        senha += "-"
    elif letra in "Kk":
        senha += "]"
    elif letra in "Ll":
        senha += "="
    elif letra in "Mm":
        senha += "+"
    elif letra in "Nn":
        senha += "§"
    elif letra in "Oo":
        senha += "¢"
    elif letra in "Pp":
        senha += "£"
    elif letra in "Qq":
        senha += "?"
    elif letra in "Rr":
        senha += "/"
    elif letra in "Ss":
        senha += "5"
    elif letra in "Tt":
        senha += "1"
    elif letra in "Uu":
        senha += "$"
    elif letra in "Ww":
        senha += "$"
    elif letra in "Xx":
        senha += ">"
    elif letra in "Yy":
        senha += ","
    elif letra in "Zz":
        senha += ":"
    else:
        senha += letra
print(senha)
