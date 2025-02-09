# Programa 3.9 modificado para apresentar-se como uma função.

def progressao_geometrica(P, R, I):
    a = [0, 0]
    a[1] = float(input(P))
    q = float(input(R))
    i = int(input(I))
    n = 1
    while n < i+1:
        if n > 1:
            a.append(0)
            a[n] = a[1]*q**(n-1)
        n = n + 1
    return a

