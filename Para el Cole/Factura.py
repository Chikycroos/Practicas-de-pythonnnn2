monto = int(input("Ingrese el monto: "))


if monto>1000:
    descuento = (monto*0.10)
    total = (monto-descuento)
    print("El monto sin descuento es de... ",monto ," y el descuento es de... ", descuento)
    print("El monto total con descuento de es... ", total)
else:
    print("El monto es de...", monto)