# Algoritmo para cálculo da parte inteira da raiz quadrada de um número par para números até 200

#n = int(input("Digite um valor inteiro par: "))
def raiz_par(n):
    X = (n + 1)/2
    L = [X]
    Y = int(X)
    K = [Y]
    #print(L)
    #print(K)
    if L[0] <= K[0]:
        X = L[0]
        #print(f"A parte inteira da raiz quadrada de {n} é igual a {X}")
    elif L[0] > K[0]:
        L.append(0)
        K.append(0)
        A = L[0]**2
        B = 2*L[0]
        C = A/B
        D = n/B
        L[1] = C+D
        K[1] = int(L[1])
        #print(L)
        #print(K)
        if L[1] <= K[1]:
            X = L[1]
            #print(f"A parte inteira da raiz quadrada de {n} é igual a {L[1]}")
        elif L[1] > K[1]:
            L.append(0)
            K.append(0)
            A = L[1]**2
            B = 2*L[1]
            C = A/B
            D = n/B
            L[2] = C+D
            K[2] = int(L[2])
            #print(L)
            #print(K)
            if K[2] == K[1]:
                X = K[2]
               #print(f"A parte inteira da raiz quadrada de {n} é igual a {K[2]}")
            else:
                if L[2] <= K[2]:
                    X = L[2]
                    #print(f"A parte inteira da raiz quadrada de {n} é igual a {L[2]}")
                elif L[2] > K[2]:
                    L.append(0)
                    K.append(0)
                    A = L[2]**2
                    B = 2*L[2]
                    C = A/B
                    D = n/B
                    L[3] = C+D
                    K[3] = int(L[3])
                    #print(L)
                    #print(K)
                    if K[3] == K[2]:
                        X = K[3]
                        #print(f"A parte inteira da raiz quadrada de {n} é igual a {K[3]}")
                    else:
                        if L[3] <= K[3]:
                            X = L[3]
                            #print(f"A parte inteira da raiz quadrada de {n} é igual a {L[3]}")
                        elif L[3] > K[3]:
                            L.append(0)
                            K.append(0)
                            A = L[3]**2
                            B = 2*L[3]
                            C = A/B
                            D = n/B
                            L[4] = C+D
                            K[4] = int(L[4])
                            #print(L)
                            #print(K)
                            if K[4] == K[3]:
                                X = K[4]
                            else:
                                if L[4] <= K[4]:
                                    X = L[4]
                                elif L[4] > K[4]:
                                    L.append(0)
                                    K.append(0)
                                    A = L[4]**2
                                    B = 2*L[4]
                                    C = A/B
                                    D = n/B
                                    L[5] = C+D
                                    K[5] = int(L[5])
                                    if K[5] == K[4]:
                                        X = K[5]
                                    else:
                                        if L[5] <= K[5]:
                                            X = L[5]
                                        elif L[5] > K[5]:
                                            L.append(0)
                                            K.append(0)
                                            A = L[5]**2
                                            B = 2*L[5]
                                            C = A/B
                                            D = n/B
                                            L[6] = C+D
                                            K[6] = int(L[6])
                                    
    return K[len(K)-1]
#print(raiz_par(n))    
