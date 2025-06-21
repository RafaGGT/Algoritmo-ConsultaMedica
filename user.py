from datetime import datetime

# Diccionario que contiene los ruts(clave) y datos(valor) del paciente 
pacientes = {
    "20111857-3": {"Nombre": "Rafael Gallegos", "Edad": "25", "Sexo": "Masculino"},
}
# Lista de constulas 
consultas = []  

# Menu principal 
def menu():
    print("--- Menú Principal ---")
    print("1) Pacientes")
    print("2) Consultas")
    print("3) Salir")
    op = int(input("Elige una opción: "))
    print("-"*25)
    return op
# Menu crud paciente
def menu_paciente():
    print("--- Menú Pacientes ---")
    print("1. Registrar paciente")
    print("2. Listar pacientes")
    print("3. Editar paciente")
    print("4. Eliminar paciente")
    print("5. Volver atras")
    op = int(input("Elige una opción: "))
    print("-"*25)
    return op
# Menu crud consultas
def menu_consultas():
    print("--- Menú Consultas ---")
    print("1. Agregar consulta")
    print("2. Ver Historial de un paciente")
    print("3. Editar consulta")
    print("4. Eliminar consulta")
    print("5. Volver atras")
    op = int(input("Elige una opción: "))
    print("-"*25)
    return op

# ------------------------------- Funciones para el CRUD de pacientes -------------------------------

# Ingresar pacientes al diccionario
def registrar_paciente():  
    rut = input("Ingrese RUT del paciente sin punto y con guion: ").strip().upper()
    # Verificamos que no exista ya el rut ingresado
    if rut in pacientes: 
        print("Paciente con ese RUT ya existe.")
        return
    nombre = input("Nombre y Apellido: ").strip().capitalize() 
    edad = input("Edad: ").strip()
    sexo = input("Sexo: ").strip().title() 
    # Ingresamos al diccionario pacientes la clave(rut) y el valor(diccionario con los datos)
    pacientes[rut] = {'Nombre': nombre, 'Edad': edad, 'Sexo': sexo}
    print("Paciente agregado exitosamente.")

# Listar pacientes
def ver_pacientes():
    # En caso de que no haya pacientes
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print("*"*30)
    # Recorre el diccionario con la informacion de los pacientes
    for rut, info in pacientes.items():
        print(f"RUT: {rut} \nNombre: {info['Nombre']} \nEdad: {info['Edad']} \nSexo: {info['Sexo']}")
        print("*"*30)

# Modifica los datos del paciente mas no el rut
def editar_paciente():
    rut = input("Ingrese RUT del paciente a editar: ").strip().upper()
    if rut not in pacientes:
        print("No se encontró un paciente con ese RUT.")
        return
    # Mostramos los datos actuales en base al rut
    print(f"Datos actuales del paciente {rut}:")
    print(f"Nombre: {pacientes[rut]['Nombre']}")
    print(f"Edad: {pacientes[rut]['Edad']}")
    print(f"Sexo: {pacientes[rut]['Sexo']}")
    # Le pedimos al usuario que modifique un dato
    try:
        op = int(input("¿Qué desea modificar?\n1) Nombre\n2) Edad\n3) Sexo\nOpción: "))
    except ValueError:
        print("Opción inválida.")
        return
    except:
        print("Error del sistema")
        return
    if op == 1:
        nuevo_nombre = input("Nuevo nombre: ").strip().title()
        if nuevo_nombre:
            pacientes[rut]['Nombre'] = nuevo_nombre
            print("Nombre actualizado.")
    elif op == 2:
        nueva_edad = input("Nueva edad: ").strip()
        if nueva_edad:
            pacientes[rut]['Edad'] = nueva_edad
            print("Edad actualizada.")
    elif op == 3:
        nuevo_sexo = input("Nuevo sexo: ").strip().title()
        if nuevo_sexo:
            pacientes[rut]['Sexo'] = nuevo_sexo
            print("Sexo actualizado.")
    else:
        print("Opción no válida.")
        return
    print("Paciente actualizado exitosamente.")

# Eliminar paciente
def eliminar_paciente():
    rut = input("Ingrese RUT del paciente a eliminar: ").strip().upper()
    if rut not in pacientes:
        print("No se encontró un paciente con ese RUT.")
        return
    # Mostramos los datos del paciente y confirmamos si desea eliminar al paciente
    print(f"\nDatos del paciente {rut}:")
    print(f"Nombre: {pacientes[rut]['Nombre']}")
    print(f"Edad: {pacientes[rut]['Edad']}")
    print(f"Sexo: {pacientes[rut]['Sexo']}")
    confirmar = input('¿Desea eliminarlo? (escribe "s" para confirmar): ').strip().lower()
    # Si se confirma primero eliminamos todas las consultas del pacientas y luego al paciente 
    if confirmar == 's':
        for consulta in consultas:
            if consulta[0] == rut:
                consultas.remove(consulta)
        del pacientes[rut] 
        print("Paciente eliminado exitosamente.")
    else:
        print("Eliminación cancelada.")

# ------------------------------- Funciones para el CRUD de consultas -------------------------------
# Se agrega una consulta a la lista
def agregar_consulta():
    rut = input("Ingrese RUT del paciente para consulta: ").strip().upper()
    if rut not in pacientes: 
        print("El paciente con ese RUT no existe.")
        return
    # Se pide que se ingrese una fecha en formato dia/mes/año
    try:
        fecha_consulta = input("Fecha de la consulta (DD/MM/AAAA): ").strip()
        # Se usa datetime.strptime para transformar un string a objeto tipo fecha
        fecha = datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
    except ValueError:
        print("Fecha inválida. Usa el formato DD/MM/AAAA.")
        return
    motivo = input("Motivo de la consulta: ").strip()
    # Ingresamos a los datos a la lista de consultas
    consultas.append([rut, fecha, motivo])
    print("Consulta agregada.")


# Ver historial del paciente
def ver_historial():
    rut = input("Ingrese RUT del paciente para ver su historial: ").strip().upper()
    # Booleano para saber si el paciente tiene consultas registradas
    historial = False
    for consulta in consultas:
        if consulta[0] == rut: # consulta[0] es la ubicacion del rut ingresado en consultas
            if not historial:
                # El encabezado se muestra solo una vez gracias al booleano de historial
                print(f"Historial de consultas para {pacientes[rut]['Nombre']} ({rut}):")
                historial = True
            print(f"- Fecha: {consulta[1].strftime('%d/%m/%Y')} | Motivo: {consulta[2]}")
    if not historial:
        print("No hay consultas registradas para este paciente.")

# Edita el motivo de la consulta en base al rut y fecha
def editar_consulta():
    rut = input("Ingrese RUT del paciente: ").strip().upper()
    if rut not in pacientes:
        print("Paciente no encontrado.")
        return
    fecha_consulta = input("Ingrese la fecha de la consulta a editar (DD/MM/AAAA): ").strip()
    try:
        # Se usa datetime.strptime para transformar un string a objeto tipo fecha
        fecha = datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de fecha inválido.")
        return
    # Recorremos la lista y buscamos cual coincide tanto en fecha como por rut
    for consulta in consultas:
        if consulta[0] == rut and consulta[1] == fecha:
            print(f"Motivo actual: {consulta[2]}")
            nuevo_motivo = input("Nuevo motivo de la consulta: ").strip()
            # Verifica que se haya escrito algo en la nueva consulta
            if nuevo_motivo:
                consulta[2] = nuevo_motivo
                print("Consulta actualizada.")
            return
    print("Consulta no encontrada.")

# Eliminar consulta por rut y fecha
def eliminar_consulta():
    rut = input("Ingrese RUT del paciente: ").strip().upper()
    if rut not in pacientes:
        print("Paciente no encontrado.")
        return
    fecha_consulta = input("Ingrese la fecha de la consulta a eliminar (DD/MM/AAAA): ").strip()
    try:
        # Se usa datetime.strptime para transformar un string a objeto tipo fecha
        fecha = datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de fecha inválido.")
        return
    # Buscar y eliminar la consulta en la que concuerde el rut y la fecha
    for consulta in consultas:
        if consulta[0] == rut and consulta[1] == fecha:
            consultas.remove(consulta)
            print("Consulta eliminada con éxito.")
            return
    print("No se encontró una consulta con ese RUT y fecha.")