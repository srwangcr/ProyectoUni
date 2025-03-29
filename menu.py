Ciclo = 0

while 6>=Ciclo :
    while True: 
        try: 
         Eleccion= int(input("Ingrese un valor del 1 al 6 , con el valor 1 ingresas a la elección del paquete, con el valor 2, ingresas al horario de atención, con el valor 3, ingresas al apartado de servicios, con el valor 4 ingresas al historial y con el valor 5, ingresas a la facturación y 6 para salir "))
         break
        except ValueError:
            print ("Por favor ingrese un número sin decimales ni letras")
    if Eleccion == 1: ##en python se compara con ==
     import Venta_de_paquete
     Ciclo = Ciclo+1
     ##Esta opción redireccionará al codigo de venta de paquete
    elif Eleccion == 2 : 
        import Horario_de_atencion
        Ciclo = Ciclo+1
        ##Esta opción redireccionará al codigo de Horario de atención   
    elif Eleccion == 3 : 
        import Servicios
        Ciclo = Ciclo+1
        ##Esta opción redireccionará al codigo de Servicios
    elif Eleccion == 4 : 
        import Historial
        Ciclo = Ciclo +1
    elif Eleccion == 5 : 
        import Facturacion
        Ciclo = Ciclo+1
        ##Esta opción redireccionará al codigo de facturación #"
    elif Eleccion == 6 :
        exit()
        Ciclo = Ciclo+1
    else: 
        print ("Ingrese una opción correcta, por favor")
        Ciclo = Ciclo-1    