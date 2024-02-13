import camper
import Error
import os
import json
import rutas
import trainer
def menuAsignacion():
    while True:
        try:
            print("""
            <<<<<<<<<<<<<<<<<<<<<<<<<
                Menu Asignaciones
            <<<<<<<<<<<<<<<<<<<<<<<<<
                1. Asignacion Notas
                2. Asignacion Rutas
                3. Salir
            """)
            op = int(input("\tSeleccione una opcion valida: "))
            if op < 1 or op > 3:
                Error.msgError("Esta opcion no es valida")
                continue
            if op == 1:
                os.system("cls")
                NotasAsignadas()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                menuAsignacionesRutas()
            elif op == 3:
                os.system("cls")
                break
            return op

        except ValueError:
            Error.msgError("Error. Opcion Invalida (de 1 a 3)")
            continue


def menuAsignacionesRutas():
    while True:
        try:
            print("""
            <<<<<<<<<<<<<<<<<<<
                Menu camper
            <<<<<<<<<<<<<<<<<<<
                1. Ruta a camper
                2. Ruta a trainer
                3. Salir
            """)
            op = int(input("\tSeleccione una opcion valida: "))
            if op < 1 or op > 3:
                Error.msgError("Seleccione una opcion valida")
                continue
            if op == 1:
                os.system("cls")
                asignarCamperaRuta()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                asignarRutaTrainer()
                input("Presione enter para volver al menu ")
            elif op == 3:
                break
            return op
        except ValueError:
            Error.msgError("Error. Opcion Invalida (de 1 a 3)")
            continue
        

def NotasAsignadas():
    mostrar_campers = camper.cargarCampers()
    campers_inscritos = [
        camper for camper in mostrar_campers if camper["Estado"].lower() == "inscrito"
    ]
    if not mostrar_campers:
        print("No hay camper registrado. Por favor agregue uno")
        camper.agregarCamper()
        return

    print("Lista de campers en estado de inscritos")
    for i, camper in enumerate(campers_inscritos, start=1):
        print(f"{i}. {camper['NombreCamper']}")

    while True:
        try:
            seleccion = int(input("Elija un Camper (0 para agregar uno nuevo): "))
            if 0 <= seleccion <= len(campers_inscritos):
                break
            else:
                Error.msgError("Error \nSeleccion invalida, intentelo de nuevo")

        except ValueError:
            Error.msgError("Error \nNumero invalido")

    if seleccion == 0:
        camper.agregarCamper()
    else:
        camper_seleccionado = campers_inscritos[seleccion - 1]
        nota_teorica = float(
            input(
                f"Ingrese la Nota teorica para el estudiante {camper_seleccionado['NombreCamper']}: "
            )
        )
        nota_practica = float(
            input(
                f"Ingrese la Nota practica para el estudiante {camper_seleccionado['NombreCamper']}: "
            )
        )
        promedio = (nota_teorica + nota_practica) / 2

        if promedio >= 60:
            print("Aprobado")
            # Cambiar el estado del camper a "aprobado"
            camper_seleccionado["Estado"] = "aprobado"
        else:
            print("Reprobado")

        camper_seleccionado["NotaTeorica"] = nota_teorica
        camper_seleccionado["NotaPractica"] = nota_practica

        camper.guardarCampers(mostrar_campers)


def asignarCamperaRuta():
    mostrar_campers = camper.cargarCampers()

    campers_aprobados = [
        camper for camper in mostrar_campers if camper["Estado"].lower() == "aprobado"
    ]

    if not campers_aprobados:
        print("No hay campers aprobados para asignar a una ruta.")
        return

    print("Lista de campers aprobados disponibles:")
    for i, camper in enumerate(campers_aprobados, start=1):
        print(f"{i}. {camper['NombreCamper']}")

    while True:
        try:
            seleccion_camper = int(
                input("Seleccione un Camper (0 para volver atrás): ")
            )
            if 0 <= seleccion_camper <= len(campers_aprobados):  
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")

        except ValueError:
            Error.msgError("Error: Número inválido")

    if seleccion_camper == 0:
        return  

    camper_seleccionado = campers_aprobados[seleccion_camper - 1]

    rutas_disponibles = rutas.cargarRutas()

    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    camper_seleccionado["RutaAsignada"] = ruta_seleccionada["NombreRuta"]
    print(
        f"Ruta '{ruta_seleccionada['NombreRuta']}' asignada al camper '{camper_seleccionado['NombreCamper']}' con éxito."
    )
    camper.guardarCampers(mostrar_campers)


def asignarRutaTrainer():
    mostrar_trainers = trainer.cargarTrainers()

    print("Lista de trainers disponibles:")
    for i, trainer in enumerate(mostrar_trainers, start=1):
        print(f"{i}. {trainer['NombreTrainer']}")

    while True:
        try:
            seleccion_trainer = int(
                input("Seleccione un Trainer (0 para volver atrás): ")
            )
            if 0 <= seleccion_trainer <= len(mostrar_trainers):
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")

        except ValueError:
            Error.msgError("Error: Número inválido")

    if seleccion_trainer == 0:
        return  

    trainer_seleccionado = mostrar_trainers[seleccion_trainer - 1]

    rutas_disponibles = rutas.cargarRutas()

    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return 
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    trainer_seleccionado["RutaAsignada"] = ruta_seleccionada["NombreRuta"]
    print(
        f"Ruta '{ruta_seleccionada['NombreRuta']}' asignada al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito."
    )
    trainer.guardarTrainers(mostrar_trainers)
    
    with open("storage/horario.json") as file:
        horarios = json.load(file)

    print("Lista de horarios disponibles:")
    for horario in horarios:
        print(f"{horario['Codigo']}. {horario['NombreJornada']} - {horario['Hora']['HoraInicio']} a {horario['Hora']['HoraFinal']}")

    while True:
        try:
            codigo_horario = int(
                input("Seleccione un horario por su código (0 para volver atrás): ")
            )
            if codigo_horario == 0:
                return  
            horario_seleccionado = next(
                (
                    horario
                    for horario in horarios
                    if horario["Codigo"] == codigo_horario
                ),
                None,
            )
            if horario_seleccionado:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    trainer_seleccionado["HorarioAsignado"] = horario_seleccionado["NombreJornada"]
    print(f"Horario '{horario_seleccionado['NombreJornada']}' asignado al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito.")

    trainer.guardarTrainers(mostrar_trainers)
    mostrar_trainers = trainer.cargarTrainers()

    print("Lista de trainers disponibles:")
    for i, trainer in enumerate(mostrar_trainers, start=1):
        print(f"{i}. {trainer['NombreTrainer']}")

    while True:
        try:
            seleccion_trainer = int(
                input("Seleccione un Trainer (0 para volver atrás): ")
            )
            if 0 <= seleccion_trainer <= len(mostrar_trainers):
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")

        except ValueError:
            Error.msgError("Error: Número inválido")

    if seleccion_trainer == 0:
        return  

    trainer_seleccionado = mostrar_trainers[seleccion_trainer - 1]

    rutas_disponibles = rutas.cargarRutas()

    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    trainer_seleccionado["RutaAsignada"] = ruta_seleccionada["NombreRuta"]
    print(
        f"Ruta '{ruta_seleccionada['NombreRuta']}' asignada al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito."
    )
    trainer.guardarTrainers(mostrar_trainers)
    
    with open("storage/horario.json") as file:
        horarios = json.load(file)

    print("Lista de horarios disponibles:")
    for horario in horarios:
        print(f"{horario['Codigo']}. {horario['NombreJornada']} - {horario['Hora']['HoraInicio']} a {horario['Hora']['HoraFinal']}")

    while True:
        try:
            codigo_horario = int(
                input("Seleccione un horario por su código (0 para volver atrás): ")
            )
            if codigo_horario == 0:
                return 
            horario_seleccionado = next(
                (
                    horario
                    for horario in horarios
                    if horario["Codigo"] == codigo_horario
                ),
                None,
            )
            if horario_seleccionado:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    trainer_seleccionado["HorarioAsignado"] = horario_seleccionado["NombreJornada"]
    print(f"Horario '{horario_seleccionado['NombreJornada']}' asignado al trainer '{trainer_seleccionado['NombreTrainer']}' con éxito.")
    rutas_disponibles = rutas.cargarRutas()
    if not rutas_disponibles:
        print("No hay rutas disponibles para asignar.")
        return

    print("Lista de rutas disponibles:")
    for ruta in rutas_disponibles:
        print(f"{ruta['CodigoRuta']}. {ruta['NombreRuta']}")

    while True:
        try:
            codigo_ruta = int(
                input("Seleccione una ruta por su código (0 para volver atrás): ")
            )
            if codigo_ruta == 0:
                return  
            ruta_seleccionada = next(
                (
                    ruta
                    for ruta in rutas_disponibles
                    if ruta["CodigoRuta"] == codigo_ruta
                ),
                None,
            )
            if ruta_seleccionada:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    trainer["RutaAsignada"] = ruta_seleccionada["NombreRuta"]

    with open("storage/horario.json") as file:
        horarios = json.load(file)

    print("Lista de horarios disponibles:")
    for horario in horarios:
        print(f"{horario['Codigo']}. {horario['NombreJornada']} - {horario['Hora']['HoraInicio']} a {horario['Hora']['HoraFinal']}")

    while True:
        try:
            codigo_horario = int(
                input("Seleccione un horario por su código (0 para volver atrás): ")
            )
            if codigo_horario == 0:
                return  
            horario_seleccionado = next(
                (
                    horario
                    for horario in horarios
                    if horario["Codigo"] == codigo_horario
                ),
                None,
            )
            if horario_seleccionado:
                break
            else:
                Error.msgError("Error: Selección inválida, intente nuevamente")
        except ValueError:
            Error.msgError("Error: Código inválido")

    trainer["HorarioAsignado"] = horario_seleccionado["NombreJornada"]
    print(f"Ruta '{ruta_seleccionada['NombreRuta']}' y horario '{horario_seleccionado['NombreJornada']}' asignados al trainer '{trainer['NombreTrainer']}' con éxito.")
    trainer.guardarTrainers(mostrar_trainers)