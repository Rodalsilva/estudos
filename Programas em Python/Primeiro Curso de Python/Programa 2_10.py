preço = float(input("Digite o valor do produto: "))
pagamento = 0
concluir_compra = int(input("Digite 1 para finalizar a compra ou 0 para desistência: "))
if concluir_compra == 1:
    print("Digite 2 para pagamento à vista em dinheiro.")
    print("Digite 3 para pagamento à vista com cartão de crédito")
    print("Digite 4 para pagamento em 2 vezes")
    print("Digite 5 para pagamento em 3 vezes")
    condição = int(input("Digite o código da condição de pagamento: "))
    if condição == 2:
        print("Pagamento à vista.")
        print("Cliente recebe um desconto de 10%.")
        pagamento = preço - 0.1*(preço)
        print(f"O valor do pagamento será R${pagamento:5.2f}.")
    elif condição == 3:
        print("Pagamento à vista com cartão de crédito.")
        print("Cliente recebe um desconto de 5%.")
        pagamento = preço - 0.05*(preço)
        print(f"O valor do pagamento será R${pagamento:5.2f}.")
    elif condição == 4:
        print("Pagamento em 2 vezes.")
        print("Não há desconto.")
        pagamento = preço/2
        print(f"O valor do pagamento será R${pagamento:5.2f} em 2 vezes.")
    elif condição == 5:
        print("Pagamento em 3 vezes.")
        print("Acréscimo de juros de 10%.")
        pagamento = preço + 0.1*(preço)
        print(f"O valor do pagamento será R${pagamento:5.2f}.")
else:
    print("Cliente desistiu da compra")















