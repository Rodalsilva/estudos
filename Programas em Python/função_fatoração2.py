n = int(input("Digite um valor inteiro: "))
N = [n,0,0]
N[len(N)-1] = 2
N[len(N)-2] = 3
F = 2
r = n%F
i = 0
while F < n:
    if r == 0:
        N.append(0)
        N[i+1] = N[i]/F
    n = N[i+1]
    r = n%F  
  
    i += 1
    while r != 0:
        F += 1
        r = n%F
        if r == 0:
            if N[i]/F == 2:
                N[i+1] = N[i]/F
            elif N[i]/F < 2:
                N[i+1] = 2
                
print(f"Os divisores positivos de {N[0]} são: {N}")
