# Programa que calcula os valores das variações percentuais sucessivas.
y = 0
t = [0]
while y < len(t):
    t[y] = input("Digite a data da ocorrência (escreva 'pare' para parar): ")
    if t[y] == 'pare':
        break
    else:
        t.append(0)
    y = y + 1
n = len(t)-1
i = 0
v = [0]
while i <= n-1:
    v[i] = float(input(f"Digite um valor para v[{t[i]}]:" ))
    if i == n-1:
        break
    else:
        v.append(0)
    i = i + 1
#print(v)
x = 0
j = [0, 0]
while x <= n-1:
    if x > 0:
        j[x] = (v[x]/v[x-1])-1
        if x == n-1:
            break
        else:
            j.append(0)
    x = x + 1
z = 0
while z < len(v)-1:
    print(f"A variação percentual entre {t[z]} e {t[z+1]} é {j[z+1]: 5.2f}")
    z = z + 1

    


    

    
