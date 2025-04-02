import re
import logging

def configurar_logging():
    logging.basicConfig(
        filename='intentos_contraseña.log', 
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def validar_contraseña(contraseña):
    
    if len(contraseña) < 8:
        print("Tu contraseña debe tener mas de 8 caracteres")
    if not any(caracter.isupper() for caracter in contraseña):
        print("Debe haber al menos 1 mayuscula")
    if not any(caracter.isdigit() for caracter in contraseña):
        print("Debe haber al menos 1 digito")
    return True
    return False
print ("debes crear una contraseña segura")

while True:
    contraseña=input("Ingresa tu contraseña: ")
    if validar_contraseña(contraseña): 
        print("contraseña correcta")
        break


def solicitar_contraseña():
    configurar_logging()
    intentos = 0
    while intentos < 3:
        contraseña = input("Ingrese su contraseña: ")
        if validar_contraseña(contraseña):
            print("Contraseña válida.")
            logging.info("Contraseña aceptada en el intento %d", intentos + 1)
            return True
        else:
            intentos += 1
            print("Contraseña no válida. debe tener al menos 8 caracteres, una mayúscula y un número.")
            logging.warning("Intento %d: Contraseña inválida", intentos)
    
    print("Demasiados intentos. Saliendo del programa.")
    logging.error("Demasiados intentos. Saliendo del programa.")
    exit()

solicitar_contraseña()