

def progressao_aritmetica(P, R, I):
    a = [0, 0]
    a[1] = float(input(P))
    r = float(input(R))
    i = int(input(I))
    n = 1
    while n < i+1:
        if n > 1:        
            a.append(0)
            a[n] = a[1] + (n-1)*r
        n = n + 1
    b = a[1:]
    return b
#print(b)

