# Programa que calcula as variações percentuais sucessiva a partir de um dicionário

# Programa que calcula os valores das variações percentuais sucessivas.

tabela = {"Julho": 298,
          "Agosto": 329,
          "Setembro": 283,
          "Outubro": 319,
          "Novembro": 302}
v = list(tabela.values())
n = len(v)
x = 0
j = [0, 0]
while x < n:
    if x > 0:
        j[x] = (v[x]/v[x-1])-1
        if x == n-1:
            j[x] = (v[x]/v[x-1])-1
            break
        else:
            j.append(0)
    x = x + 1
u = list(tabela.keys())
z = 0
while z < len(u)-1:
    print(f"A variação percentual entre {u[z]} e {u[z+1]} é {j[z+1]: 5.2f}")
    z = z + 1

# Acima, utilizamos tabela.values() e tabela.keys() para obtermos apenas, em cada objeto,
# as sequências de valores e chaves, respectivamente.
# A função list transforma o objeto dado em seu parâmetro em uma lista.

