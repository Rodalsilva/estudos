# Programa 3.6 modificado para se apresentar como função.

def pesquisa_PA(L, v):
    x = 0
    for e in L:
        if e != v:
            if x >= len(L)-1:
                return "Elemento não encontrado."
        else:
            e == L[x]
            return x + 1
            break
        x += 1
