Algoritmo "menor_de_tres"

Var

a, b, c: inteiro

Inicio

  escreva("Digite um primeiro n�mero: ")
  leia(a)
  escreva("Digite um segundo n�mero: ")
  leia(b)
  escreva("Digite um terceiro n�mero: ")
  leia(c)
  // Podemos ter (a > b) => (a > b > c) ou (a > c > b) ou (c > a > b) ou
  //(b > a) => (b > a > c) ou (b > c > a) ou (c > b > a)
  
  se a > b ent�o
     se b > c ent�o
        escreva("Temos ", c," como o menor valor")
     sen�o
        escreva("Temos ", b," como o menor valor")
     fimse
  fimse
  se b > a ent�o
     se a > c ent�o
        escreva("Temos ", c," como o menor valor")
     sen�o
        escreva("Temos ", a," como o menor valor")
     fimse
  fimse
  


Fimalgoritmo