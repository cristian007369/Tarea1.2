#Programa para verificar cuál de tres número es mayor
print("-------------------------------------------------")
print("--------------------Tarea no.2-------------------")
print("-------------------------------------------------")
#imput
a=int(input("Digite un número entero: "))
b=int(input("Digite otro número entero: "))
c=int(input("lo mismo, digite un número entero: "))

#Processing y output
if a>b:
    if b>c:
        print("-------------------------------------------------")
        print(str(a) + " es mayor que " + str(b) + " es mayor que " + str(c))
        print("-------------------------------------------------")
    else:
        if c>a:
            print("-------------------------------------------------")
            print(str(c) + " es mayor que " + str(a) + " es mayor que " + str(b))
            print("-------------------------------------------------")
        else:
            print("-------------------------------------------------")
            print(str(a) + " es mayor que " + str(c) +  " es mayor que " + str(b))
            print("-------------------------------------------------")
else:
    if a>c:
        print("-------------------------------------------------")
        print(str(b) + " es mayor que " + str(a) +  " es mayor que " + str(c))
        print("-------------------------------------------------")
    else:
        if c>b:
            print("-------------------------------------------------")
            print(str(c) + " es mayor que " + str(b) +  " es mayor que " + str(a))
            print("-------------------------------------------------")
        else:
            print("-------------------------------------------------")
            print(str(b) + " es mayor que " + str(c) + " es mayor que " + str(a))
            print("-------------------------------------------------")