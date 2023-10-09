

print("Bienvenido a Odd or Even")
print("¿Quiere saber si un numero entre el 1 y 1000 es par o impar?")
numero = int(input("Ingrese un número: "))

if (numero >= 1 and numero <=1000):
    print("Número válido")
    if (numero % 2 == 0):
        print(numero, "es par")
    else:
         print(numero, "es impar")
else:
    print("Número fuera del límite 1 - 1000")



