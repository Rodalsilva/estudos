
b = [0, 0]
b[0] = 3
n = 0
while n < 5:
    b[n+1] = 2*b[n]
    if n == 4:
        break
    else:
        b.append(0)
    n = n + 1
print("Os seis termos iniciais da sequência são dados na lista abaixo:")
print(b)

