
L = []
x = 0
while x < 2:
    L.append(0)
    L[x]=[]
    x = x+1
print(L)
y = 0
while y < len(L):
    L[y].append(0)
    y = y + 1
print(L)
z = 0
while z < len(L[0]):
    L[z].append(0)
    if z > 1:
        break
    z = z + 1
print(L)
   
    
    
 

