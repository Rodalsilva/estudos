
    
    
P = input("Digite um primeiro valor:")
R = input("Digite um segundo valor:")
I = input("Digite um terceiro valor:")
a = [0, 0]
a[1] = float(P)
r = float(R)
i = int(I)
n = 1
while n < i+1:
    if n > 1:
        a.append(0)
        a[n] = a[1] + (n-1)*r
    n = n + 1
print(a)
  









    



  


