print("__________________________________")
print("Lista - suma todos")
print("__________________________________")

# Solicitar un número final de la lista
num1 = int(input("Ingrese un Número hasta 100: "))

# Crear la lista del 1 hasta num1
lista = list(range(1, num1 + 1))

# Calcular la suma
resultado = sum(lista)

# Mostrar el resultado
print(f"La suma de la lista hasta {num1} es {resultado}")
