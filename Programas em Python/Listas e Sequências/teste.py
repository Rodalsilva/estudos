# Cálculo do n-ésimo termo de uma PG

a = [0, 0]
a[1] = float(input("Digite um valor real para o primeiro termo da sequência: "))
q = float(input("Digite um valor real para a razão da progressão: "))
i = int(input("Digite o número de termos desta sequência: "))
n = 1
while n < i+1:
    if n > 1:
        a.append(0)
        a[n] = a[1]*q**(n-1)
    n = n + 1
j = int(input(f"Digite o índice menor que {i} relativo a posição do termo que deseja obter: "))
print(f"Temos a[{j}] = {a[j]}")











        

