Algoritmo "glicose"

Var

glicose: real
classifica: caractere

Inicio

escreva("Digite a medida da glicose: ")
leia(glicose)
se glicose > 100 ent�o
   se glicose <= 140 ent�o
      classifica <- "Elevado"
   sen�o
      classifica <- "Diabetes"
   fimse
sen�o
   classifica <- "Normal"
fimse
escreva("Classifica��o: ", classifica)

Fimalgoritmo