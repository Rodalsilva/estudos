Algoritmo "medida e preço de um terreno"

Var

largura_terreno, comprimento_terreno, valor_metro2 : real
area_terreno, preco_terreno : real

Inicio

escreval("Digite o valor da medida da largura do terreno: ")
leia(largura_terreno)
escreval("Digite o valor da medida do comprimento do terreno: ")
leia(comprimento_terreno)
escreval("Digite o valor do preço do terreno: ")
leia(valor_metro2)
area_terreno <- largura_terreno*comprimento_terreno
preco_terreno <- area_terreno*valor_metro2
escreval("A área do terreno é ", area_terreno:8:2, " metros quadrados")
escreval("O valor do preço do terreno é ", preco_terreno:8:2, " reais")

Fimalgoritmo