from random import randint
compu = randint(1,50)

print("- - B I E N V E N I D O - -")
bandera=0
contador=0
while bandera==0:
    eleccion = int(input("Intenta adivinar el número, Ingresa tu elección: "))
    if(eleccion > 50 or eleccion < 1):
        print("Ingresa solo numeros entre el 1 y 50")
    else:
        contador+=1
        if eleccion == compu:
            print("Correcto, ¡Haz acertado, Ganaste!")
            bandera=1
        else:
            if eleccion>compu:
                print("El número a adivinar es menor!")
                seguir = int(input("¿Quieres continuar jugando?\n0.- NO\n1.- SI\nElige opción:"))
                if seguir == 0:
                    bandera=1
            elif eleccion<compu:
                print("El número a adivinar es mayor!")
                seguir = int(input("¿Quieres continuar jugando?\n0.- NO\n1.- SI\nElige opción:"))
                if seguir == 0:
                    bandera=1
        
print("- - Fin del juego - -")
print("El número era: "+str(compu))
print("Total de intentos: "+str(contador))