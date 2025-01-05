# Buscador linear

A = [1, 2, 3, 4, 5]
n = len(A) # A função len retorna um valor igual ao número de elementos da lista
k = int(input("Digite um número inteiro de 1 a 5: "))
i = 0
while i < n:
    if A[i] == k:
        print(f"O valor buscado está na posição {i} da lista")
    i = i + 1



