Algoritmo "medida e pre�o de um terreno"

Var

largura_terreno, comprimento_terreno, valor_metro2 : real
area_terreno, preco_terreno : real

Inicio

escreval("Digite o valor da medida da largura do terreno: ")
leia(largura_terreno)
escreval("Digite o valor da medida do comprimento do terreno: ")
leia(comprimento_terreno)
escreval("Digite o valor do pre�o do terreno: ")
leia(valor_metro2)
area_terreno <- largura_terreno*comprimento_terreno
preco_terreno <- area_terreno*valor_metro2
escreval("A �rea do terreno � ", area_terreno:8:2, " metros quadrados")
escreval("O valor do pre�o do terreno � ", preco_terreno:8:2, " reais")

Fimalgoritmo