#3 números enteros y determine el mayor.
a =int(input("Ingrese el primer numero:  "))
b =int(input("Ingrese el segundo numero:  "))
c =int(input("Ingrese el tercer numero:  "))
if a > b and c < a:
    mayor = f"el mayor es {a}"
elif b > a and c < b:
    mayor = f"el mayor es {b}"
elif c > a and b < c:
    mayor = f"el mayor es {c}"
else:
    mayor =" son todos iguales"
print(mayor) 