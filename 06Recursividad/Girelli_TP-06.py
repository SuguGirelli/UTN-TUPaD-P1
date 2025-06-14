from funciones import factorial, fibonacci, potencia, decimal_a_binario, es_palindromo, suma_digitos, contar_bloques, contar_digito



# Ejercicio 1
numero = int(input("1- Ingrese un numero: "))

for i in range(1, numero + 1):    print(f"El factorial de {i} es: {factorial(i)}")

# Ejercicio 2
numero = int(input("2- Ingrese un numero: "))
print("Serie de Fibonacci:")
for i in range(numero + 1):
    print(fibonacci(i), end=" ")
print()

# Ejercicio 3
base = int(input("3- Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"La potencia de {base} elevado a {exponente} es: {potencia(base, exponente)}")

# Ejercicio 4
numero = int(input("4- ingrese un numero decimal: "))
print(f"El numero {numero} en binario es: {decimal_a_binario(numero)}")

# Ejercicio 5
palabra = input("5- Ingrese una palabra: ").lower()
if es_palindromo(palabra):
    print("es un palíndromo.")
else:
    print("no es un palíndromo.")

# Ejercicio 6 
numero  = int(input("6- ingrese un número para suma de dígitos: " ))
print(f"La suma de digitos de {numero}  es {suma_digitos(numero)}")

# Ejercicio 7
n = int(input("7- Ingrese el número de bloques en la base de la pirámide: "))
print(f"Total de bloques: {contar_bloques(n)}")

# Ejercicio 8
numero = int(input("8- Ingrese un número: "))
digito = int(input("Ingrese dígito a buscar: "))
print(f"Apariciones del dígito {digito} en el número {numero}: {contar_digito(numero, digito)}")






