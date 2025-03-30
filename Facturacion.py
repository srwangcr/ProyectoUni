if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main # Esto asegura que el módulo no se ejecute directamente
else:
    pass

from Register import nombre_user, numero_de_cedula, numero_de_celular, correo, direccion
from Servicios import seleccionar_servicios 
from Venta_de_paquete import mostrar_paquetes
from Horario_de_atencion import Horario_Final


def Facturacion(): # Esta función genera la facturación
    paquete_final, precio_paquete = mostrar_paquetes()  # Cambié 'precio' a 'precio_paquete' para mayor claridad
    servicios_elegidos, total_servicios = seleccionar_servicios()  # Cambié 'total' a 'total_servicios'
    
    # Crear una lista que incluya el nombre, las horas y el precio unitario de cada servicio
    servicios_info = [f"{servicio['nombre']} (Horas: {servicio['horas']}, Precio unitario: ${servicio['precio']})" for servicio in servicios_elegidos]
    servicios_elegidos_str = ", ".join(servicios_info)  # El join ingresa a la lista para consultar datos
    
    # Verifica que el total y el precio sean números
    subtotal = total_servicios + precio_paquete  # Asegúrate de que 'precio_paquete' sea un número
    IVA = 0.13  # IVA como porcentaje
    Total_Facturacion = subtotal + (subtotal * IVA)  # Total con IVA

    facturacion_lista = []

    facturacion_info = (f"Nombre: {nombre_user}\n "
                        f"Cédula: {numero_de_cedula}\n "
                        f"Celular: {numero_de_celular}\n "
                        f"Correo: {correo}\n "
                        f"Dirección: {direccion}\n "
                        f"Usted eligió este paquete: {paquete_final}\n "
                        f"con un precio de {precio_paquete} dólares\n "
                        f"horario final: {Horario_Final}\n "
                        f"Subtotal: {subtotal}\n"
                        f"IVA: {subtotal * IVA}\n"  # Cálculo del IVA
                        f"Total final: {Total_Facturacion}\n"
                        f"Servicios elegidos: {servicios_elegidos_str}\n "
                        f"Precio total de servicios: ${total_servicios}\n")  # Agregado el precio total de servicios
    facturacion_lista.append(facturacion_info)

    print(facturacion_lista[0])

Facturacion()  # Llama a la función de facturación