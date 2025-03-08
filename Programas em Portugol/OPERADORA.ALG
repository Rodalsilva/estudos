Algoritmo "Operadora"

Var

 minutos: inteiro
 custo: real

Inicio

      escreva("Digite a quantidade de minutos: ")
      leia(minutos)
      se minutos < 100 então
         escreva("Valor a pagar: R$ 50,00")
      senão
           custo <-  50+2*(minutos-100)
           escreva("Valor a pagar: R$ ", custo:5:2)
      fimse


Fimalgoritmo