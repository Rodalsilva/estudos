Algoritmo "glicose"

Var

glicose: real
classifica: caractere

Inicio

escreva("Digite a medida da glicose: ")
leia(glicose)
se glicose > 100 então
   se glicose <= 140 então
      classifica <- "Elevado"
   senão
      classifica <- "Diabetes"
   fimse
senão
   classifica <- "Normal"
fimse
escreva("Classificação: ", classifica)

Fimalgoritmo