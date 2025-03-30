usuario_1 = "admin1"
password_1 = "admin1"
usuario_2 = "admin2"
password_2 = "admin2"

# Este es el código de inicio de sesión para el sistema de ventas de paquetes

def login(usuario_1, password_1, usuario_2, password_2):
    ciclo = 0  # esta es la funcion de inicio de sesion
    print("Bienvenido al sistema de ventas de paquetes")
    print("Por favor, inicie sesión para continuar")

    while True :
     usuario = input("Ingrese su nombre de usuario: ")
     password = input("Ingrese su contraseña: ")

     if (usuario == usuario_1 and password == password_1) or (usuario == usuario_2 and password == password_2):  # esta es la condicion para el inicio de sesion
        print("Inicio de sesión exitoso")
        print("Bienvenido", usuario)
        import Register # esto llama al modulo de register
        import menu # esto llama al modulo de menu
        break
     else:
        print("Nombre de usuario o contraseña incorrectos")  # este es el mensaje de error
        print("Por favor, intente nuevamente")
        ciclo += 1
        if ciclo == 1:
            print("Le quedan 2 intentos")
        elif ciclo == 2:
            print("Le queda 1 intento")   
        elif ciclo == 3:            
            print("Ha excedido el número de intentos permitidos")   
            print("El programa se cerrará")
            exit()
# Este es el código de inicio de sesión para el sistema de ventas de paquetes
login(usuario_1, password_1, usuario_2, password_2)  # esta es la funcion de inicio de sesion
# Este es el código de inicio de sesión para el sistema de ventas de paquetes
