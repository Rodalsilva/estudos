Algoritmo "ret�ngulo"

Var

base, altura, AREA, PERIMETRO, DIAGONAL : real
quadrado_base, quadrado_altura, soma : real

Inicio

    escreva("Digite a medida da base do ret�ngulo: ")
    leia(base)
    escreva("Digite a medida da altura do ret�ngulo: ")
    leia(altura)
    AREA <- base*altura
    PERIMETRO <- 2*base+2*altura
    quadrado_base <- Exp(base, 2)  //Uso do c�digo Exp(x, y) para c�lculo da
    quadrado_altura <- Exp(altura, 2)//das pot�ncias dos valores das vari�veis
                                     // base e altura, elevadas ao quadrado.
    soma <- quadrado_base + quadrado_altura
    
    DIAGONAL <- RaizQ(soma) // Uso do c�digo RaizQ para se obter o valor da
                            // raiz quadrada do valor da vari�vel soma.
    escreval(PERIMETRO)
    escreva(DIAGONAL)


Fimalgoritmo