import random

def gerar_senha(tam_senha: int) -> str:
    caracteres = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "+", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "/", "?", "[", "{", "]", ",", ".", ";", "<", ">", ":", "|", "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    random.shuffle(caracteres)
    senha = ""
    for i in range(tam_senha):
        senha += random.choice(caracteres)
    return senha

tam_senha = int(input("Qual o tamanho da senha: "))
print()
print(gerar_senha(tam_senha))
