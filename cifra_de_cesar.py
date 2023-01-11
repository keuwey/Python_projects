def cifrar_cesar(mensagem: str, chave: int) -> str:
    """Cifra uma mensagem usando a cifra de César."""
    alfabeto = 'abcçdefghijklmnopqrstuvwxyzABCÇDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagem_cifrada = ''
    for caractere in mensagem:
        index = alfabeto.find(caractere)
        if index == -1:
            # Caractere não encontrado
            mensagem_cifrada += caractere
        else:
            index_cifrado = (index + chave) % len(alfabeto)
            mensagem_cifrada += alfabeto[index_cifrado]
    return mensagem_cifrada

def decifrar_cesar(mensagem: str, chave: int) -> str:
    """Decifra uma mensagem cifrada com a cifra de César."""
    alfabeto = 'abcçdefghijklmnopqrstuvwxyzABCÇDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagem_decifrada = ''
    for caractere in mensagem:
        index = alfabeto.find(caractere)
        if index == -1:
            # Caractere não encontrado
            mensagem_decifrada += caractere
        else:
            index_decifrado = (index - chave) % len(alfabeto)
            mensagem_decifrada += alfabeto[index_decifrado]
    return mensagem_decifrada

def codificar_mensagem(mensagem: str, chave: int, codificar: bool) -> str:
    """Codifica ou decodifica uma mensagem usando a cifra de César."""
    if codificar:
        return cifrar_cesar(mensagem, chave)
    else:
        return decifrar_cesar(mensagem, chave)

mensagem = input("Digite a mensagem: ")
chave = int(input("\nDigite a chave da cifra: "))
codificar = bool(int(input("\nDigite o modo (cifrar = 1, decifrar = 0): ")))

mensagem_codificada = codificar_mensagem(mensagem, chave, codificar)
print(f"\nMensagem codificada: {mensagem_codificada}")
