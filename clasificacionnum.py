def clasificar_numeros():
    positivos = []
    negativos = []
    
    while True:
        try:
            numero = int(input("Ingresa un número o ingrese 0 para salir del programa: "))
            if numero == 0:
                break
            elif numero > 0:
                positivos.append(numero)
            else:
                negativos.append(numero)
        except ValueError:
            print("ingresa un número válido.")
    
    resultado = {
        "cantidad_positivos": len(positivos),
        "cantidad_negativos": len(negativos),
        "positivos": positivos,
        "negativos": negativos
    }
    
    return resultado

if __name__ == "__main__":
    resultado = clasificar_numeros()
    print("\nResultados:")
    print(resultado)