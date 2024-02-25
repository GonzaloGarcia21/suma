print("Ingrese datos numericos para sumar dos valores a + b:")


while True:
    try:
        a = int(input("Dime el primer valor?"))
        b = int(input("Dime el segundo valor?"))
        break

    except ValueError:
        print("Uno o mas valores no son numericos. Intenta de nuevo")

suma = int(a + b)
print("El resultado de la suman entre", a, "+", b, "es =", suma)
