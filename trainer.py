import Error
import os
import json

def TrainerMenu():
    while True:
        try:
            print("""
            <<<<<<<<<<<<<<<<<<<
                Menu Trainer
            <<<<<<<<<<<<<<<<<<<
                1. Crear Trainer
                2. Editar Trainer
                3. Buscar Trainer
                4. Salir
            """)    
            op = int(input("\tSeleccione una opcion valida: "))
            if op < 1 or op > 5:
                Error.msgError("Opcion invalida, intente nuevamente")
                continue
            if op == 1:
                os.system("cls")
                trainerAgregado()
                input("Presione enter para volver al menu ")
            elif op == 2:
                os.system("cls")
                editarTrainer()
                input("Presione enter para volver al menu ")    
            elif op == 3:
                os.system("cls") 
                buscarTrainer()
                input("Presione enter para volver al menu ")     
            elif op == 4:
                os.system("cls")
                break  
            return op     
        except ValueError:
            Error.msgError("Opcion invalida intente de nuevo")
            continue

def cargarTrainers():
    try: 
        with open ('storage/trainer.json', 'r') as trainers_file:
            trainers= json.load(trainers_file)
        
    except FileNotFoundError:
        trainers= []
    return trainers

def guardarTrainers(trainers): 
    with open('storage/trainer.json', 'w') as trainers_file:
        json.dump(trainers, trainers_file, indent=4 )   

def trainerAgregado():
    print("Formulario Trainer")

    id_trainer= None
    while id_trainer is None:
        try:
            id_trainer= int(input("Ingrese la identificacion del trainer: "))
        except ValueError:
            Error.msgError("Identificacion invalida")
            
    nombre_trainer= input("Ingrese el nombre del Trainer: ")
    while not nombre_trainer:
        Error.msgError("Nombre de Trainer Invalido")
        nombre_trainer= input("Ingrese el nombre del Trainer: ")

    esp_trainer= input("Ingrese la especializacion del trainer: ")
    while not esp_trainer:
        Error.msgError("Especializacion no definida")
        esp_trainer= input("Ingrese la especializacion del trainer: ")

    diccionario_trainers= {
        "IdTrainer": id_trainer,
        "NombreTrainer": nombre_trainer,
        "Especializacion": esp_trainer,
    }

    listaTrainer= cargarTrainers()
    listaTrainer.append(diccionario_trainers)
    guardarTrainers(listaTrainer)   
    print("Trainer Agregado Exitosamente")

def listarTrainer():
    trainers = cargarTrainers()
    print("Lista de Trainers: ")
    for index, trainer in enumerate(trainers, start=1):
        print(f"{index}. {trainer['NombreTrainer']}")

def editarTrainer():
    print("MODIFICAR TRAINERS")
    listarTrainer()
    modificar_trainer = input("Ingrese el nombre del trainer que desea modificar: ")
    listTrainer = cargarTrainers()
    encontrado = False
    for trainer in listTrainer:
        if trainer['NombreTrainer'] == modificar_trainer:
            print("Trainer Encontrado: ")
            print(f"Identificacion: {trainer['IdTrainer']}")
            print(f"Nombre: {trainer['NombreTrainer']}")
            print(f"Especializacion: {trainer['Especializacion']}")
            print()
            
            pregunta = input("Desea Modificar la identificacion? (S/N)")                       
            if pregunta.upper() == "S":
                idTrainer = None
                while idTrainer is None:
                    try:
                        idTrainer = int(input("Nueva Identificacion: "))
                    except ValueError:
                        Error.msgError("Numero no valido")
                trainer['IdTrainer'] = idTrainer
                    
            pregunta = input("Desea Modificar el nombre? (S/N)")                       
            if pregunta.upper() == "S":            
                trainer['NombreTrainer'] = input("Nuevo Nombre: ")
                while not trainer['NombreTrainer']:
                    Error.msgError("El nombre no puede estar vacio")
                    trainer['NombreTrainer'] = input("Nuevo Nombre: ")
                
            pregunta = input("Desea Modificar la especializacion? (S/N)")                       
            if pregunta.upper() == "S":                
                trainer['Especializacion'] = input("Nueva especializacion: ")
                while not trainer['Especializacion']:
                    Error.msgError("La especializacion no puede estar vacia")
                    trainer['Especializacion'] = input("Nueva Especializacion: ")    

            pregunta = input("Desea Modificar la edad? (S/N)")                       
            if pregunta.upper() == "S":
                trainer['Edad'] = input("Nueva Edad: ")
                while not trainer['Edad']:
                    Error.msgError("La edad no puede estar vacia")
                    trainer['Edad'] = input("Nueva Edad: ")
                
            pregunta = input("Desea Modificar el genero? (S/N)")                       
            if pregunta.upper() == "S":                
                trainer['Genero'] = input("Nuevo Genero: ")
                while not trainer['Genero']:
                    Error.msgError("El genero no puede estar vacio")
                    trainer['Genero'] = input("Nuevo Genero: ")
                     
            encontrado = True
            break       
    if encontrado:
        guardarTrainers(listTrainer)
        print("Trainer modificado exitosamente")
    else:
        print("Trainer no encontrado")                                    
            
def buscarTrainer():
    print("BUSCAR TRAINER")
    trainers = cargarTrainers()
    nombre_buscar = input("Ingrese el nombre del camper que desea buscar: ")
    encontrado = False
    for trainer in trainers:
        if trainer['NombreTrainer'] == nombre_buscar:
            encontrado = True
            print("Trainer encontrado:")
            print(f"Identificacion: {trainer['IdTrainer']}")
            print(f"Nombre: {trainer['NombreTrainer']}")
            print(f"Especialidad: {trainer['Especializacion']}")
            print()
    if not encontrado:
        print("Trainer no encontrado.")       
                



