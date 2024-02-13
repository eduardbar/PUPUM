import json
from datetime import datetime, timedelta

def cargar_datos(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

def guardar_matricula(matricula):
    with open('storage/matriculas.json', 'a') as file:
        json.dump(matricula, file, indent=4)
        file.write('\n')  

def asignar_matricula(camper, ruta, trainer, salon):
    fecha_inicio = datetime.now().strftime('%Y-%m-%d')
    fecha_finalizacion = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

    matricula = {
        "Camper": f"{camper['NombreCamper']} {camper['ApellidoCamper']}",
        "Ruta_de_entrenamiento": ruta['NombreRuta'],
        "Trainer": trainer['NombreTrainer'],
        "Salon": salon['NombreSala'],
        "Fecha_de_inicio": fecha_inicio,
        "Fecha_de_finalizacion": fecha_finalizacion
    }

    print("\nMatrícula asignada:")
    print(json.dumps(matricula, indent=2))


    guardar_matricula(matricula)

def gestor_matriculas():
    camper_data = cargar_datos('camper.json')
    ruta_data = cargar_datos('rutas.json')
    trainer_data = cargar_datos('trainers.json')
    salon_data = cargar_datos('salones.json')

    campers_aprobados = [camper for camper in camper_data if camper['Estado'] == 'aprobado']

    if not campers_aprobados:
        print("No hay campers aprobados para matricular.")
        return

    for i, camper in enumerate(campers_aprobados):
        ruta = ruta_data[i % len(ruta_data)]  
        trainer = trainer_data[i % len(trainer_data)]  
        salon = salon_data[i % len(salon_data)]  
        asignar_matricula(camper, ruta, trainer, salon)