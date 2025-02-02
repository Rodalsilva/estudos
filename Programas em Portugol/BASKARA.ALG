Algoritmo "Baskara"

Var

a, b, c, delta, x1, x2: real

Inicio

escreva("Dgite um valor para a: ")
leia(a)
escreva("Digite um valor para b: ")
leia(b)
escreva("Dgite um valor para c: ")
leia(c)
delta <- Exp(b, 2) - 4*a*c
se delta < 0 então
   escreva("Esta equacao nao possui raizes reais")
senão
   x1 <- (-b + RaizQ(delta))/2*a
   escreval(x1:5:4)
   x2 <- (-b - RaizQ(delta))/2*a
   escreval(x2:5:4)
fimse

Fimalgoritmo