# Programa que atribui uma classificação aos nadadores segundo sua idade

nadador_idade = int(input("Digite a idade do nadador: "))
if nadador_idade >= 5 and nadador_idade <= 7:
    print("Infantil A")
elif nadador_idade >= 8 and nadador_idade <= 10:
    print("Infantil B")
elif nadador_idade >= 11 and nadador_idade <= 13:
    print("Juveinil A")
elif nadador_idade >= 14 and nadador_idade <= 17:
    print("Juveinil B")
elif nadador_idade >= 18:
    print("Adulto")
