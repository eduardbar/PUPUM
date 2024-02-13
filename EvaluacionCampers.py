import menuMatriculas
import Error
import json

def evaluar_modulo(camper, modulo):
    nota_teorica = float(input("Ingrese el 30% de la nota del camper para este módulo: "))
    nota_practica = float(
        input("Ingrese la nota del 60% del camper para este módulo: ")
    )
    nota_quices = float(
        input("Ingrese la nota de los quiz del camper para este módulo: ")
    )

    nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quices * 0.1)

    if nota_final >= 60:
        print(
            f"El camper {camper['NombreCamper']} ha aprobado el módulo {modulo['NombreModulo']} con una nota final de {nota_final}."
        )
        return True
    else:
        print(
            f"El camper {camper['NombreCamper']} no ha aprobado el módulo {modulo['NombreModulo']} con una nota final de {nota_final}."
        )
        return False


def evaluar_campers():
    camper_data = menuMatriculas.cargar_datos("storage/camper.json")
    ruta_data = menuMatriculas.cargar_datos("storage/rutas.json")

    for camper in camper_data:
        ruta_asignada = next(
            (
                ruta
                for ruta in ruta_data
                if ruta["NombreRuta"] == camper["RutaAsignada"]
            ),
            None,
        )
        if ruta_asignada:
            print(
                f"\nEvaluación de camper: {camper['NombreCamper']} {camper['ApellidoCamper']}"
            )
            Error.msgError("Error de ruta")

        for modulo in ruta_asignada["Modulos"]:
            print(f"\nEvaluación del módulo: {modulo['NombreModulo']}")
            if evaluar_modulo(camper, modulo):
                if "Modulos_aprobados" not in camper:
                    camper["Modulos_aprobados"] = []
                camper["Modulos_aprobados"].append(modulo["NombreModulo"])

    with open("storage/camper.json", "w") as file:
        json.dump(camper_data, file, indent=4)
