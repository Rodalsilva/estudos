Algoritmo "dardo"

Var

a, b, c: real

Inicio

escreva("Escreva o valor da primeira dist�ncia: ")
leia(a)
escreva("Escreva o valor da segunda dist�ncia: ")
leia(b)
escreva("Escreva o valor da terceira dist�ncia: ")
leia(c)

se a >= b ent�o
	se c >= a ent�o
		escreva("MAIOR DISTANCIA = ", c)
	sen�o
		escreva("MAIOR DISTANCIA = ", a)
	fimse
sen�o
	se c >= b ent�o
		escreva("MAIOR DISTANCIA = ", c)
	sen�o
		escreva("MAIOR DISTANCIA = ", b)
	fimse
fimse


Fimalgoritmo