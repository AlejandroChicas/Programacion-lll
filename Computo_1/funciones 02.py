
print("----------------------------------")
print("Josue Chicas")
print("USTR026016")
print("----------------------------------")

# crear función
def evaluar_numero(num):
    if num > 0:
        return "El número es positivo"
    elif num < 0:
        return "El número es negativo"
    else:
        return "El número es 0"

# solicitar número al usuario
num = int(input("Introduce un número: "))

# mostrar resultado
print(evaluar_numero(num))
