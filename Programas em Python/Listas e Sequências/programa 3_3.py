# Programa que calcula o valor do último termo de uma progressão aritmética

a = [0, 0]
a[0] = float(input("Digite um valor real para o primeiro termo da sequência: "))
r = float(input("Digite um valor real para a razão de progressão: "))
i = int(input("Digite um valor inteiro i tal que i+1 é igual ao número de termos da sequência: "))
a[1] = a[0] + r
n = 1
while n < i:
    m = n + 1
    a.append(0)
    a[m] = a[1] + n*r
    n = n + 1
#print(a)
print(a[len(a)-1])


