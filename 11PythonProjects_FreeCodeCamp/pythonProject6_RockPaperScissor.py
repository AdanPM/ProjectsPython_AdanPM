from random import randint
compu = randint(1,3)

print("- - Bienvenido a Piedra, Papel o Tijeras - -")
valido=0
while valido==0:
    eleccion = int(input("1.- Piedra\n2.- Papel\n3.- Tijeras\nSeleccione su opción: "))
    if(eleccion==1 or eleccion==2 or eleccion==3):
        if eleccion==1:
            txteleccion="Piedra"
        elif eleccion==2:
            txteleccion="Papel"
        elif eleccion==3:
            txteleccion="Tijeras"
        valido=1
    else:
        print("Seleccione un numero válido (1 al 3)")

if compu==1:
    eleccioncompu="Piedra"
elif compu==2:
    eleccioncompu="Papel"
elif compu==3:
    eleccioncompu="Tijeras"

print("La computadora eligió: "+eleccioncompu)
print("Tu elección: "+txteleccion)

if compu == eleccion:
    print("E M P A T E")
elif compu==1 and eleccion==3 or compu==2 and eleccion==1 or compu==3 and eleccion==2:
    print("PERDISTE")
elif eleccion==1 and compu==3 or eleccion==2 and compu==1 or eleccion==3 and compu==2:
    print("GANASTE")
