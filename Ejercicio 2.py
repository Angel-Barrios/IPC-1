entrada = input("Ingrese los números separados por espacios: ")
numeros = list(map(int, entrada.split())) # Ingreso de los numeros del usuario
print(f"Sus número son {numeros}")
def sumar(numeros):
    total = 0
    for num in numeros:
        total += num
    return total
print("La suma de la lista es: ", sumar(numeros))
print("El promedio de la lista es: ", sumar(numeros)/len(numeros))
grande = max(numeros)
pequeño = min(numeros)
print(f"El número más grande de la lista es: {grande}")
print(f"El número más pequeño de la lista es: {pequeño}")
