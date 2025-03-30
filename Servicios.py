if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main # Esto asegura que el módulo no se ejecute directamente
else:
    pass


servicios = {
    1: {"nombre": "Jetski", "precio": 100, "horas": 0, "max_elegido": 2},
    2: {"nombre": "Parasailing", "precio": 75, "horas": 0, "max_elegido": 2},
    3: {"nombre": "Windsurf", "precio": 25, "horas": 0, "max_elegido": 2},
    4: {"nombre": "Tiro al blanco", "precio": 10, "horas": 0, "max_elegido": 2},
    5: {"nombre": "Avistamiento de ballenas", "precio": 80, "horas": 0, "max_elegido": 1},
    6: {"nombre": "Boat Sunset Tour", "precio": 120, "horas": 0, "max_elegido": 1},
    7: {"nombre": "Bote Banana", "precio": 35, "horas": 0, "max_elegido": 3},
}

# ... (código anterior)

def seleccionar_servicios(cantidad_de_servicios=None, servicios_elegidos=None):
    if servicios_elegidos is None:
        servicios_elegidos = []
    
    if cantidad_de_servicios is None:
        print("Servicios:")
        for key, value in servicios.items():
            print(f"{key}. {value['nombre']}: ${value['precio']} por persona")

        # Solicitar cantidad de servicios
        while True:
            try:
                cantidad_de_servicios = int(input("Elija cuántos servicios desea adquirir (Máximo 5 servicios): "))
                if 1 <= cantidad_de_servicios <= 5:
                    break
                else:
                    print("Por favor, ingrese un número entre 1 y 5.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

    # Selección de servicios
    for _ in range(cantidad_de_servicios):
        while True:
            try:
                servicio_elegido = int(input("Elija el número del servicio que desea comprar: "))
                if servicio_elegido in servicios:
                    if servicios[servicio_elegido]["horas"] < servicios[servicio_elegido]["max_elegido"]:
                        servicios[servicio_elegido]["horas"] += 1
                        servicios_elegidos.append(servicios[servicio_elegido])
                        print(f"{servicios[servicio_elegido]['nombre']} seleccionado.")
                        break
                    else:
                        print(f"Este servicio no se puede escoger más de {servicios[servicio_elegido]['max_elegido']} veces, por favor, elija otro.")
                else:
                    print("Número de servicio no válido. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

    # Calcular y mostrar el total
    total = sum(servicio["precio"] * servicio["horas"] for servicio in servicios.values())
    print(f"El total a pagar es: ${total}")

    return servicios_elegidos, total