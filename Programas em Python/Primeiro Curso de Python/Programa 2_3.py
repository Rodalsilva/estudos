# Programa 2.3 (Modificado) - Cálculo da média aritmética de quatro notas bimestrais.

n1 = float(input("Digite o valor da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
n3 = float(input("Digite o valor da terceira nota: "))
n4 = float(input("Digite o valor da quarta nota: "))
soma = n1+n2+n3+n4
média = soma/4
print(média)
if média >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
