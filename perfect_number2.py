for i in range(1, 1000000):
    summ = 0
    for m in range(i):
        if i % (m + 1) == 0:
            summ = summ + (m + 1)
            g = summ - i

    if g == i:
        print(g)