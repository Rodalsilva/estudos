Algoritmo "dardo"

Var

a, b, c: real

Inicio

escreva("Escreva o valor da primeira distância: ")
leia(a)
escreva("Escreva o valor da segunda distância: ")
leia(b)
escreva("Escreva o valor da terceira distância: ")
leia(c)

se a >= b então
	se c >= a então
		escreva("MAIOR DISTANCIA = ", c)
	senão
		escreva("MAIOR DISTANCIA = ", a)
	fimse
senão
	se c >= b então
		escreva("MAIOR DISTANCIA = ", c)
	senão
		escreva("MAIOR DISTANCIA = ", b)
	fimse
fimse


Fimalgoritmo