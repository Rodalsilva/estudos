# Programa que calcula a quantidade de horas necessárias para produzir uma quantidade fixa determinada.
# A produção é realizada com o uso de um determinado número de máquinas.
# O número de máquinas é inversamente proporcional ao número de horas.
# Partimos da suposição de que três máquinas levam 2 horas para produzir um lote de 1 000 peças.

n = int(input("Digite o número de máquinas: "))
k = 6
h = 6/n
print(f"O número de minutos necessários para a produção com {n} máquinas em operação é igual a {h*60}")

