Algoritmo "troco_verificado"

Var

quantidade: inteiro
preco, recebido, troco: real

Inicio

escreva("Pre�o unit�rio do produto: ")
leia(preco)
escreva("Quantidade comprada: ")
leia(quantidade)
escreva("Dinheiro recebido: ")
leia(recebido)
troco <- recebido - quantidade*preco
se troco < 0 ent�o
   escreva("Dinheiro insuficiente. Faltam ", troco*(-1):5:2, " reais.")
sen�o
   escreva("TROCO = ", troco:5:2)
fimse

Fimalgoritmo