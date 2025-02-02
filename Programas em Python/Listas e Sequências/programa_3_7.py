import programa_3_5

L = programa_3_5.progressao_aritmetica("Digite um valor para o primeiro termo:",
                                       "Digite um valor para a razão de progressão:",
                                       "Digite um valor para o número de termos:")
S = len(L)*(L[0]+L[len(L)-1])/2
print(S)
