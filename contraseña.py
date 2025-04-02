import re
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
