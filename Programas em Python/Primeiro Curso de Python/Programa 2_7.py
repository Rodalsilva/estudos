nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - nascimento
if idade >= 16:
    if idade < 18:
        print("Tem idade para votar")
    elif idade >= 18:
        print("Tem idade para conseguir carteira de habilitação")
else:
    print("Menor de 16.")
