print("**"*18)
print("*** ESTA ES TU FACTURA DE VENTA ***")
print("**"*18)

nombre = input("Por favor ingresar el nombre del producto: ")

#Aca estamos validando que el precio del producto sea positivo
valPre = True
while valPre:
    try:
        precio= float (input("Ingresa el precio del producto: ")) 
        if precio<=0:
            print("el Dato ingresado del precio es erroneo")
                  
        else:
            valPre=False
    except:
        print("Solo numeros enteros")

#Aca estamos validando la cantidad del producto sea Num positivo
valCant = True
while valCant:
    try: 
        cantidad = int(input("Ingresa la cantidad del producto: ")) 
        if cantidad<0:
            print("El Dato ingresado de la cantidad es incorrecto")
        else:
            valCant=False
    except:
        print("Intentaste escribir una letra/palabra")

#Aca estamos validando el porcentaje de descuento
valDesc=True
while valDesc:
    try:
        descuento = float(input("por favor ingresa el porcentaje de descuento del producto de 0 al 100:\n ")) 
        if descuento<0 or descuento>100:
            print("Error en el porcentaje, Recuerda que es de 0-100")
            
        else: valDesc=False
    except:
        print("Intentaste escribir una letra/palabra")

totalSinDesc = cantidad*precio
descuentoCompra = (totalSinDesc*descuento)/100
compraTotal = (totalSinDesc-descuentoCompra)

print("El total de la compra es:")
print("cantidad, nombre, precio")
print(f"{cantidad}          {nombre}     {totalSinDesc:.2f}")
print(f"El total de la compra con descuento es: \n{cantidad}          {nombre}     {compraTotal:.2f}")