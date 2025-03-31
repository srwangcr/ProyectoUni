if __name__ == "__main__": 
    print("Este módulo no se puede ejecutar directamente. Por favor, inicie desde main.py.")
    import main # Esto asegura que el módulo no se ejecute directamente
else:
    pass

#Los tabs estan con espacios 
while True: # entra en un bucle  
 nombre_user = input("Por favor ingrese su nombre completo: ") # pide tu nombre
 if all(c.isalpha() or c.isspace() for c in nombre_user): # abre un if para revisar que solo metas letras y espacios para evitar uso de numeros
  break # si todo esta bien salta al siguiente proceso
 else: # en caso de que falle le pide reingresas los datos
   print("por favor ingrese su nombre y apellido sin números")


while True:  # entra en un bucle
    try:  # llama a lo siguiente:
        numero_de_cedula = int(input("Por favor ingrese su número de cédula: "))  # pide tu número de cédula
        
        # Verifica que el número de cédula sea positivo y tenga exactamente 9 dígitos
        if numero_de_cedula <= 0:
            print("La cédula debe ser un número positivo.")
        elif len(str(numero_de_cedula)) != 9:
            print("La cédula debe tener exactamente 9 dígitos.")
        else:
            break  # sale del bucle si todas las condiciones son válidas
    except ValueError:  # esto maneja la excepción si el usuario ingresa un valor no válido
        print("Por favor ingrese su número de cédula sin letras ni caracteres especiales.")
     
while True: # abre bucle
    try: # llama al siguiente proceso
     
     numero_de_celular = int(input("Por favor ingrese su número de celular: ")) # pide el numero de celular

     if numero_de_celular <= 0 :
       print("el numero de celular debe ser mayor a 0 digitos") # verifica que el numero de celular sea mayor a 8 para evitar uso de negativos
     elif len(str(numero_de_celular)) != 8:
            print("La cédula debe tener exactamente 8 dígitos.")
     else:
      break  # sale del bucle si todas las condiciones son válidas
    except ValueError:  # esto maneja la excepción si el usuario ingresa un valor no válido
      print("Por favor ingrese su número de celular sin letras ni caracteres especiales.")

while True:  # abre bucle
    correo = str(input("Por favor ingrese su correo electrónico: "))  # pide el correo electrónico
    # Verifica que el correo tenga un '@' y un '.com' y que no contenga caracteres no válidos
    if "@" not in correo or ".com" not in correo or not correo.replace(".", "").replace("@", "").isalnum():
        print("El correo electrónico no es válido. Asegúrese de que contenga '@', '.com' y no tenga caracteres no válidos.")  # si no es válido, le pide que lo reingrese
    else:  # si tiene arroba y .com, salta al siguiente proceso
        break  # si el correo es válido


direccion = str(input("Por favor ingrese su direccion: ")) # pide la direccion
print(nombre_user, numero_de_cedula, numero_de_celular,  correo, direccion) # imprime los datos ingresados por el usuario