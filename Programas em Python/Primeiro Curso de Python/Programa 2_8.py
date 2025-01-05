# Programa que determina a classificação de um produto

n = int(input("Digite um número inteiro: "))
if n == 1:
    print("Alimento não perecível")
elif n >= 2 and n <=4:
    print("Alimento perecível")
elif n == 5 or n == 6:
    print("Vestuário")
elif n == 7:
    print("Higiene pessoal")
elif n >= 8 and n <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido")
