# Programa 3: Encuentra el valor máximo y mínimo con funciones manuales.

def maximo_manual(lista):
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista[1:]:
        if num > maximo:
            maximo = num
    return maximo

def minimo_manual(lista):
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

# Lectura de 8 números
numeros = []
print("--- Registro de 8 números ---")
for i in range(8):
    valor = int(input(f"Número {i+1}: "))
    numeros.append(valor)

# Obtención del mayor y menor
mayor = maximo_manual(numeros)
menor = minimo_manual(numeros)

# Salida
print("\n--- Resultados ---")
print("Mayor (manual):", mayor)
print("Menor (manual):", menor)