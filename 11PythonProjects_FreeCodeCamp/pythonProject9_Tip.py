
print("- - Bienvenido - -")
total = float(input("¿Cuánto es el total de la cuenta? "))
tip = float(input("¿Cúanto porcentaja desea dejar de propina? "))

tipp = (tip/100)
propina = tipp * total
pagar=total+propina

print("Su propina es de: "+str(propina)+"\nSu total asciende a: "+str(pagar))

bandera=0
while bandera==0:
    repartir = int(input("¿Desea repartir la cuenta entre más personas?\n1. Si\n2. No\nSeleccione Opción: "))
    if repartir==1:
        cantidad = int(input("¿Entre cuantas personas quiere dividir la propina?"))
        iguales = int(input("¿Partes iguales?\n1. Si\n2. No\nSeleccione Opción: "))
        if iguales==1:
            tipigual = propina / cantidad
            print("Cada persona debe pagar: "+str(tipigual))
            bandera==1
        elif iguales==2:
            contador=0
            porc=0
            txtticketpropina=""
            while contador<cantidad:
                parte=int(input("Cuanto porcentaje corresponde a la persona "+str((contador+1))+": "))
                tipindividual=propina*(parte/100)
                porc=porc+parte
                txtticketpropina=txtticketpropina+("Persona "+str((contador+1))+" paga: "+str(tipindividual)+"\n")
                contador+=1
            if porc<100:
                print("No se cubrió el total de la propina")
                faltante = 100-porc
                tipfaltante = propina*(faltante/100)
                print("Faltan "+str(tipfaltante))
            elif porc>100:
                print("Se superó la cantidad de propina")
                sobrante = porc-100
                tipsobrante = propina*(sobrante/100)
                print("Sobran "+str(tipsobrante))
            print("Partes de la propina\n"+txtticketpropina)
            bandera=1
    else:
        bandera=1

print("Gracias por su preferencia")
