from funcao_lista_de_2_listas import lista_de_2_listas
from funcao_lista_de_listas import lista_de_listas

K = []
n = int(input("Digite o número de conjuntos: "))
m = int(input("Digite o número de elementos dos conjuntos: "))

if n <= 2:
    K = lista_de_2_listas(n)
elif n > 2:
    K = lista_de_listas(n)
print(K)
ma = 0
r = 0
while r < n:
    s = 0
    soma = 0
    while s < len(K[0]):
        soma = soma + K[r][s]
        s = s + 1
        if s > 3:
            print(f"O valor da soma N1+N2+N3+N4 do conjunto {r+1} é {soma}")
            ma = soma/m
            print(f"A média aritmética do conjunto {r+1} é igual a {ma}")
    r = r + 1






    








    
