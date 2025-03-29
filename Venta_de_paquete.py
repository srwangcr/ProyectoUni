def mostrar_paquetes():
    paquetes = [
        ("1. Paquete 1: Incluye una estadía de 1 noche, con desayuno incluido", 200),
        ("2. Paquete 2: Comprende una estadía de 3 noches, con desayunos incluidos y derecho a una cena en el restaurante premium.", 570),
        ("3. Paquete 3: Ofrece una estadía de 5 noches, con desayunos incluidos, dos cenas en el restaurante premium y una hora de masajes relajantes en el spa.", 925),
        ("4. Paquete 4: Proporciona una estadía de 7 noches con desayunos incluidos, tres cenas en el restaurante premium, una hora de masajes relajantes en el spa", 1260)
    ] 
    for i, (descripcion, precio) in enumerate(paquetes, start=1):
     print(f"{i}. {descripcion} - Precio: ${precio}")  # ¡Ahora se usa "precio"!
    while True:  # Este while asegura que no se ingrese un valor flotante o string 
        try:   
            paquete = int(input("Ingrese el paquete deseado, por favor que sea un número del 1 al 4: "))
            if 1 <= paquete <= 4: 
                return paquetes[paquete - 1]  # Restamos 1 para acceder al índice correcto
            else: 
                print("Por favor, elija un número válido para el sistema")
        except ValueError: 
            print("Por favor, que sea un número sin decimales")
paquete_final, precio = mostrar_paquetes()
print (f"Usted eligió este paquete: {paquete_final} con un precio de {precio} dolares")
