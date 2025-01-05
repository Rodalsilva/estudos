# Programa que lê três valores inteiros e diferentes e os mostra em ordem decrescente.

a = int(input("Digite um valor inteiro para A: "))
b = int(input("Digite um valor inteiro para B: "))
c = int(input("Digite um valor inteiro para C: "))
if a < b and b < c:
    print(c, b, a)
elif a < c and c < b:
    print(b, c, a)
elif c < a and a < b:
    print(b, a, c)
elif c < b and b < a:
    print(c, b, a)
elif b < c and c < a:
    print(a, c, b)
elif b < a and a < c:
    print(c, a, b)

    






 
