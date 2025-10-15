entrada = input("Ingrese los números separados por espacios: ") # El usuario ingresa los números
numeros = list(map(int, entrada.split())) # Se crea una lista de los números ingresados por el usuario
print(f"Sus número son {numeros}") # Se imprime una lista de los números ingresados
def sumar(numeros): # Se define una función para sumar los números de la lista
    total = 0
    for num in numeros:
        total += num
    return total
print("La suma de la lista es: ", sumar(numeros)) # Se imprime la suma de los números de la lista
print("El promedio de la lista es: ", sumar(numeros)/len(numeros)) # Se imprime el promedio de los números de la lista
grande = max(numeros) # Función para encontrar el número más grande de la lista
pequeño = min(numeros)# Función para encontrar el número más pequeño de la lista
print(f"El número más grande de la lista es: {grande}") # Se imprime el número más grande
print(f"El número más pequeño de la lista es: {pequeño}") # Se imprime el número más pequeño
