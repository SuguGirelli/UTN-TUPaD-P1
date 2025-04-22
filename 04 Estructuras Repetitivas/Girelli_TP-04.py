#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

n = 0
for n in range(101):
    print(n)
    n += 1

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene

numero = int(input("Por favor ingrese un numero entero: "))
digitos = len(str(abs(numero)))

print("El numero ingresado tiene",digitos,"digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Por favor ingrese un numero: "))
numero2 = int(input("Por favor ingrese un segundo numero: "))

suma = 0

if numero1 < numero2:
    for n in range (numero1+1,numero2):
        suma += n
elif numero2 < numero1:
    for n in range (numero2+1,numero1):
        suma += n
else:
    print("Ambos numeros son iguales por lo tanto no hay numeros para sumar.")
print(f"La suma de los numeros enteros comprendidos entre {numero1} y {numero2} es: {suma}.")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

a = 0

while True:
    numero = int(input("Por favor ingrese un numero para sumar (ingrese 0 para finalizar la suma): "))
    if numero == 0:
        break
    a += numero
print(f"La suma total de los numeros ingresados es de: {a}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio = random.randint(0,9)
num_intentos = 0

while True:
    a = int(input("Adivina en que número estoy pensando. Ingrese un número entre 0 y 9: "))
    num_intentos += 1
    if a == numero_aleatorio:
        print(f"Adivinaste, el número en el que estaba pensado era {a} y solo te tomo {num_intentos} intento(s).")
        break
    else:
        print("Intenta con otro número.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for n in range(100,-1,-2):
    print(n)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Por favor escriba un número positivo:"))
suma = 0

if numero < 0:
    print("El numero ingresado no es un número positivo")
else:
    for n in range (0+1,numero):
        suma += n

print(f"La suma de los números comprendidos entre 0 y {numero} es de {suma}.")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par = 0
impar = 0
negativo = 0
positivo = 0

for n in range(100):
    numero = int(input("Por favor ingrese un número: "))

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    if numero <0:
        negativo += 1
    elif numero > 0:
        positivo += 1
print("En los números ingresado encontramos: ")
print(f"{par} número(s) par.")
print(f"{impar} número(s) impar.")
print(f"{negativo} número(s) negativo(s).")
print(f"{positivo} número(s positivo(s).")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

suma = 0

cantidad_numeros = 10

for n in range(cantidad_numeros):
    numero = int(input(f"Ingrese un número entero: "))
    suma += numero

media = suma/cantidad_numeros
print(f"La media de los números ingresados es de {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número por favor: ")

numero2 = ""

for n in range(len(numero) -1,-1,-1):
    numero2 += numero[n]
print(f"El número que se ah ingresado es {numero} y al invertirlo nos que {numero2}.")