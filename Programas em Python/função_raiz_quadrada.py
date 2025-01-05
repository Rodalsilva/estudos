import raiz_de_n_par

n = int(input("Digite um valor: "))
def épar(n):
    return n % 2 == 0
def par_ou_ímpar(n):
    if épar(n):
        return raiz_de_n_par.raiz_par(n)
    else:
        return "ímpar"
print(f"A parte inteira da raiz quadrada de {n} é igual a {par_ou_ímpar(n)}")
