def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def ingresar_numero_positivo(mensaje):
    while True:
        try:
            num = input(mensaje)
            if not num.isdigit():
                raise ValueError("No letras. Por favor, ingresa un número natural positivo.")
            num = int(num)
            if num <= 0:
                raise ValueError("Por favor, ingresa un número natural positivo.")
            return num
        except ValueError as e:
            print(e)

num1 = ingresar_numero_positivo("Ingresa el primer número: ")
num2 = ingresar_numero_positivo("Ingresa el segundo número: ")

print("El máximo común divisor de", num1, "y", num2, "es:", mcd(num1, num2))
