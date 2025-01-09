

p = float(input("Digite um valor real para o primeiro termo da sequência: "))
r = float(input("Digite um valor real para a razão de progressão: "))
i = int(input("Digite um valor para o número de termos da sequência: "))

def progressao_aritmetica(p, r, i):
    a = [0, 0]
    a[1] = p
    n = 1
    while n < i+1:
        if n > 1:        
            a.append(0)
            a[n] = a[1] + (n-1)*r
        n = n + 1
    b = a[1:]
    return b
print(progressao_aritmetica(p, r, i))
