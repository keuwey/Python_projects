# -*- coding: utf-8; -*-
# Este script calcula o máximo divisor comum (MDC) de dois números

def MDC(n1, n2):

    if n1 != 0 != n2:
        if n1 > n2:
            dividendo = n1
            divisor = n2
        else:
            dividendo = n2
            divisor = n1
        while dividendo % divisor != 0:
            resto = dividendo % divisor
            dividendo = divisor
            divisor = resto
        print('Máximo divisor comum: ', divisor)
    else:
        print('Os números não podem ser iguais a 0')
