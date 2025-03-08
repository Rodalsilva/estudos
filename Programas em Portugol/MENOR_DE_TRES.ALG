Algoritmo "menor_de_tres"

Var

a, b, c: inteiro

Inicio

  escreva("Digite um primeiro número: ")
  leia(a)
  escreva("Digite um segundo número: ")
  leia(b)
  escreva("Digite um terceiro número: ")
  leia(c)
  // Podemos ter (a > b) => (a > b > c) ou (a > c > b) ou (c > a > b) ou
  //(b > a) => (b > a > c) ou (b > c > a) ou (c > b > a)
  
  se a > b então
     se b > c então
        escreva("Temos ", c," como o menor valor")
     senão
        escreva("Temos ", b," como o menor valor")
     fimse
  fimse
  se b > a então
     se a > c então
        escreva("Temos ", c," como o menor valor")
     senão
        escreva("Temos ", a," como o menor valor")
     fimse
  fimse
  


Fimalgoritmo