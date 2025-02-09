import math

x = float(input("Digite um valor para o parâmetro da função seno: "))
n = int(input("Digite o número de termos da sequência: "))
L = [0]
m = 0
while m < n:
    L.append(0)
    L[m] = math.sin(x+m*math.pi)
    m = m + 1
print(L)











        

