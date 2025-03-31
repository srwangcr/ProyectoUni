if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main  # Esto asegura que el módulo no se ejecute directamente
else:
    pass

from Register import nombre_user, numero_de_cedula, numero_de_celular, correo, direccion
from menu import paquete_final, precio_paquete, Horario_Final 

def Facturacion(servicios_elegidos, total_servicios):  # Recibe los servicios elegidos y el total

    # Crear una lista que incluya el nombre, las horas y el precio unitario de cada servicio
    servicios_info = [f"{servicio['nombre']} (Horas: {servicio['horas']}, Precio unitario: ${servicio['precio']})" for servicio in servicios_elegidos]
    servicios_elegidos_str = ", ".join(servicios_info)  # El join ingresa a la lista para consultar datos
    
    # Verifica que el total y el precio sean números
    subtotal = total_servicios + precio_paquete  # Asegúrate de que 'precio_paquete' sea un número
    IVA = 0.13  # IVA como porcentaje
    Total_Facturacion = subtotal + (subtotal * IVA)  # Total con IVA

    # Imprimir la información de facturación
    print(f"Nombre: {nombre_user}")
    print(f"Cédula: {numero_de_cedula}")
    print(f"Celular: {numero_de_celular}")
    print(f"Correo: {correo}")
    print(f"Dirección: {direccion}")
    print(f"Usted eligió este paquete: {paquete_final}")
    print(f"Con un precio de {precio_paquete} dólares")
    print(f"Horario final: {Horario_Final}")
    print(f"Subtotal: {subtotal}")
    print(f"IVA: {subtotal * IVA}")  # Cálculo del IVA
    print(f"Total final: {Total_Facturacion}")
    print(f"Servicios elegidos: {servicios_elegidos_str}")
    print(f"Precio total de servicios: ${total_servicios}")

# No llames a la función aquí, se llamará desde el módulo menu