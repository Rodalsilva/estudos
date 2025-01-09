
a = [0, 0]
a[0] = 5
n = 0
while n < 5:
    a[n+1] = a[n] + 2
    if n == 4:
        break
    else:
        a.append(0)
    n = n + 1
print("Os seis termos iniciais da sequência são dados na lista abaixo:")
print(a)

