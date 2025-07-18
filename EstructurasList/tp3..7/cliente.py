from tramite_admin import TramitesAdmin
from tramite import Tramite

def main():
    admin = TramitesAdmin()
    admin.load()  # Cargar trámites desde la base de datos

    while True:
        print("\nOpciones:")
        print("1. Agregar trámite")
        print("2. Quitar trámite")
        print("3. Listar trámites")
        print("4. Persistir Cambios")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = int(input("Número del trámite: "))
            apellido = input("Apellido del solicitante: ")
            nombre = input("Nombre del solicitante: ")
            requerimiento = input("Descripción del requerimiento: ")
            admin.add(Tramite(numero, apellido, nombre, requerimiento))
            print("Trámite agregado exitosamente!")
        elif opcion == '2':
            try:
                removed = admin.remove()
                print(f"Trámite removido: {removed}")
            except IndexError as e:
                print(e)
        elif opcion  == '3':
            print("Lista de trámites:")
            for tramite in admin.list():
                print(tramite)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        elif opcion == '4':
            admin.persist()
        else:
            print("Opción fuera de rango, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
    