#Los tabs estan con espacios 
while True: # entra en un bucle  
 nombre_user = input("Por favor ingrese su nombre completo: ") # pide tu nombre
 if all(c.isalpha() or c.isspace() for c in nombre_user): # abre un if para revisar que solo metas letras y espacios para evitar uso de numeros
  break # si todo esta bien salta al siguiente proceso
 else: # en caso de que falle le pide reingresas los datos
   print("por favor ingrese su nombre y apellido sin números")

while True: # entra en un bucle
    try: # llama a lo siguiente: 
     numero_de_cedula = int(input("Por favor ingrese su número de cedula: ")) # pide tu numero de cedula
     if numero_de_cedula != 9: #####: # verifica que el numero de cedula sea mayor a 0 para evitar uso de negativos
      print("La cedula debe tener 9 digitos, sin carácteres especiales")
     else: 
      break # sale del bucle
    except ValueError: # esto hace una excepcion del break para manndar el siguiente print a pantalla y volver a pedir datos
     print("por favor ingrese su numero de celuda sin letras ni caracteres especiales. ")
     
while True: # abre bucle
    try: # llama al siguiente proceso
     numero_de_celular = input("Por favor ingrese su número de celular: ") # pide el numero de celular
     if numero_de_celular < 8 :
       print("reingrese su numero de celular, debe de ser entre 8 a 11 numeros, ni puede ser negativo")
       numero_de_celular = input("Por favor ingrese su número de celular: ")
     else: 
      break
    except ValueError:
     print("por favor ingrese su numero de celular sin letras ni caracteres especiales. ")
     
while True:
    correo = str(input("Por favor ingrese su correo electronico: "))
    if "@" not in correo:
     print ("el correo electronico no es valido ")
    else:
     break
direccion = str(input("Por favor ingrese su direccion: "))
print(nombre_user, numero_de_cedula, numero_de_celular,  correo, direccion)