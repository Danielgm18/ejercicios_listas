#Desarrollar un algoritmo que determine si una matriz es magica.
x=list(map(int,input("Ingresa los numeros de la matriz: ").split()))
x1=list(x)
f1=sum(x[0:3])
f2=sum(x[3:6])
f3=sum(x[6:9])
col1=sum(x[0:9:3])
col2=sum(x[1:9:3])
col3=sum(x[2:9:3])
dia1=sum(x[2:7:2])
dia2=sum(x[0:9:4])
if f1 == f2 == f3 == col1 == col2 == col3 == dia1 == dia2:
    print("La matriz es mágica")
else:
    print("la matriz no es mágica")
