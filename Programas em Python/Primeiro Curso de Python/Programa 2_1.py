velocidade = float(input("Digite em km/h o valor da velocidade do usuário: "))
multa = (velocidade - 80)*5
if velocidade > 80:
    print(f"O usuário ultrapassou o limite de velocidade estabelecido e foi multado em R${multa:5.2f}") 

