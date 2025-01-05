# Listas de listas - Programa que transforma os elementos de uma lista em listas
# O programa foi projetado para funcionar quando o número de elementos da lista inicial L for maior que 2

L = []
x = 0
n = int(input("Digite o número de conjuntos: "))
while x < n:  # Nesta etapa, vamos fazer com que cada item da lista L seja uma nova lista
    L.append(0)
    L[x]=[]
    x = x+1
y = 0
while y < len(L): # Nesta etapa, está sendo atribuído o valor 0 ao item da lista L[y]
    L[y].append(0)
    y = y + 1

# Fazendo n = 3, obtemos como resultado a lista L = [[0], [0], [0]].
# Seja z o número de índice da lista L[n - m], isto é, z = n - m, com m = 1, 2 ou 3.
# Assim, por exemplo, para m = 3, z é o índice 0 de lista L[0].
# Inicialmente, façamos z = 0.
# Enquanto z for menor que card(L[0]), vamos adicionar mais um elemento a lista L[0].
# Adição de novos elementos será pelo método append.

z = 0
while z < len(L[0]):   # z = 0 < 1 = len(L[0]) => 
    L[z].append(0)     # (adição de mais um 0 a lista L[0]) => L[0] = [0, 0].
                       # Ou seja, obtemos L = [L[0], L[1], L[2]]= [[0,0], [0], [0]].
    z = z + 1          # Aqui o valor de z é atualizado para 1.
                       # Temos agora que len(L[1])= len([0, 0]) = 2.
                       # Segue-se que z = 1 < 2 = len(L[0]) => L[1] = [0, 0].
                       # Assim, até aogora, temos L = [L[0], L[1], L[2]]= [[0,0], [0, 0], [0]]
                       # Atualiza-se novamente o valor de z. Obtemos z = 2.
                       # Segue-se então que z = 2 == len(L[0]).
                       # Não há previsão de comportamento neste conjunto de instruções para este caso.
                       # Vamos então testar a estrutura de decisão if.
if z == len(L[0]):
    L[len(L[0])].append(0)
    if n > 3:
        k = 0
        while 3 + k < n:
            L[3+k].append(0)
            k = k + 1
            
if z == len(L[n-1]):
    w = 1
    while n - w >= 0:
        L[n-w].append(0)
        w = w + 1
        if len(L[n - 1]) < 4:
            a = 1
            while n - a >= 0:
                L[n-a].append(0)
                a = a + 1
i = 0
while i < n:
    j = 0
    while j <= 3:
        L[i][j] = float(input(f"Digite um valor para N{j + 1} do conjunto {i + 1}: "))
        if i == n:
            break
        j = j + 1
    i = i + 1

print(f"Notas do aluno 1: {L[0]}")
print(f"Notas do aluno 2: {L[1]}")
print(f"Notas do aluno 3: {L[2]}")
print(L)

