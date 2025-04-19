#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

a = int(input("Que edad tiene?: "))

if a >= 18:
    print("Es mayor de edad.")

#--------------------------------------------------------------------------------------------------------------------

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

b = int(input("Por favor ingrese su nota: "))

if b >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#--------------------------------------------------------------------------------------------------------------------

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

c = int(input("Por favor ingrese un numero: "))

if c % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#--------------------------------------------------------------------------------------------------------------------

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

Edad = int(input("Por favor ingrese su edad: "))

if Edad < 12:
    print("Pertenece a la categoria Niño/a.")

elif Edad >= 12 and Edad < 18:
    print("Pertenece a la categoria Adolescente.")

elif Edad >= 18 and Edad < 30:
    print("Pertenece a la categoria Adulto/a joven.")

else:
    print("Pertenece a la categoria Adulto/a mayor.")       

#--------------------------------------------------------------------------------------------------------------------

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

password = (input("Por favor ingrese una contraseña, recuerde que esta misma tiene que contener de 8 a 14 caracteres: "))

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


#--------------------------------------------------------------------------------------------------------------------

#6) #Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print("La mediana es: ",median(numeros_aleatorios))

print("La media es: ",mean(numeros_aleatorios))

print("La moda es: ",mode(numeros_aleatorios))

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgo positivo o a la derecha.")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Hay sesgo negativo o a la izquierda.")
elif mean(numeros_aleatorios) == mode(numeros_aleatorios):
    print("No hay sesgo.")



#--------------------------------------------------------------------------------------------------------------------

#7) 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.


frase = input("Ingrese una frase o una palabra: ")

if frase[-1].lower() in "aeiou":
    print(f"{frase}! ")

#--------------------------------------------------------------------------------------------------------------------

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. ")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")

numero = int(input("Ingrese la opción que desee: "))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Por favor ingrese una opcion valida")

#--------------------------------------------------------------------------------------------------------------------


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese de que magnitud fue el terremoto: "))

if magnitud < 3:
    print(f"El terremoto fue de categoria {magnitud}: Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print(f"El terremoto fue de categoria {magnitud}: Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud <5:
    print(f"El terremoto fue de categoria {magnitud}: Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print(f"El terremoto fue de categoria {magnitud}: Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print(f"El terremoto fue de categoria {magnitud}: Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print(f"El terremoto fue de categoria {magnitud}: Extremo (puede causar graves daños a gran escala).")


#--------------------------------------------------------------------------------------------------------------------

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En que hemisferio se encuentra? (N/S) ")
mes = int(input("¿En que mes estamos? (1/12) "))
dia = int(input("¿Que dia es hoy? "))

estacion = ""

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        estacion = "Invierno"
    elif (mes == 3 and dia > 21) or (3 <= mes <= 4) or (mes == 5 and dia < 21):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <21):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <21):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        estacion = "Verano"
    elif (mes == 3 and dia > 21) or (3 <= mes <= 4) or (mes == 5 and dia < 21):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <21):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <21):
        estacion = "Primavera"
print(f"Estas en {estacion}.")  