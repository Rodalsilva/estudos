# Programa que determina a quantidade de quilômetros que um carro pode percorrer a partir da quantidade de litros que ele consome.
# O número de litros de gasolina que o carro consome na estrada é diretamente proporcional ao número de quilômetros percorridos.
# Sabe-se que o carro consome 5 litros para percorrer 74 quilômetros

litro_gasolina = float(input("Digite a quantidade de gasolina abastecida: "))
distância_km = 0
if litro_gasolina >= 5:
    distância_km = 74*litro_gasolina/5
print(f"A distância que o carro poderá percorrer com a quantidade {litro_gasolina} de gasolina é de até {distância_km: 5.2f} km")


