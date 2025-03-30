if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main # Esto asegura que el módulo no se ejecute directamente
else:
    pass

from Servicios import seleccionar_servicios
from Register import nombre_user, numero_de_cedula, numero_de_celular, correo, direccion
from Horario_de_atencion import Horario_Final
from Venta_de_paquete import paquete_final


historial_lista = []  # Lista para almacenar la información de facturación
def historial():
    servicios_elegidos, total = seleccionar_servicios()
    
    # Crear una lista con solo el nombre y las horas de los servicios elegidos
    servicios_info = [f"{servicio['nombre']} (Horas: {servicio['horas']})" for servicio in servicios_elegidos]
    
    # Unir la información de los servicios en una cadena
    servicios_elegidos_str = ", ".join(servicios_info)

    historial_info = (f"Nombre: {nombre_user}\n " 
                      f"Cédula: {numero_de_cedula}\n "
                      f"Celular: {numero_de_celular}\n "
                      f"Correo: {correo}\n "
                      f"Dirección: {direccion}\n "
                      f"Usted eligió este paquete: {paquete_final}\n "
                      f"con un precio de {total} dólares\n "  # Cambié 'precio' a 'total' para que sea consistente
                      f"horario final: {Horario_Final}\n "
                      f"servicios elegidos: {servicios_elegidos_str}\n ")  # Usar la cadena formateada

    historial_lista.append(historial_info)  # Agrega la información de la facturación a la lista
    print(historial_lista[0])  # Imprime la información de la facturación

# Llamar a la función de historial
historial()