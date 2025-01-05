# Regra da sociedade

sócio_A = float(input("Digite o valor do investimento do sócio A: "))
sócio_B = float(input("Digite o valor do investimento do sócio B: "))
sócio_C = float(input("Digite o valor do investimento do sócio C: "))
lucro = float(input("Digite o valor do lucro a ser distribuído pelos sócios: "))
soma_investimento = sócio_A + sócio_B + sócio_C
k = lucro/soma_investimento
retorno_A  = sócio_A*k
retorno_B  = sócio_B*k
retorno_C  = sócio_C*k
print(f"O sócio A recebeu R${retorno_A}, B recebeu R${retorno_B} e C recebeu R${retorno_C}.")
