# Programa 2.4 - Identificação do tipo de triângulo.

a = int(input("Digite um número inteiro para a medida do lado a: "))
b = int(input("Digite um número inteiro para a medida do lado b: "))
c = int(input("Digite um número inteiro para a medida do lado c: "))
if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        print("TriÂngulo Equilátero")
    else:
        if a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
else:
    print("Estes valores não formam um triângulo")


