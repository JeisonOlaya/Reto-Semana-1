print("\n")
print("**"*18)
print("*** ESTA ES TU FACTURA DE VENTA ***")
print("**"*18)
print("\n")

# en la linea 8 creamos la lista

user= []
proceso = True
# inicia un while que esta corriendo por todo el programa para que el usurio pueda repetir el proceso si desea agregar otro producto.

while proceso:    
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
        
    user.append([cantidad,nombre, precio])

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



    volver =int(input("deseas agregar otro producto a la lista? digita 1 para Si o 2 para No: "))

    if volver == 2:
        print("Fin de la compra \n")        
        proceso = False



contador = 0
print("El total de la compra sin descuento es: \n")
print("cantidad, nombre, precio")
c = 0


total = 0
totDesc= 0
for product in user:
       
    total = total + (product[0] * product[2])
    descuentoCompra = (total*descuento)/100
    totDesc = (total-descuentoCompra)

for i in user:
    print(i[0], i[1], i[2])

print(f"total= {total:.2f}\n")
print("El total de la compra con descuento es: \n")
print("===============================")
print(f"total= {totDesc:.2f}")

