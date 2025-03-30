if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main  # Esto asegura que el módulo no se ejecute directamente
else:
    pass

Ciclo = 0
servicios_elegidos = []  # Inicializa la lista de servicios elegidos
total = 0  # Inicializa el total
paquete_final = None  # Inicializa el paquete final
precio_paquete = 0  # Inicializa el precio del paquete
Horario_Final = None  # Inicializa el horario final

while 6 >= Ciclo:
    while True: 
        try: 
            Eleccion = int(input("Ingrese un valor del 1 al 6, con el valor 1 ingresas a la elección del paquete, con el valor 2, ingresas al horario de atención, con el valor 3, ingresas al apartado de servicios, con el valor 4 ingresas a la facturación, con el valor 5 ingresas al historial y 6 para salir: "))
            break
        except ValueError:
            print("Por favor ingrese un número sin decimales ni letras")
    
    if Eleccion == 1: 
        import Venta_de_paquete  # Importa el módulo de venta de paquetes
        paquete_final, precio_paquete = Venta_de_paquete.mostrar_paquetes()  # Llama a la función y guarda los resultados
        Ciclo += 1
    elif Eleccion == 2: 
        import Horario_de_atencion  # Importa el módulo de horarios
        Horario_Final = Horario_de_atencion.seleccionar_horario()  # Llama a la función y guarda el horario seleccionado
        Ciclo += 1
    elif Eleccion == 3: 
        import Servicios  # Importa el módulo Servicios
        servicios_elegidos, total = Servicios.seleccionar_servicios()  # Llama a la función y guarda los resultados
        Ciclo += 1
    elif Eleccion == 4:
        import Facturacion  # Asegúrate de que el módulo Facturacion esté importado
        if not servicios_elegidos or paquete_final is None or total == 0 or Horario_Final is None:  # Verifica si no hay servicios elegidos o paquete
            print("Faltan datos para poder crear su facturación. Por favor, ingrese los datos necesarios:")
            if paquete_final is None:
                print("- Primero el paquete")
            if Horario_Final is None:
                print("- Luego el horario de atención")
            if not servicios_elegidos:
                print("- Luego el servicio")
            Ciclo -= 1
        else:
            Facturacion.Facturacion(servicios_elegidos, total)  # Llama a la función Facturacion con los parámetros correctos
            Ciclo += 1
    elif Eleccion == 5: 
        import Historial  # Asegúrate de que el módulo Historial esté importado
        if not servicios_elegidos or paquete_final is None or total == 0 or Horario_Final is None:  # Verifica si no hay servicios elegidos o paquete
            print("Faltan datos para poder generar el historial. Por favor, ingrese los datos necesarios:")
            if paquete_final is None:
                print("- Primero el paquete")
            if Horario_Final is None:
                print("- Luego el horario de atención")
            if not servicios_elegidos:
                print("- Luego el servicio")
            Ciclo -= 1
        else:
            Historial.historial(servicios_elegidos, total)  # Llama a la función Historial con los parámetros correctos
            Ciclo += 1
    elif Eleccion == 6:
        print("Gracias por usar nuestro sistema, vuelva pronto")
        exit()
    else: 
        print("Ingrese una opción correcta, por favor")
        Ciclo -= 1