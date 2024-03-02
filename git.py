def main():
    print("Bienvenido a la agenda telefónica")
    agenda = {}

    while True:
        print("\n1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")
        
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            ver_contactos(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")