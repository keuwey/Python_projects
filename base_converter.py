def converter_base(numero: int, base_origem: int, base_destino: int) -> int:
    """Converte um número de uma base para outra."""
    # Converte o número para a base 10
    numero_base_10 = int(str(numero), base_origem)
    # Converte o número base 10 para a base de destino
    numero_convertido = int(str(numero_base_10), base_destino)
    return numero_convertido

# Exemplo: converte o número 1010 (base 2) para a base 10
numero_base_2 = 1010
numero_base_10 = converter_base(numero_base_2, 2, 10)
print(numero_base_10)  # Imprime 10

# Exemplo: converte o número 10 (base 10) para a base 16
numero_base_10 = 10
numero_base_16 = converter_base(numero_base_10, 10, 16)
print(numero_base_16)  # Imprime A
