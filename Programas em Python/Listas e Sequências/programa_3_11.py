import programa_3_10
import math

L = programa_3_10.progressao_geometrica("Digite um valor para o primeiro termo:",
                                       "Digite um valor para a razão de progressão:",
                                       "ATENÇÃO! Digite um inteiro n > 2 para o número de termos:")
Q = L[2]/L[1]
S = L[1]*((math.pow(Q, len(L)-1) - 1)/(Q - 1))
V = L[1:]
print(f"A soma dos termos da sequência {V} é:")
print(f"S_{len(V)} = {S}")
