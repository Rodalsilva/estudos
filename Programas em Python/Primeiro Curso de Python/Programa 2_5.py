
São_Paulo = 11
Rio = 21
Vitória = 27
BH = 31
origem = int(input("Digite o código da cidade da região sudeste de sua origem: "))
taxa = 0
cidade = input("Digite o nome de sua cidade: ")

if origem == 11:
    taxa = 10
elif origem == 21:
    taxa = 12
elif origem == 27:
    taxa = 12
elif origem == 31:
    taxa = 14
else:
    print(f"Desculpe, mas a cidade de {cidade} não é contemplada pelos nossos serviços.")
    
print(f"O valor da taxa aplicada para a cidade de {cidade} é de R${taxa:5.2f}.")
