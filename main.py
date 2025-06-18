import user as u

# Bucle infinito que mantiene abierto el menu
while True:
    try:
        # Abrimos el menu inicial
        opcion = u.menu()
        if opcion == 1:
            # Abrimos el menu de pacientes
            opcion_paciente = u.menu_paciente()
            if opcion_paciente == 1:
                u.registrar_paciente()
            elif opcion_paciente == 2:
                u.ver_pacientes()  
            elif opcion_paciente == 3:
                u.editar_paciente()
            elif opcion_paciente == 4:
                u.eliminar_paciente() 
            elif opcion_paciente != 5:
                print("Opción no válida. Intenta de nuevo.")
        # Abrimos el menu de consultas
        elif opcion == 2:
                opcion_consulta = u.menu_consultas()
                if  opcion_consulta == 1:
                    u.agregar_consulta()
                elif  opcion_consulta == 2:
                    u.ver_historial()
                elif  opcion_consulta == 3:
                    u.editar_consulta()
                elif  opcion_consulta == 4:
                    u.eliminar_consulta()
                elif opcion_paciente != 5:
                    print("Opción no válida. Intenta de nuevo.")
        # Le damos cierre a la aplicacion con un break
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError:
        print("Ingresa un numero valido")
    except: 
        print("Error del sistema")
