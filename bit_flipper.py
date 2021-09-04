# Um script de manipulação de bits, trocando 0s por 1s
# Ex.: >>> 0100101
# .... 1011010

print(''.join('1' if x == '0' else '0' for x in input()))
