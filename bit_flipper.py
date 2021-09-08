"""

This is a simple bit manipulation script, swapping 0s for 1s
Ex.: >>> 0100101
.... 1011010

"""

print(''.join('1' if x == '0' else '0' for x in input()))
