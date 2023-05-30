def show_passwords():
    # Contraseña para acceder a las contraseñas almacenadas
    password = "123456789"
    
    # Solicitar la contraseña al usuario
    user_password = input("Ingresa la contraseña: ")
    
    # Verificar si la contraseña es correcta
    if user_password == password:
        # Contraseñas almacenadas
        passwords = ["password123", "987543", "123e345"]
        
        # Mostrar las contraseñas
        print("Contraseñas almacenadas:")
        for password in passwords:
            print(password)
    else:
        print("Contraseña incorrecta.")

# Ejecutar el programa
show_passwords()