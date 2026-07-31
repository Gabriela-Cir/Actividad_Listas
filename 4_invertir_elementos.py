# Programa 4: Invierte una lista manualmente con un bucle recorriendo en reverso.

def invertir_manual(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida

# Lectura de 6 números
numeros = []
print("--- Registro de 6 números ---")
for i in range(6):
    valor = int(input(f"Número {i+1}: "))
    numeros.append(valor)

# Inversión de lista
lista_invertida = invertir_manual(numeros)

# Salida
print("\n--- Resultados ---")
print("Original:", numeros)
print("Invertida:", lista_invertida)