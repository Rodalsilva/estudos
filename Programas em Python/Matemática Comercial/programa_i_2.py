# Programa que avalia o custo e benefício do consumo do álcool ou da gasolina.

consumo_álcool = float(input("Digite o valor do consumo do álcool por litro: "))
consumo_gasolina = float(input("Digite o valor do consumo do álcool por litro: "))
# O veículo A consome 1 litro de álcool como combustível a cada 8 km percorridos,
# enquanto o veiculo B consome gasolina na proporção de 12 km por litro
distância_A = 8
distância_B = 12
distância_viagem = float(input("Digite o valor da distância em km que será percorrida: "))
litro_A = distância_viagem/distância_A # Nos dá a quantidade em litros de álcool necessária para empreender a viagem
litro_B = distância_viagem/distância_B # Nos dá a quantidade em litros de gasolina necessária para empreender a viagem
valor = float(input("Digite o valor disponível para a compra de combustível: "))
litro_álcool = valor/consumo_álcool # Nos dá a quantidade em litros de álcool disponível com o valor que temos para compra
litro_gasolina = valor/consumo_gasolina # Nos dá a quantidade em litros de gasolina disponível com o valor que temos para compra

if valor > litro_B * consumo_gasolina:
    if consumo_álcool < consumo_gasolina:
        if litro_álcool >= litro_A:
            print("É mais vantajoso abastecer o carro com álcool")
        else:
            acréscimo_álcool = litro_A - litro_álcool
            print(f"É necessário abastecer mais {acréscimo_álcool: 5.2f} de álcool para empreender esta viagem")
            if litro_gasolina >= litro_B and litro_gasolina < litro_álcool+acréscimo_álcool:
                print("É mais vantajoso abastecer o carro com gasolina")
    else:
        print("É mais vantajoso comprar gasolina")
else:
    print("Valor insuficiente para empreender a viagem")


    





