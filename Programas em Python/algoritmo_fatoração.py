# Algoritmo de Fatoração

n = int(input("Digite um valor inteiro: "))
F = 2
r = n%F

while F < n**(1/2):
    if r == 0:
        print(f"{F} é fator de {n}")
        break
    else:
        F += 1
        if n%F == 0:
            print(f"{F} é fator de {n}")
            break
if F > n**(1/2):
    print(f"{n} é primo")
    
