
def lista_de_2_listas(n):
    L = []
    x = 0
    
    while x < n:  
        L.append(0)
        L[x]=[]
        x = x+1
    y = 0
    while y < len(L): 
        L[y].append(0)
        y = y + 1


    z = 0
    while z < len(L[0]):   
        L[z].append(0)
        z = z + 1         
                     
    if z == len(L[n-1]):
        w = 1
        while n - w >= 0:
            L[n-w].append(0)
            w = w + 1
            if len(L[n - 1]) < m:
                a = 1
                while n - a >= 0:
                    L[n-a].append(0)
                    a = a + 1
    i = 0
    while i < n:
        j = 0
        while j < m:
            L[i][j] = float(input(f"Digite um valor para N{j + 1} do conjunto {i + 1}: "))
            if i == n:
                break
            j = j + 1
        i = i + 1
    return L

    
    










    



  


