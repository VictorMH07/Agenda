def mostrar_menu():
    print("\nAgenda de contacto")
    print("1. Agragar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")
    
def agregar_contacto(agenda):
    nombre = input("Ingrese nombre completo del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")
    agenda[nombre] = {"telefono": telefono, "correo": correo}
    print(f"Se ha agregado el contacto {nombre} exitosamente")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado exitosamente")
    else:
        print(f"No se ha encontrado el contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que está buscando: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Correo: {agenda[nombre]['correo']}")
    else:
        print(f"El contacto {nombre}, no se encontro en la agenda")

def lista_contactos(agenda):
    if agenda:
        print("\nLista de contactos")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Correo: {info["correo"]}")
            print("-" * 50)
    else:
        print("La agenda se encuentra vacia")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            lista_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda")
            break
        else:
            print("Por favor seleccione una opcion válida (del 1 a 5)")

agenda_contactos()
