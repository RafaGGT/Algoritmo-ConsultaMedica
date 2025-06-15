import user as u

while True:
    try:
        opcion = u.menu()
        if opcion == 1:
            u.registrar_paciente()
        elif opcion == 2:
            u.ver_pacientes()
        elif opcion == 3:
            rut = input("Ingrese RUT del paciente para consulta: ").strip().upper()
            u.agregar_consulta(rut)
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError:
        print("Ingresa un numero valido")
    except: 
        print("Error del sistema")

    