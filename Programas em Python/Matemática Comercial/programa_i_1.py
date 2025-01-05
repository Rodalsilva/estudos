
ano_1 = int(input("Digite o ano 1 considerado: "))
ano_2 = int(input("Digite o ano 2 considerado: "))
vendas_1 = float(input(f"Digite o valor das vendas do {ano_1}: "))
vendas_2 = float(input(f"Digite o valor das vendas do {ano_2}: "))
razão = vendas_2/vendas_1
if vendas_2 > vendas_1:
    print(f"As vendas de {ano_2} são {razão} maiores que {ano_1}")
elif vendas_2 == vendas_1:
    print(f"As vendas de {ano_2} são iguais a de {ano_1}")
else:
    print(f"As vendas de {ano_2} são {razão} menores que {ano_1}")
    
