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
    quadrado_base <- Exp(base, 2)
    quadrado_altura <- Exp(altura, 2)
    soma <- quadrado_base + quadrado_altura
    
    DIAGONAL <- RaizQ(soma)
    escreval(PERIMETRO)
    escreva(DIAGONAL)


Fimalgoritmo