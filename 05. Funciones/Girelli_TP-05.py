import funciones

#Hola Mundo
funciones.imprimir_hola_mundo()

#Saludar Usuario:
nombre = input("Ingrese un nombre: ")
funciones.saludar_usuaruio(nombre)

#Informacion personal:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su recidencia: ")

funciones.informacion_personal(nombre, apellido, edad, residencia)

#area y perimetro:
radio = float(input("Ingrese el radio de un circulo para calcular su area y perimetro: "))

area = funciones.calcular_area_circulo(radio)
perimetro = funciones.calcular_perimetro_ciruclo(radio)

print(f"El area del ciruclo con un radio de {radio} es de {area}m2 y su perimetro de {perimetro} metros.")

#Segundos en horas
segundos = float(input("Ingrese la cantidad de segundos que desea pasar a horas: "))

horas = funciones.segundos_a_horas(segundos)
print(f"Los cantidad de {segundos} segundos equivalen a {horas}hs.")

#Tabla de multiplicar
numero = int(input("Ingrese un numero y mostraremos su tabla: "))
funciones.tabla_multiplicar(numero)

#Op basicas
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese un segundo número: "))

resultados = funciones.operaciones_basicas(num1, num2)

print("Resultados de las operaciones basicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#IMC
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = funciones.calcular_IMC(peso, altura)

print(f"Su indice de masa corporal es de: {imc}")

#De C° a F°
celsius = float(input("Por favor ingrese la temperatura acutal en grados celsius (C°): "))
fahrenheit = funciones.celsius_a_fahrenheir(celsius)

print(f"La temperatura celsius: {celsius} ingresadad equivale a {fahrenheit} grados fahrenheit F°.")


#Promedio
nota1 = int(input("Ingrese su primer nota: "))
nota2 = int(input("Ingrese su segunda nota: "))
nota3 = int(input("Ingrese su tercer nota: "))

notafinal = funciones.calcular_promedio(nota1, nota2, nota3)

print(f"Su promedio entre las tres notas es de: {notafinal}")