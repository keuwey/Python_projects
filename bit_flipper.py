def inverter_bits(bits: str) -> str:
    """
    Inverte os bits de uma string de bits.
    Exemplo: 0100101 > 1011010
    """
    return ''.join('1' if x == '0' else '0' for x in bits)

bits = input()
invertidos = inverter_bits(bits)
print(invertidos)
