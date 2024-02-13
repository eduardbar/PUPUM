import Error
import json

def cargarRutas():
    try:
        with open('storage/rutas.json', 'r') as fileRutas:
            rutas= json.load(fileRutas)
        
    except FileNotFoundError: 
        rutas = []
    return rutas

def guardarRutas(rutas):
    with open('storage/rutas.json', 'w') as fileRutas:
        json.dump(rutas,fileRutas, indent=4)

def rutasAgregadas():
    print("AGREGAR RUTAS DE ENTRENAMIENTO")

    cantidad_rutas = int(input("Cuantas rutas que desea agregar: "))
    while cantidad_rutas <= 0:
        Error.msgError("Debe ingresar minimo una ruta de entrenamiento")
        cantidad_rutas = int(input("Ingrese la cantidad de rutas que desea agregar: "))

    listaRutas = cargarRutas()  

    for i in range(1, cantidad_rutas + 1):
        print(f"\nRuta {i}")

        codigo_ruta = None
        while codigo_ruta is None:
            try:
                codigo_ruta = int(input("Ingrese codigo para la ruta: "))
            except ValueError:
                Error.msgError("Numero no valido")

        nombre_ruta = input("Escriba el nombre de la ruta de entrenamiento: ")
        while not nombre_ruta:
            Error.msgError("El nombre de la ruta no puede estar vacío")
            nombre_ruta = input("Escriba el nombre de la ruta de entrenamiento: ")

        cantidad_modulos = int(
            input("Ingrese la cantidad de modulos que desea agregar: ")
        )
        while cantidad_modulos <= 0:
            Error.msgError("Debe ingresar al menos un modulo")
            cantidad_modulos = int(
                input("Ingrese la cantidad de modulos que desea agregar: ")
            )

        modulos = []

        for j in range(1, cantidad_modulos + 1):
            print(f"\nModulo {j}")

            codigo_modulo = None
            while codigo_modulo is None:
                try:
                    codigo_modulo = int(input(f"Escriba el codigo del modulo: "))
                except ValueError:
                    Error.msgError("El codigo debe ser un número valido")

            nombre_modulo = input(
                f"Escriba el nombre del modulo de la ruta {nombre_ruta}: "
            )
            while not nombre_modulo:
                Error.msgError("El nombre no puede estar vacío")
                nombre_modulo = input(
                    f"Escriba el nombre del modulo de la ruta {nombre_ruta}: "
                )

            cantidad_temas = int(
                input(f"Ingrese la cantidad de temas para el modulo {nombre_modulo}: ")
            )
            while cantidad_temas <= 0:
                Error.msgError("¡Debe ingresar al menos un tema!")
                cantidad_temas = int(
                    input(
                        f"Ingrese la cantidad de temas para el modulo {nombre_modulo}: "
                    )
                )

            temas = []

            for k in range(1, cantidad_temas + 1):
                nombre_tema = input(
                    f"Escriba el nombre del tema {k} del modulo {nombre_modulo}: "
                )
                while not nombre_tema:
                    Error.msgError("¡El nombre no puede estar vacío!")
                    nombre_tema = input(
                        f"Escriba el nombre del tema {k} del modulo {nombre_modulo}: "
                    )

                temas.append({"NombreTema": nombre_tema})

            modulos.append(
                {
                    "CodigoModulo": codigo_modulo,
                    "NombreModulo": nombre_modulo,
                    "Temas": temas,
                }
            )

        listaRutas.append(
            {"CodigoRuta": codigo_ruta, "NombreRuta": nombre_ruta, "Modulos": modulos}
        )

    guardarRutas(listaRutas) 

def listarRutas():
    rutas = cargarRutas()

    if not rutas:
        print("No hay rutas disponibles.")
        return

    print("\nLista de rutas disponibles:")
    for ruta in rutas:
        print(f"\nRuta {ruta['CodigoRuta']}: {ruta['NombreRuta']}")
        print("Modulos:")
        for modulo in ruta["Modulos"]:
            print(f"  - Módulo {modulo['CodigoModulo']}: {modulo['NombreModulo']}")
            print("    Temas:")
            for tema in modulo["Temas"]:
                print(f"      * {tema['NombreTema']}")
