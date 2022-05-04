#1) Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#  Escribe un programa que comience leyendo el número de barras vendidas que no son del día.
#  Después tu programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

from this import d
print("Bienvenido a la panaderia cada una de nuestras barras de pan cuestan 3.49€")
print("Pero tambien tenemos barras de pan con un descuento del 60%, estas barras no son del día")
print("Ingrese 1 para comprar pan del dia y 2 para comprar pan que no es del día")
s=int(input("   "))
if s==1:
    print("¿Cuantas desea llevar?")
    c=float(input(" "))
    f= c*3.49
    f=str(f)
    print("Su valor a pagar es de: "+f+"€")
else:
    print("¿Cuantas desea llevar?")
    c=float(input(" "))
    f= c*3.49
    f=str(f)
    p= c*3.49
    d= p*0.6
    t=p-d
    d=str(d)
    p=str(p)
    t=str(t)
    print("Su descuento es de "+d+"€")
    print("Su valor a pagar es de: "+t+"€ sin descuento: "+f+"€")
