if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main  # Esto asegura que el módulo no se ejecute directamente
else:
    pass

# Definición de los horarios disponibles
horarios = [
    ("1. Horario 1: Check in 3pm, Check out 11am, Room service de 6am a 11pm, desayunos 6am a 10:30, almuerzos 12pm a 3pm"),
    ("2. Horario 2: Spa 10am a 11am, Uso de Gimnasio 6am a 8am, Cargador eléctrico 6am a 10am, Restaurante Premium (Cena) 6pm a 7:30pm"),
    ("3. Horario 3: Spa 2pm a 3pm, Gimnasio de 9am a 11am, Cargador eléctrico 10am a 2pm, Restaurante Premium (Cena) 7:30pm a 9pm"),
    ("4. Horario 4: Spa 6pm a 7pm, Gimnasio de 2pm a 6pm, Cargador eléctrico 2pm a 6pm, Restaurante Premium (Cena) 9pm a 10:30pm")
]

def mostrar_horarios():
    """Muestra la lista de horarios disponibles."""
    for i, (descripcion) in enumerate(horarios, start=1):
        print(f"{i}. {descripcion}")

def seleccionar_horario():
    """Permite al usuario seleccionar un horario y lo imprime."""
    mostrar_horarios()
    while True: 
        try: 
            Horario = int(input("Ingrese un valor del 1 al 4, el valor que elija será el horario que tendrá: "))
            if 1 <= Horario <= 4:
                # Imprime la descripción del horario seleccionado
                print(f"Usted eligió: {horarios[Horario - 1][0]}")  # Imprime la descripción completa del horario
                return horarios[Horario - 1][0]  # Si necesitas devolverlo para usarlo en otro lugar
            else:
                print("Por favor, elija un número válido para el sistema.")
        except ValueError:
            print("Por favor, ingrese un número sin decimales ni letras.")