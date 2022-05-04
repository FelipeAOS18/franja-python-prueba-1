#2) Escribir un programa que le pregunte al usuario una cantidad a invertir, 
# el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión
#  redondeado a dos decimales.

print("Cuanto deseas invertir ingrese la cantidad")
c=int(input(" "))
print("Ingrese la cantidad de años:")
a=int(input(" "))
print("El interes:")
i=float(input(" "))

cf= c*((i/100)+1)**a
cf=str(cf)
print("Capital Final esperado es de: "+cf+"")