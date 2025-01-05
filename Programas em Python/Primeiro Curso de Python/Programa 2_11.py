# Programa que conta o número de inteiros positivos divisíveis por 60 e menores que um dado n

n = int(input("Digite um valor inteiro para n: "))
r = 1
s = 0
while r <= n:
    if r % 60 == 0:
        s = s + 1
        print(s)
    r = r + 1





