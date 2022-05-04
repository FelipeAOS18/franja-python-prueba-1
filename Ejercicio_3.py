#3) Escribir un programa que haga transformaciones de pesos a dólares.
#  Debe preguntarle al usuario si desea transformar de pesos mexicanos a dólares, de pesos chilenos a dólares,
#  o desde pesos argentinos a dólares. Mostrar por pantalla la cantidad de monedas a convertir,
#  la moneda que se convirtió y el monto en dólares.
#Peso Chileno a dólar: 855
#Peso Mexicano a dólar: 20
#Peso Argentino a dólar: 115

print("Bienvenido al convertidor virtual")
print("Si deseas convertir de pesos mexicanos a dolares ingresa 0")
print("Si deseas converitr de pesos chilenos a dolares ingresa 1")
print("Si deseas convertir de pesos argentinos a dolares ingrese 2")
m=int(input( ))
if m==0 :
    print("Bienvenido al convertidor de pesos Mexicanos a dolares")
    print("Porfavor ingrese la cantidad que desea convertir")
    c=float(input(""))
    t=c/20
    t=str(t)
    print("Su cantidad de dolares es de $"+t+" ")
    #converitr pesos mex a dolares
elif m==1 :
    print("Bienvenido al convertidor de pesos Chilenos a dolares")
    print("Porfavor ingrese la cantidad que desea convertir")
    c=float(input(""))
    t=c/855
    t=str(t)
    print("Su cantidad de dolares es de $"+t+" ")
    #convertir pesos chil a dolares
else :
    print("Bienvenido al convertidor de pesos Argentinos a dolares")
    print("Porfavor ingrese la cantidad que desea convertir")
    c=float(input(""))
    t=c/115
    t=str(t)
    print("Su cantidad de dolares es de $"+t+" ")
    #converitr de pesos arg a dolares 
