# Función de ejemplo: Doble de un número
def doble(x):
    return x * 2

# Función de ejemplo: Filtrar números pares
def es_par(x):
    return x % 2 == 0

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizando la función map para aplicar la función doble a cada elemento de la lista
dobles = list(map(doble, numeros))
print("Dobles:", dobles)

# Utilizando la función filter para obtener los números pares de la lista
pares = list(filter(es_par, numeros))
print("Números pares:", pares)

# Utilizando la función lambda con map para duplicar cada elemento de la lista
dobles_lambda = list(map(lambda x: x * 2, numeros))
print("Dobles con lambda:", dobles_lambda)

# Utilizando la función lambda con filter para obtener los números pares de la lista
pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares con lambda:", pares_lambda)