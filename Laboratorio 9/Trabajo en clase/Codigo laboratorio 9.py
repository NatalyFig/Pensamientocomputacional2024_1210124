# ejercicio 1: pedir al usuario su edad y decirle si es mayor de edad # type: ignore
edad = int(input("ingrese su edad: "))
if edad >= 18:
   print("Debe tramitar su DPI.")
else: print("Aun no es mayor de edad.")

#ejercicio 2: Escribe un programa que pida al usuario un número e indique si es positivo o negativo.
numero = float(input("Ingrese un numero: "))
if numero > 0:
   print("El numero es positivo.")
elif numero < 0:
   print("El numero es negativo. ")
else: 
   print("El numero es 0.")

#ejercicio 3: Utilizando la estructura switch solicite un número y si este está dentro del rango 1 a 5 imprima el numero en letras, si se ingresa un número diferente debe imprimirse “número no definido”.
numero = int(input("Ingrese un numero: "))
match numero: 
   case 1: 
    print ("uno")
   case 2: 
     print ("dos")
   case 3: 
     print ("tres")
   case 4: 
     print ("cuatro")
   case 5:
     print ("cinco")
   case _:
     print ("no esiste")

# ejercicio 4: Escribe un programa que imprima la tabla de multiplicar del número 2
print("tabla de multiplicar del numero 2: ")

i = 1 
while i <= 10: 
    print("2 x"+ str (i)+ (" = ")+ str (2*i))
    i += 1