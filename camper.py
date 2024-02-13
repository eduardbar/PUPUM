import Error
import os
import json
import menuMatriculas

def CamperMenu():
    while True:
        try:
            print("""
            <<<<<<<<<<<<<<<<<<<
                Menu camper
            <<<<<<<<<<<<<<<<<<<
                1. Crear Camper
                2. Editar Camper
                3. Buscar Camper
                4. Salir
            """)            
            op = int(input("\tSeleccione una opcion valida: "))
            if op < 1 or op > 5:
                Error.msgError("Opcion inexistente")
                continue
            if op == 1:
                os.system("cls")
                agregarCamper()
                input("Presione enter para volver al menu")
            elif op == 2:
                os.system("cls")
                camper_a_modificar =input("Ingrese el nombre del camper que desea modificar: ")
                editarCamper(camper_a_modificar)
                input("Presione enter para volver al menu")
            elif op == 3:
                os.system("cls")
                buscarCamper()
                input("Presione enter para volver al menu")
            elif op == 4:
                os.system("cls")
                break
            return op

        except ValueError:
            Error.msgError("Opcion inexistente")
            continue

def cargarCampers():
    try:
        with open('storage/camper.json', 'r') as fileCamper:
            campers = json.load(fileCamper) 

    except FileNotFoundError:
        campers = []
    return campers    

def guardarCampers(campers):
    with open('storage/camper.json', 'w') as fileCamper:
        json.dump(campers, fileCamper, indent=4)

def agregarCamper():

    id_camper = None
    while id_camper is None:
        try:
            id_camper = int(input("Ingrese numero de Identificacion del camper: "))
        except ValueError:
            Error.msgError("Ingrese un numero valido")

    nombre_camper = input("Ingrese nombre del camper: ")
    while not nombre_camper:
        Error.msgError("El nombre no puede estar vacio")
        nombre_camper = input("Ingrese nombre del camper: ")

    apellido_camper = input("Ingrese Apellidos del camper: ")
    while not apellido_camper:
        Error.msgError("El Apellido no puede estar vacio")
        apellido_camper = input("Ingrese Apellidos del camper: ")

    tel_celular = None
    while tel_celular is None:
        try:
            tel_celular = int(input("Ingrese el numero celular  del camper: "))
        except ValueError:
            Error.msgError("Ingrese un numero valido")

    tel_fijo = None
    while tel_fijo is None:
        try:
            tel_fijo = int(input("Ingrese numero fijo del camper: "))
        except ValueError:
            Error.msgError("Ingrese un numero valido")

    estado = input("Ingrese el estado del camper: ")
    while not estado:
        Error.msgError("El estado no puede estar vacio")
        estado = input("Ingrese el estado del camper: ")

    camper_diccionario = {
        "IdCamper": id_camper,
        "NombreCamper": nombre_camper,
        "ApellidoCamper": apellido_camper,
        "Contacto": {"telefonoCelular": tel_celular, "telefonoFijo": tel_fijo},
        "Estado": estado,
    }

    listCamper = cargarCampers()
    listCamper.append(camper_diccionario)
    guardarCampers(listCamper)
    print("Camper Agregado Exitosamente")

def mostrarListaCampers():
    campers = cargarCampers()
    print("Lista de Campers:")
    for index, camper in enumerate(campers, start=1):
        print(f"{index}. {camper['NombreCamper']} {camper['ApellidoCamper']}")

def editarCamper(camper_a_modificar):
    print("Edicion Camper")
    listCamper = cargarCampers()
    encontrado = False
    for camper in listCamper:
        if camper["NombreCamper"] == camper_a_modificar:
            print(f"Camper encontrado: {camper}")

            camper["NombreCamper"] = input("Nombre del camper: ")
            while not camper["NombreCamper"]:
                Error.msgError("El nombre no puede estar vacio")
                camper["NombreCamper"] = input("Nombre del camper: ")

            camper["ApellidoCamper"] = input("Apellido del camper: ")
            while not camper["ApellidoCamper"]:
                Error.msgError("El Apellido no puede estar vacio")
                camper["ApellidoCamper"] = input("Apellido del camper")

            tel_celular = None
            while tel_celular is None:
                try:
                    tel_celular = int(input("Numero de celular del camper: "))
                except ValueError:
                    Error.msgError("Numero no valido")
            camper["TelContacto"]["telefonoCelular"] = tel_celular

            tel_fijo = None
            while tel_fijo is None:
                try:
                    tel_fijo = int(input("Numero fijo del camper: "))
                except ValueError:
                    Error.msgError("Contacto Invalido")
            camper["TelContacto"]["telefonoFijo"] = tel_fijo
            break

    if encontrado:
        guardarCampers(listCamper)
        print("Camper modificado exitosamente.")
    else:
        print("Camper no encontrado.")

def buscarCamper():
    print("BUSCAR CAMPER: ")
    campers = cargarCampers()
    nombre_buscar = input("Ingrese el nombre del camper a consultar: ")
    encontrado = False
    for camper in campers:
        if camper["NombreCamper"] == nombre_buscar:
            encontrado = True
            print("Camper encontrado:")
            print(f"Identificacion: {camper['IdentificacionCamper']}")
            print(f"Nombre: {camper['NombreCamper']} {camper['ApellidoCamper']}")
            print(f"Direccion: {camper['DireccionCamper']}")
            print(
                f"Nombre del Acudiente: {camper['AcudienteCamper']['NombreAcudiente']}"
            )
            print(
                f"Identificacion del Acudiente: {camper['AcudienteCamper']['IdAcudiente']}"
            )
    if not encontrado:
        print("Camper no encontrado.")

def campersRiesgo():
    print("**CAMPERS EN RIESGO BAJO**")
    campers = cargarCampers

def campers_en_riesgo():
    camper_data = menuMatriculas.cargar_datos('storage/camper.json')
    ruta_data = menuMatriculas.cargar_datos('storage/rutas.json')

    campers_riesgo = []

    for camper in camper_data:
        ruta_asignada = next((ruta for ruta in ruta_data if ruta['NombreRuta'] == camper['RutaAsignada']), None)
        if ruta_asignada:
            for modulo in ruta_asignada['Modulos']:
                if 'Notas' in camper and camper['Notas'].get(modulo['NombreModulo'], 0) < 60:
                    campers_riesgo.append(camper)
                    break 

    if campers_riesgo:
        print("\nCampers en riesgo:")
        for camper in campers_riesgo:
            print(f"{camper['NombreCamper']} {camper['ApellidoCamper']} - Ruta: {camper['RutaAsignada']}")
    else:
        print("\nNo hay campers en riesgo.")