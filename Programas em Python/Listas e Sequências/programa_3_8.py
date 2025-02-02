import programa_3_5

L = programa_3_5.progressao_aritmetica("Digite um valor para o primeiro termo:",
                                       "Digite um valor para a razão de progressão:",
                                       "ATENÇÃO! Digite um inteiro n > 2 para o número de termos:")

R = L[1]-L[0]
v = float(input("Digite o valor do último termo: "))
if v%R == 0:
    x = 0
    while x < len(L):
        if L[x+2] == v:
            N = x + 3
            break
        elif L[x+2] < v:
            L.append(0)
            L[x+3] = L[x+2]+R
        x = x + 1
SomaN = (N*(L[0]+L[N-1]))/2
print(f"Temos que a soma do número de termos desta P.A. é:")
print(f"S_{N} = {SomaN}")

