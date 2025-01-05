# Programa que cria perfis em notas de alunos
# Funciona apenas quando o número de alunos não é maior que 2
# Precursor do programa Listas de listas

L = []
x = 0
n = int(input("Digite o número de alunos da turma: "))
while x < n:  # Nesta etapa, vamos fazer com que cada item da lista L seja uma nova lista
    L.append(0)
    L[x]=[]
    x = x+1
y = 0
while y < len(L): # Nesta etapa, está sendo atribuído o valor 0 ao item da lista L[y]
    L[y].append(0)
    y = y + 1
# Ex.: n = 2 => [[0], [0]]

z = 0
while z < len(L[0]):  # z = 0 < 1 = len(L[0]) => 
    L[z].append(0)    # (adição de mais um 0 a lista L[0]) => L[0] = [0, 0].
                      # Ou seja, obtemos L = [L[0], L[1]]= [[0,0], [0]].
                      # Após a operação acima, também é acessado o elemento de índece 0 de L[1].
                      # Portanto, quando se tem o comando L[z].append()
                      # vê-se que o método append acessará todos os elementos de índices de z,
                      # ainda que tais elementos sejam listas dentro de listas.
                      # Assim, L = [L[0], L[1]] = [[0,0], [0, 0]]
    z = z + 1         # Aqui o valor de z é atualizado para 1.
                      # Temos agora que len(L[0])= len([0, 0]) = 2.
                      # Segue-se que z = 1 < 2 = len(L[0]) => L[1] = [0, 0].
                      # Atualiza-se novamente o valor de z. Obtemos z = 2.
                      # Segue-se então que z = 2 == len(L[0]).
                      # Não há previsão de comportamento do conjunto de instruções para este caso.
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

L[0][0] = float(input("Digite um valor para N1 do aluno 1: "))
L[0][1] = float(input("Digite um valor para N2 do aluno 1: "))
L[0][2] = float(input("Digite um valor para N3 do aluno 1: "))
L[0][3] = float(input("Digite um valor para N4 do aluno 1: "))

L[1][0] = float(input("Digite um valor para N1 do aluno 2: "))
L[1][1] = float(input("Digite um valor para N2 do aluno 2: "))
L[1][2] = float(input("Digite um valor para N3 do aluno 2: "))
L[1][3] = float(input("Digite um valor para N4 do aluno 2: "))
                

print("-"*20)
    
print(f"Notas do aluno 1: {L[0]}")
print(f"Notas do aluno 2: {L[1]}")

print(L)       
    

            
        
    




    


