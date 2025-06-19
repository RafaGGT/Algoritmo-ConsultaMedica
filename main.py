import user as u

# Bucle infinito que mantiene abierto el menu principal
while True:
    try:
        # Menú principal
        opcion = u.menu()
        if opcion == 1:
            # Bucle del menú de pacientes
            while True:
                opcion_paciente = u.menu_paciente()
                if opcion_paciente == 1:
                    u.registrar_paciente()
                elif opcion_paciente == 2:
                    u.ver_pacientes()
                elif opcion_paciente == 3:
                    u.editar_paciente()
                elif opcion_paciente == 4:
                    u.eliminar_paciente()
                elif opcion_paciente == 5:
                    break  
                else:
                    print("Opción no válida. Intenta de nuevo.")
        elif opcion == 2:
            # Bucle del menú de consultas
            while True:
                opcion_consulta = u.menu_consultas()
                if opcion_consulta == 1:
                    u.agregar_consulta()
                elif opcion_consulta == 2:
                    u.ver_historial()
                elif opcion_consulta == 3:
                    u.editar_consulta()
                elif opcion_consulta == 4:
                    u.eliminar_consulta()
                elif opcion_consulta == 5:
                    break 
                else:
                    print("Opción no válida. Intenta de nuevo.")
        elif opcion == 3:
            print("¡Hasta luego!")
            break  
        else:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError:
        print("Ingresa un número válido.")
    except Exception as e:
        print("Error del sistema:", e)

