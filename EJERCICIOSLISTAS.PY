#1.Desarrollar un algoritmo que determine si una matriz es magica.
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

#2.Desarrollar un algoritmo que imprima de manera ascendente los valores de un diccionario.
y = input("Ingresa cinco numeros en desorden: ").split()
dic = {}  
for i in y:
    dic[i] = int(i) 
valores = sorted(dic.values())
print("Numeros en orden ascendente:", valores)

dic1 = {"a": 11, "b": 2}
dic2 = {"a": 1, "b": 2, "c": 3}
f=True
for clave, valor in dic1.items():
    if clave not in dic2 or dic2[clave] != valor:
       f=False
if f:
    print("Todas las claves y valores de dic1 están en dic2.")
else:
    print("No todas las claves y valores de dic1 están en dic2.")
        
#3.Desarrollar un algoritmo que verifique si todas las clave:valor de un diccionario se encuentran en otro diccionario.
dic1 = {"a": 11, "b": 2}
dic2 = {"a": 1, "b": 2, "c": 3}
f=True
for clave, valor in dic1.items():
    if clave not in dic2 or dic2[clave] != valor:
       f=False
if f:
    print("Todas las claves y valores de dic1 están en dic2.")
else:
    print("No todas las claves y valores de dic1 están en dic2.")
#4.Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle
dic1 = eval(input("Ingrese el primer diccionario: "))
dic2 = eval(input("Ingrese el segundo diccionario: "))

dic3 = dic2.copy()
dic3.update(dic1)

print("\nDiccionario resultante:")
print(dic3)

#5.Desarrollar un programa que dada una listas de personas,imprima los nombres y apellidos 
#de las personas que estan en un rango de edades.
n = int(input("¿Cuántas personas desea ingresar? "))

personas = []

for i in range(n):
    print(f"Persona {i+1}:")
    nombre = input("Ingrese los nombres: ")
    apellido = input("Ingrese los apellidos: ")
    edad = int(input("Ingrese la edad: "))

    personas.append({"nombres": nombre,"apellidos": apellido,"edad": edad})

edadmin = int(input("Ingrese la edad mínima: "))
edadmax = int(input("Ingrese la edad máxima: "))

print(f"\nPersonas con edades entre {edadmin} y {edadmax} años:")

for persona in personas:
    if edadmin <= persona["edad"] <= edadmax:
        print(persona["nombres"], persona["apellidos"])

