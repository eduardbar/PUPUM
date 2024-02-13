import os
import camper
import rutas
import trainer
import Error
import Asignaciones
import menuMatriculas
import EvaluacionCampers
import moduloReportes

def menuPrincipal():

    while True:
        try:
            print("""
            <<<<<<<<<<<<<<<<<<<
                Menu Campus
            <<<<<<<<<<<<<<<<<<<
                1. Menu Camper
                2. Menu Trainer
                3. Agregar Rutas
                4. Asignaciones
                5. Menu Matriculas
                6. Evaluacion campers
                7. Menu de reportes
                8. Salir
            """)
            op = int(input("\tSeleccione una opcion "))
            if op < 1 or op > 8:
                Error.msgError("Opcion inexistente")
                continue
            return op

        except ValueError:
            Error.msgError("Opcion inexistente")
            continue

def main():
    os.system("cls")  
    while True:
        op = menuPrincipal()
        if op == 1:
            os.system("cls")
            camper.CamperMenu()
        elif op == 2:
            os.system("cls")
            trainer.TrainerMenu()
        elif op ==3:
            os.system("cls")
            rutas.rutasAgregadas()
        elif op == 4:
            os.system("cls")
            Asignaciones.menuAsignacion()
        elif op == 5:
            os.system("cls")
            menuMatriculas.gestor_matriculas()
        elif op == 6:
            os.system("cls")
            EvaluacionCampers.evaluar_campers()
        elif op == 7:
            os.system("cls")
            moduloReportes.menuReportes() 
        elif op == 8:
            print("\nGracias por usar el programa")
            break
        else:
            Error.msgError("Opcion inexistente.")
            continue
            
main()