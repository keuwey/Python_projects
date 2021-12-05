import re
print("-=-" * 25)
print("Bem-vindo(a) ao programa\n")

"""

Para o correto funcionamento, no modo decode (decifrar), dê espaço a cada letra.
Ex.: >>> 666 444 7 777 2 9999 33 777
     >>> oiprazer

"""

modo = input("Escolha uma opção (Cifrar = 1, decifrar = 0): ")
if modo == '1':
    cifra = input("Digite a mensagem a ser cifrada: ")
    for x in cifra:
        if x.lower() == 'a':
            msg_cifrada = "2 "
            print(msg_cifrada, end="")
        elif x.lower() == 'b':
            msg_cifrada = "22 "
            print(msg_cifrada, end="")
        elif x.lower() == 'c':
            msg_cifrada == '222 '
            print(msg_cifrada, end="")
        elif x.lower() == 'd':
            msg_cifrada = '3 '
            print(msg_cifrada, end="")
        elif x.lower() == 'e':
            msg_cifrada = '33 '
            print(msg_cifrada, end="")
        elif x.lower() == 'f':
            msg_cifrada = '333 '
            print(msg_cifrada, end="")
        elif x.lower() == 'g':
            msg_cifrada = '4 '
            print(msg_cifrada, end="")
        elif x.lower() == 'h':
            msg_cifrada = '44 '
            print(msg_cifrada, end="")
        elif x.lower() == 'i':
            msg_cifrada = '444 '
            print(msg_cifrada, end="")
        elif x.lower() == 'j':
            msg_cifrada = '5 '
            print(msg_cifrada, end="")
        elif x.lower() == 'k':
            msg_cifrada = '55 '
            print(msg_cifrada, end="")
        elif x.lower() == 'l':
            msg_cifrada = '555 '
            print(msg_cifrada, end="")
        elif x.lower() == 'm':
            msg_cifrada = '6 '
            print(msg_cifrada, end="")
        elif x.lower() == 'n':
            msg_cifrada = '66 '
            print(msg_cifrada, end="")
        elif x.lower() == 'o':
            msg_cifrada = '666 '
            print(msg_cifrada, end="")
        elif x.lower() == 'p':
            msg_cifrada = '7 '
            print(msg_cifrada, end="")
        elif x.lower() == 'q':
            msg_cifrada = '77 '
            print(msg_cifrada, end="")
        elif x.lower() == 'r':
            msg_cifrada = '777 '
            print(msg_cifrada, end="")
        elif x.lower() == 's':
            msg_cifrada = '7777 '
            print(msg_cifrada, end="")
        elif x.lower() == 't':
            msg_cifrada = '8 '
            print(msg_cifrada, end="")
        elif x.lower() == 'u':
            msg_cifrada == '88 '
            print(msg_cifrada, end="")
        elif x.lower() == 'v':
            msg_cifrada = '888 '
            print(msg_cifrada, end="")
        elif x.lower() == 'w':
            msg_cifrada = '9 '
            print(msg_cifrada, end="")
        elif x.lower() == 'x':
            msg_cifrada = '99 '
            print(msg_cifrada, end="")
        elif x.lower() == 'y':
            msg_cifrada = '999 '
            print(msg_cifrada, end="")
        elif x.lower() == 'z':
            msg_cifrada = '9999 '
            print(msg_cifrada, end="")
        
        print("-=-" * 25)

        """"

        Parece que eu ainda vou ter que fazer com que cada
        palavra cifrada fique com um hífen, denotando que se trata
        de uma palavra, e não números soltos.
        Ex.: >>> 666-444 7-777-2-9999-33-777
             >>> Oi prazer

        """

elif modo == '0':
    phone_letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def number_to_text(val):
        groups = [match.group() for match in re.finditer(r'(\d)\1*', val)]
        result = ""
        for group in groups:
            keynumber = int(group[0])
            count = len(group)
            result += phone_letters[keynumber][count - 1]
        return result
    decipher_msg = input("Digite o números a serem decifrados: ")
    print("\n", number_to_text(decipher_msg))

    print("\n", "-=-" * 25)

else:
    print("Digite uma opção válida")