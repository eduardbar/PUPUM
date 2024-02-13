import Error
import os
import trainer
import json
import camper

def cargarDatos():
    try:
        with open("storage/camper.json") as file:
            campers = json.load(file)
    except FileNotFoundError:
        print("El archivo de campers no existe.")
        campers = []

    try:
        with open("storage/trainers.json") as file:
            trainers = json.load(file)
    except FileNotFoundError:
        print("El archivo de trainers no existe.")
        trainers = []

    try:
        with open("storage/rutas.json") as file:
            rutas = json.load(file)
    except FileNotFoundError:
        print("El archivo de rutas no existe.")
        rutas = []

    return campers, trainers, rutas

def menuReportes():
    while True:
        try:
            print("""
            <<<<<<<<<<<<<<<<<<<<<<<<<<
                Modulo de reportes  
            <<<<<<<<<<<<<<<<<<<<<<<<<<
                1. Campers en inscrrito
                2. Campers que aprobaron el examen inicial
                3. Listar trainers
                4. Estudiantes con bajo rendimiento
                5. Campers y trainers asociados a una ruta
                6. Campers aprobados y reprobados
                7. Campers en riesgo
                8. Salir
            """)
            op = int(input("\tSeleccione una opcion valida: "))
            if op < 1 or op > 7:
                Error.msgError("Seleccion invalida")
                continue
            if op == 1:
                os.system("cls")
                listarCampersInscritos()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                listarCampersAprobadosExamenInicial()
                input("Presione enter para volver al menu ")
            elif op == 3:
                os.system("cls")
                trainer.listarTrainer()
                input("Presione enter para volver al menu ")
            elif op == 4:
                os.system("cls")
                listarCampersBajoRendimiento()
                input("Presione enter para volver al menu ")
            elif op == 5:
                os.system("cls")
                listarCampersYTrainersPorRuta()
                input("Presione enter para volver al menu ")
            elif op == 6:
                os.system("cls")
                listarRendimientoCampersPorModulo()
                input("Presione enter para volver al menu ")
            elif op == 7:
                os.system("cls")
                camper.campers_en_riesgo()
                input("Presione enter para volver al menu ")                                                              
            elif op == 8:
                os.system("cls")
                break
            return op

        except ValueError:
            Error.msgError("Seleccion invalida, intente nuevamente")
            continue

def listarCampersInscritos():
    try:
        with open("storage/camper.json") as file:
            campers = json.load(file)
            campers_inscritos = [camper for camper in campers if camper["Estado"] == "inscrito"]
            if campers_inscritos:
                print("\nCampers en estado de inscrito:")
                for camper in campers_inscritos:
                    print(f"Nombre: {camper['NombreCamper']} {camper['ApellidoCamper']}")
            else:
                print("No hay campers en estado de inscrito.")
    except FileNotFoundError:
        print("El archivo de campers no existe.")


def listarCampersAprobadosExamenInicial():
    try:
        with open("storage/camper.json") as file:
            campers = json.load(file)
            campers_aprobados = [camper for camper in campers if "NotaTeorica" in camper and "NotaPractica" in camper and ((camper["NotaTeorica"] + camper["NotaPractica"]) / 2) >= 60]
            if campers_aprobados:
                print("\nCampers que aprobaron el examen inicial:")
                for camper in campers_aprobados:
                    print(f"Nombre: {camper['NombreCamper']} {camper['ApellidoCamper']}")
            else:
                print("No hay campers que hayan aprobado el examen inicial.")
    except FileNotFoundError:
        print("El archivo de campers no existe.")

def listarCampersBajoRendimiento():
    try:
        with open("storage/camper.json") as file:
            campers = json.load(file)
            campers_bajo_rendimiento = [camper for camper in campers if "NotaTeorica" in camper and "NotaPractica" in camper and ((camper["NotaTeorica"] + camper["NotaPractica"]) / 2) < 50]
            if campers_bajo_rendimiento:
                print("\nCampers con bajo rendimiento:")
                for camper in campers_bajo_rendimiento:
                    print(f"Nombre: {camper['NombreCamper']} {camper['ApellidoCamper']}")
            else:
                print("No hay campers con bajo rendimiento.")
    except FileNotFoundError:
        print("El archivo de campers no existe.")

def listarCampersYTrainersPorRuta():
    campers, trainers, rutas = cargarDatos()
    if not campers:
        print("No hay campers registrados.")
        return
    if not trainers:
        print("No hay trainers registrados.")
        return
    if not rutas:
        print("No hay rutas registradas.")
        return

    try:
        codigo_ruta = int(input("Ingrese el código de la ruta: "))

        ruta_seleccionada = None
        for ruta in rutas:
            if ruta["CodigoRuta"] == codigo_ruta:
                ruta_seleccionada = ruta
                break

        if ruta_seleccionada:
            print(f"\nCampers y trainers asociados a la ruta '{ruta_seleccionada['NombreJornada']}':")
            campers_asociados = [camper for camper in campers if camper.get("RutaAsignada") == ruta_seleccionada["NombreJornada"]]
            if campers_asociados:
                print("\nCampers:")
                for camper in campers_asociados:
                    print(f"- {camper['NombreCamper']} {camper['ApellidoCamper']}")

            trainers_asociados = [trainer for trainer in trainers if trainer.get("Especializacion") == ruta_seleccionada["NombreJornada"]]
            if trainers_asociados:
                print("\nTrainers:")
                for trainer in trainers_asociados:
                    print(f"- {trainer['NombreTrainer']}")

            if not campers_asociados and not trainers_asociados:
                print("No hay campers ni trainers asociados a esta ruta.")
        else:
            print("No se encontró ninguna ruta con ese código.")
    except ValueError:
        Error.msgError("Error. Código de ruta inválido.")

def obtenerNombreTrainer(id_trainer, trainers):
    for trainer in trainers:
        if trainer["IdTrainer"] == id_trainer:
            return trainer["NombreTrainer"]
    return "Desconocido"

def listarRendimientoCampersPorModulo():
    campers, trainers, rutas = cargarDatos()
    if not campers:
        print("No hay campers registrados.")
        return
    if not trainers:
        print("No hay trainers registrados.")
        return
    if not rutas:
        print("No hay rutas registradas.")
        return

    try:
        codigo_ruta = int(input("Ingrese el código de la ruta: "))

        ruta_seleccionada = None
        for ruta in rutas:
            if ruta["CodigoRuta"] == codigo_ruta:
                ruta_seleccionada = ruta
                break

        if ruta_seleccionada:
            nombre_ruta = ruta_seleccionada["NombreJornada"]
            print(f"\nRendimiento de los campers en los módulos para la ruta '{nombre_ruta}':")

            for trainer in trainers:
                campers_asociados = [camper for camper in campers if camper.get("RutaAsignada") == nombre_ruta and camper.get("TrainerAsignado") == trainer["IdTrainer"]]
                if campers_asociados:
                    print(f"\nTrainer: {trainer['NombreTrainer']}")
                    print("Campers:")
                    for camper in campers_asociados:
                        print(f"- {camper['NombreCamper']} {camper['ApellidoCamper']}:")
                        for modulo in camper.get("Modulos_aprobados", []):
                            print(f"  - {modulo}")
                else:
                    print(f"\nNo hay campers asociados al trainer '{trainer['NombreTrainer']}' en la ruta '{nombre_ruta}'.")

        else:
            print("No se encontró ninguna ruta con ese código.")
    except ValueError:
        Error.msgError("Error. Código de ruta inválido.")        