from datetime import datetime

# Diccionario que contiene los ruts(como clave) y datos(como valor) del paciente 
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
    print("3. agregar consulta")
    print("5. Salir")
    op = int(input("Elige una opción: "))
    return op

# Ingresar pacientes
def registrar_paciente():  
    rut = input("Ingrese RUT del paciente sin punto y con guion: ").strip().upper()
    # Evita duplicados
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
        print(f"RUT: {rut}, \nNombre: {info['Nombre']} \nEdad: {info['Edad']} \nSexo: {info['Sexo']}")
        print("*"*30)

# Se agrega una consulta a la lista
def agregar_consulta(rut):
    if rut not in pacientes:
        print("Paciente no encontrado.")
        return
    try:
        fecha_str = input("Fecha de la consulta (DD/MM/AAAA): ").strip()
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
    except ValueError:
        print("Fecha inválida. Usa el formato DD/MM/AAAA.")
        return
    motivo = input("Motivo de la consulta: ").strip()
    consultas.append({'rut': rut, 'fecha': fecha, 'motivo': motivo})
    print("Consulta agregada.")
    


def editar_paciente():
    pass



def eliminar_paciente():
    pass

def ver_historial():
    pass