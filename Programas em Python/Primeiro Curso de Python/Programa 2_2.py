d = float(input("Digite o valor da distância a ser percorrida em Km: "))
if d <= 200:
    print(f"O preço da passagem é R${d*0.50:5.2f}")
else:
    print(f"O preço da passagem é R${d*0.45:5.2f}")
