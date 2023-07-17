import random
import string

def gerar_senha(tam_senha: int) -> str:
    """Função que gera senha com base nos módulos string e random"""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choices(caracteres, k=tam_senha))
    return senha

tam_senha = int(input("Qual o tamanho da senha: "))
print()
print(gerar_senha(tam_senha))
