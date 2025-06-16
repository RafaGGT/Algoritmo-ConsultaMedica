from datetime import datetime

# Diccionario que contiene los ruts(clave) y datos(valor) del paciente 
pacientes = {
    "rut-test1": {"Nombre": "nom-test1", "Edad": "ed-test1", "Sexo": "sex-test1"},
    "rut-test2": {"Nombre": "nom-test2", "Edad": "ed-test2", "Sexo": "sex-test2"}
}
# Lista de constulas 
consultas = []  

# Menu principal
def menu():
    print("\n*** Menú de Consultas Médicas ***")
    print("1. Registrar paciente")
    print("2. Listar pacientes")
    print("3. Agregar consulta")
    print("4. Ver Historial")
    print("5. Salir")
    op = int(input("Elige una opción: "))
    return op

# Ingresar pacientes
def registrar_paciente():  
    rut = input("Ingrese RUT del paciente sin punto y con guion: ").strip().upper()
    if rut in pacientes: 
        print("Paciente con ese RUT ya existe.")
        return
    nombre = input("Nombre y Apellido: ").strip().title() 
    edad = input("Edad: ").strip()
    sexo = input("Sexo: ").strip().title() 
    pacientes[rut] = {'Nombre': nombre, 'Edad': edad, 'Sexo': sexo}
    print("Paciente agregado exitosamente.")

# Listar pacientes
def ver_pacientes():
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print("*"*30)
    for rut, info in pacientes.items():
        print(f"RUT: {rut} \nNombre: {info['Nombre']} \nEdad: {info['Edad']} \nSexo: {info['Sexo']}")
        print("*"*30)

# Se agrega una consulta a la lista
def agregar_consulta():
    rut = input("Ingrese RUT del paciente para consulta: ").strip().upper()
    if rut not in pacientes: 
        print("El paciente con ese RUT no existe.")
        return
    try:
        fecha_str = input("Fecha de la consulta (DD/MM/AAAA): ").strip()
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
    except ValueError:
        print("Fecha inválida. Usa el formato DD/MM/AAAA.")
        return
    motivo = input("Motivo de la consulta: ").strip()
    aaa = consultas.append({'rut': rut, 'fecha': fecha, 'motivo': motivo})
    print("Consulta agregada.")
    
# Modifica los datos del paciente mas no el rut
def editar_paciente():
    rut = input("Ingrese RUT del paciente a editar: ").strip().upper()
    if rut not in pacientes:
        print("No se encontró un paciente con ese RUT.")
        return
    
    print(f"\nDatos actuales del paciente {rut}:")
    print(f"Nombre: {pacientes[rut]['Nombre']}")
    print(f"Edad: {pacientes[rut]['Edad']}")
    print(f"Sexo: {pacientes[rut]['Sexo']}")
    
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

    if nuevo_nombre:
        pacientes[rut]['Nombre'] = nuevo_nombre
    if nueva_edad:
        pacientes[rut]['Edad'] = nueva_edad
    if nuevo_sexo:
        pacientes[rut]['Sexo'] = nuevo_sexo
    
    print("Paciente actualizado exitosamente.")

# Ver historial del paciente
def ver_historial():
    rut = input("Ingrese RUT del paciente para ver su historial: ").strip().upper()
    tiene_consultas = False
    for consulta in consultas:
        if consulta['rut'] == rut:
            if not tiene_consultas:
                print(f"\nHistorial de consultas para {pacientes[rut]['Nombre']} ({rut}):")
                tiene_consultas = True
            print(f"- Fecha: {consulta['fecha'].strftime('%d/%m/%Y')} | Motivo: {consulta['motivo']}")
    if not tiene_consultas:
        print("Este paciente no tiene consultas registradas.")


def eliminar_paciente():
    pass


def eliminar_consulta():
    pass

def editar_consulta():
    pass