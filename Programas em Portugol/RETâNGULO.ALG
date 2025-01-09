Algoritmo "retângulo"

Var

base, altura, AREA, PERIMETRO, DIAGONAL : real
quadrado_base, quadrado_altura, soma : real

Inicio

    escreva("Digite a medida da base do retângulo: ")
    leia(base)
    escreva("Digite a medida da altura do retângulo: ")
    leia(altura)
    AREA <- base*altura
    PERIMETRO <- 2*base+2*altura
    quadrado_base <- Exp(base, 2)  //Uso do código Exp(x, y) para cálculo da
    quadrado_altura <- Exp(altura, 2)//das potências dos valores das variáveis
                                     // base e altura, elevadas ao quadrado.
    soma <- quadrado_base + quadrado_altura
    
    DIAGONAL <- RaizQ(soma) // Uso do código RaizQ para se obter o valor da
                            // raiz quadrada do valor da variável soma.
    escreval(PERIMETRO)
    escreva(DIAGONAL)


Fimalgoritmo