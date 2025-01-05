# Algoritmo de Fatoração

n = int(input("Digite um valor inteiro: "))
m = 0
def fatoração(n):
    F = 2
    r = n%F
    while F < n**(1/2):
        if r == 0:
            m = F
            break
        elif r != 0:
            F += 1
            if n%F == 0:
                m = F
                break
    if F > n**(1/2):
        print(f"{n} é primo")
    return F
    
print(fatoração(n))
