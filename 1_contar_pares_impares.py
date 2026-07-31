# Programa 1: Cuenta cuántos números pares e impares hay en una lista.

def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Lectura de 10 números
numeros = []
print("--- Registro de 10 números ---")
for i in range(10):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)

# Conteo y salida
cant_pares, cant_impares = contar_pares_impares(numeros)
print("\n--- Resultados ---")
print("Pares:", cant_pares)
print("Impares:", cant_impares)