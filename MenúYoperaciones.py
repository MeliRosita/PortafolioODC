def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    return num1 / num2

def multiplicacion(num1, num2):
    return num1 * num2

def binario_a_decimal(binario):
    try:
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return "Entrada no válida"

def decimal_a_binario(decimal):
    try:
        binario = bin(decimal).replace("0b", "")
        return binario
    except ValueError:
        return "Entrada no válida"

while True:
    print("Menú Principal: ")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - División")
    print("4 - Multiplicación")
    print("5 - Conversión de binario a decimal")
    print("6 - Conversión de decimal a binario")
    print("0 - Salir")

    menuprincipal = int(input("Elija una opción: "))

    if menuprincipal == 0:
        print("Saliendo del programa...")
        break
    elif menuprincipal == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = suma(num1, num2)
        print(f"Resultado de la suma: {resultado}")
    elif menuprincipal == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = resta(num1, num2)
        print(f"Resultado de la resta: {resultado}")
    elif menuprincipal == 3:
        num1 = float(input("Ingrese el numerador: "))
        num2 = float(input("Ingrese el denominador: "))
        resultado = division(num1, num2)
        print(f"Resultado de la división: {resultado}")
    elif menuprincipal == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(num1, num2)
        print(f"Resultado de la multiplicación: {resultado}")
    elif menuprincipal == 5:
        binario = input("Ingrese un número binario: ")
        resultado = binario_a_decimal(binario)
        print(f"Resultado de la conversión a decimal: {resultado}")
    elif menuprincipal == 6:
        decimal = int(input("Ingrese un número decimal: "))
        resultado = decimal_a_binario(decimal)
        print(f"Resultado de la conversión a binario: {resultado}")
    else:
        print("Opción no válida, escriba un número del 0 al 6")
