import programa_3_5


L = programa_3_5.progressao_aritmetica("Digite um valor para o primeiro termo:", "Digite um valor para a razão de progressão:", "Digite um valor para o número de termos:")
v = float(input("Digite um número a pesquisar: "))
x = 0
for e in L:
    if e != v:
        if x >= len(L)-1:
            print("Elemento não encontrado.")
    else:
        e == L[x]
        print(f"O elemento {L[x]} foi encontrado na posição {x + 1}.")
    x += 1
