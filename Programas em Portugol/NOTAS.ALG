Algoritmo "Notas"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

//Problema "notas"
//Fazer um programa para ler as duas notas que um aluno obteve no primeiro
//e segundo semestres de uma disciplina anual.
//Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal)
//no ano juntamente com um texto explicativo.
//Caso a nota final do aluno seja inferior a 60.00,
//mostrar a mensagem "REPROVADO"

Var

 nota_1, nota_2, nota_final: real

Inicio

 escreval("Digite a primeira nota: ")
 leia(nota_1)
 escreval("Digite a segunda nota: ")
 leia(nota_2)
 nota_final <- nota_1 + nota_2
 
 // Segue abaixo uma estrutura de seleção composta

 se nota_final > 60 então
    escreval("Nota Final = ", nota_final:5:1)
    escreva("Aluno aprovado")
 senão
    escreval("Nota Final = ", nota_final:5:1)
    escreva("Aluno reprovado")
 fimse

Fimalgoritmo