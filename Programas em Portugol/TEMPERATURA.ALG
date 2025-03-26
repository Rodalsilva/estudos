Algoritmo "temperatura"

Var

  temp: caractere
  F, C, T: real

Inicio

  escreva("Voce vai digitar a temperatura em qual escala (C/F): ")
  leia(temp)
  se temp = "F" então
     escreva("Digite a temperatura em Fahrenheit: ")
     leia(F)
     T <- 5*(F-32)/9
     escreva("Temperatura equivalente em Celsius:", T:4:2)
  senão
     escreva("Digite a temperatura em Celsius: ")
     leia(C)
     T <-((9/5)*C) + 32
     escreva("Temperatura equivalente em Fahrenheit:", T:4:2)
  fimse
  

Fimalgoritmo