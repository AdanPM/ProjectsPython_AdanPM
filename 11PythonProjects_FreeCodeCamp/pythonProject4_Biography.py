
print("Responde el siguiente cuestionario")


nombre = input("Ingrese su nombre: ")
   
bandera=0
while bandera==0:
    dia = input("Ingrese dia de nacimiento (1 - 31): ")
    if dia.isdigit():
        if int(dia)>=1 and int(dia)<=31:
            bandera = 1
        else:
            print("Ingrese solo numeros del 1 al 31")
    else:
        print("Ingrese solo numeros del 1 al 31")

bandera=0
while bandera==0:
    mes = input("Ingrese mes de nacimiento (1 - 12): ")
    if mes.isdigit():
        if int(mes)>=1 and int(mes)<=12:
            bandera = 1
        else:
            print("Ingrese solo numeros del 1 al 12")
    else:
        print("Ingrese solo numeros del 1 al 12")

bandera=0
while bandera==0:
    ano = input("Ingrese año de nacimiento (Ej. 1998): ")
    if ano.isdigit():
        bandera = 1
    else:
        print("Ingrese solo numeros (Ej. 1998)")
    

direccion = input("Ingrese dirección: ")
metas = input("Ingrese metas que desea lograr: ")

print("Datos Ingresados")
print("Nombre: "+nombre+"\nFecha Nacimiento: "+str(dia)+"/"+str(mes)+"/"+str(ano)+"\nDirección: "+direccion+"\nMetas: "+metas)

