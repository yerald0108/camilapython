import json
import os

def crear_familia():
    """Crea una nueva familia con sus integrantes y la agrega al archivo JSON."""
    global familias
    familia = {} 
    familia_next = len(familias) + 1
    familia_numero = len(familias) + 1
    familia_key = f"Familia {familia_numero}" 
    familia[familia_key] = []

    while True:
        nombre = input("Ingrese el nombre del integrante (o 'fin' para finalizar): ")
        if nombre.lower() == 'fin':
            break
        edad = int(input("Ingrese la edad del integrante: "))
        sexo = input("Ingrese el sexo del integrante (M/F): ").upper()
        while sexo not in ["M", "F"]:
            sexo = input("Sexo inválido. Ingrese M para Masculino o F para Femenino: ").upper()
        raza = input("Ingrese la raza del integrante (B/N/M): ").upper()
        while raza not in ["B", "N", "M"]:
            raza = input("Raza inválido. Ingrese B para Blanco, N para Negro y M para Mestiso: ").upper()
        enfermedades = input("Ingrese las enfermedades o patologías del integrante (separadas por comas): ").split(",")
        integrante = {
            "Nombre": nombre,
            "Edad": edad,
            "Sexo": sexo,
            "Raza": raza,
            "Enfermedades": enfermedades
        }
        familia[familia_key].append(integrante)

    familias.update(familia)
    familia_numero += 1
    familia_next += 1
    guardar_datos()
    
    print("\nFamilia creada correctamente.")
    print(f"Actualmente hay {len(familias)} familias creadas, siguiente número de familia será el {familia_next}.")

def editar_familia():
    """Permite editar las familias y sus integrantes."""
    global familias
    familia_next = len(familias) + 1
    familia_numero = len(familias) + 1
    while True:
        print("\nOpciones de edición:")
        print("1. Agregar persona a una familia")
        print("2. Eliminar un integrante de una familia")
        print("3. Editar información de un integrante")
        print("4. Eliminar una familia")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nListado de familias:")
            for i, (numero_familia, familia) in enumerate(familias.items(), start=1):
                print(f"{i}. Familia {i}")
            if len(familias) == 0:
                print("\nNo hay familias creadas aún.")
            else:
                index_familia = int(input("Ingrese el número de la familia a la que agregar el integrante: ")) - 1
                while index_familia < 0 or index_familia >= len(familias):
                    index_familia = int(input("Número de familia inválido. Ingrese un número válido: ")) - 1
                familia_key = list(familias.keys())[index_familia]
                while True:
                    nombre = input("Ingrese el nombre del integrante (o 'fin' para finalizar): ")
                    if nombre.lower() == 'fin':
                        break
                    edad = int(input("Ingrese la edad del integrante: "))
                    sexo = input("Ingrese el sexo del integrante (M/F): ").upper()
                    while sexo not in ["M", "F"]:
                        sexo = input("Sexo inválido. Ingrese M para Masculino o F para Femenino: ").upper()
                    raza = input("Ingrese la raza del integrante (B/N/M): ").upper()
                    while raza not in ["B", "N", "M"]:
                        raza = input("Raza inválido. Ingrese B para Blanco, N para Negro y M para Mestiso: ").upper()
                    enfermedades = input("Ingrese las enfermedades o patologías del integrante (separadas por comas): ").split(",")
                    integrante = {
                        "Nombre": nombre,
                        "Edad": edad,
                        "Sexo": sexo,
                        "Raza": raza,
                        "Enfermedades": enfermedades
                    }
                    familias[familia_key].append(integrante)
                guardar_datos()
                print("\nIntegrante agregado correctamente.")
                
        elif opcion == "2":
            print("\nListado de familias:")
            for i, (numero_familia, familia) in enumerate(familias.items(), start=1):
                print(f"{i}. Familia {i}")
            if len(familias) == 0:
                print("\nNo hay familias creadas aún.")
            else:
                index_familia = int(input("Ingrese el número de la familia a la que eliminar el integrante: ")) - 1
                while index_familia < 0 or index_familia >= len(familias):
                    index_familia = int(input("Número de familia inválido. Ingrese un número válido: ")) - 1
                familia_key = list(familias.keys())[index_familia]
                if len(familias[familia_key]) == 0:
                    print("\nLa familia no tiene integrantes.")
                else:
                    for i, integrante in enumerate(familias[familia_key]):
                        print(f"{i+1}. {integrante['Nombre']}")
                    index_eliminar = int(input("Ingrese el número del integrante a eliminar: ")) - 1
                    while index_eliminar < 0 or index_eliminar >= len(familias[familia_key]):
                        index_eliminar = int(input("Número inválido. Ingrese un número válido: ")) - 1
                    del familias[familia_key][index_eliminar]
                    guardar_datos()
                    print(f"Integrante eliminado correctamente.")
                    
        elif opcion == "3":
            print("\nListado de familias:")
            for i, (numero_familia, familia) in enumerate(familias.items(), start=1):
                print(f"{i}. Familia {i}")
            if len(familias) == 0:
                print("\nNo hay familias creadas aún.")
            else:
                index_familia = int(input("Ingrese el número de la familia a la que editar el integrante: ")) - 1
                while index_familia < 0 or index_familia >= len(familias):
                    index_familia = int(input("Número de familia inválido. Ingrese un número válido: ")) - 1
                familia_key = list(familias.keys())[index_familia]
                if len(familias[familia_key]) == 0:
                    print("\nLa familia no tiene integrantes.")
                else:
                    for i, integrante in enumerate(familias[familia_key]):
                        print(f"{i+1}. {integrante['Nombre']}")
                    index_editar = int(input("Ingrese el número del integrante a editar: ")) - 1
                    while index_editar < 0 or index_editar >= len(familias[familia_key]):
                        index_editar = int(input("Número inválido. Ingrese un número válido: ")) - 1
                    integrante = familias[familia_key][index_editar]
                    nombre = input(f"Nuevo nombre (actual: {integrante['Nombre']}): ")
                    edad = int(input(f"Nueva edad (actual: {integrante['Edad']}): "))
                    sexo = input(f"Nuevo sexo (actual: {integrante['Sexo']}): ").upper()
                    while sexo not in ["M", "F"]:
                        sexo = input("Sexo inválido. Ingrese M para Masculino o F para Femenino: ").upper()
                    raza = input(f"Nueva raza (actual: {integrante['Raza']}): ").upper()
                    while raza not in ["B", "N", "M"]:
                        raza = input("Raza inválido. Ingrese B para Blanco, N para Negro y M para Mestiso: ").upper()
                    enfermedades = input(f"Nuevas enfermedades (actual: {', '.join(integrante['Enfermedades'])}): ").split(",")
                    integrante.update({
                        "Nombre": nombre,
                        "Edad": edad,
                        "Sexo": sexo,
                        "Raza": raza,
                        "Enfermedades": enfermedades
                    })
                    familias[familia_key][index_editar] = integrante
                    guardar_datos()
                    print(f"\nInformación del integrante actualizada correctamente.")
        elif opcion == "4":
            if len(familias) == 0:
                print("\nNo hay familias creadas aún.")
            else:
                print("\nListado de familias:")
                for i, familia_key in enumerate(familias.keys()):
                    print(f"{i+1}. {familia_key}")
                index_eliminar = int(input("Ingrese el número de la familia a eliminar: ")) - 1
                while index_eliminar < 0 or index_eliminar >= len(familias):
                    index_eliminar = int(input("Número inválido. Ingrese un número válido: ")) - 1
                familia_key = list(familias.keys())[index_eliminar]
                del familias[familia_key]
                guardar_datos()
                familia_numero += -1
                familia_next += -1
                print(f"\nFamilia eliminada correctamente.")
                print(f"Actualmente hay {len(familias)} familias creadas, siguiente número de familia será el {familia_next}.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
            
def buscar_datos():
    """Busca integrantes por edad, sexo, raza y enfermedad."""
    global familias

    if not familias:
        print("\nNo hay familias registradas.")
        return

    # 1. Pregunta por la edad
    while True:
        try:
            opcion_edad = int(input("\n¿Cómo quieres buscar por edad?\n"
                                   "1. Buscar por intervalo de edad\n"
                                   "2. Buscar edades mayores que\n"
                                   "3. Buscar edades menores que\n"
                                   "4. Buscar sin especificar edad\n"
                                   "Elige una opción (1-4): "))
            if 1 <= opcion_edad <= 4:
                break
            else:
                print("Opción inválida. Por favor, elige una opción entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    edad_minima = 0
    edad_maxima = 0

    if opcion_edad == 1:
        while True:
            try:
                edad_minima = int(input("Ingrese la edad mínima: "))
                edad_maxima = int(input("Ingrese la edad máxima: "))
                if edad_minima <= edad_maxima:
                    break
                else:
                    print("La edad mínima debe ser menor o igual que la edad máxima.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

    elif opcion_edad == 2:
        edad_minima = int(input("Ingrese la edad mínima: "))
    elif opcion_edad == 3:
        edad_maxima = int(input("Ingrese la edad máxima: "))

    # 2. Pregunta por el sexo
    while True:
        sexo_buscado = input("Ingrese el sexo del integrante (M/F) (o presiona Enter para buscar sin sexo): ").upper()
        if sexo_buscado in ("M", "F", ""):
            break
        else:
            print("Opción inválida. Por favor, ingresa 'M', 'F', o presiona Enter.")

    # 3. Pregunta por la raza
    while True:
        
        raza_buscada = input("Ingrese la raza del integrante (B/N/M) (o presiona Enter para buscar sin raza): ").upper()
        if raza_buscada in ("B", "N", "M", ""):
            break
        else:
            print("Raza inválido. Ingrese 'B' para Blanco, 'N' para Negro, 'M' para Mestiso:, o presiona Enter.")

    # 4. Pregunta por la enfermedad
    enfermedad_buscada = input("Ingrese las enfermedades que desea buscar (separadas por coma, o presiona Enter para buscar sin enfermedad): ").upper()
    enfermedad_buscada = enfermedad_buscada.split(",") if enfermedad_buscada else []

    # Búsqueda
    integrantes_encontrados = []
    for numero_familia, familia in familias.items():
        for i, integrante in enumerate(familia):
            if opcion_edad == 4 or ( # Buscar sin especificar edad
                (opcion_edad == 1 and edad_minima <= integrante["Edad"] <= edad_maxima) or \
                (opcion_edad == 2 and integrante["Edad"] >= edad_minima) or \
                (opcion_edad == 3 and integrante["Edad"] <= edad_maxima)
            ):
                if (sexo_buscado == "TODOS" or sexo_buscado == "" or integrante["Sexo"] == sexo_buscado) and \
                   (not raza_buscada or raza_buscada.upper() == integrante["Raza"].upper()) and \
                   all(enfermedad in integrante["Enfermedades"] for enfermedad in enfermedad_buscada): # Buscar EXACTAMENTE todas las enfermedades
                    integrantes_encontrados.append(
                        {"Familia": numero_familia, "Integrante": i + 1, "Datos": integrante}
                    )

    if integrantes_encontrados:
        print("\nIntegrantes encontrados:")
        familia_actual = None
        for integrante in integrantes_encontrados:
            if familia_actual != integrante['Familia']: # Separar por familia
                print("-" * 20) # Guion como separador
                familia_actual = integrante['Familia']
            print(f"    Familia: {integrante['Familia']}")
            print(f"    Integrante: {integrante['Integrante']}")
            print(f"    Nombre: {integrante['Datos']['Nombre']}")
            print(f"    Edad: {integrante['Datos']['Edad']}")
            print(f"    Sexo: {integrante['Datos']['Sexo']}")
            print(f"    Raza: {integrante['Datos']['Raza']}")
            if integrante['Datos']['Enfermedades']:
                print(f"    Enfermedades: {', '.join(integrante['Datos']['Enfermedades'])}")
            else:
                print(f"    Enfermedades: No hay enfermedades registradas")
            print() # Espacio en blanco para separar por integrante

        print(f"Se encontraron {len(integrantes_encontrados)} integrantes con las características especificadas.") # <-- Total de integrantes
    else:
        print(f"\nNo se encontró ningún integrante con las características especificadas.")
            
def guardar_datos():
    """Guarda los datos de la población en el archivo JSON."""
    with open("poblacion.json", "w") as f:
        datos_poblacion = {
            nombre_poblacion: nombre_consultorio
        }
        for i, (familia_key, integrantes) in enumerate(familias.items()):
            datos_poblacion[familia_key] = []
            for j, integrante in enumerate(integrantes):
                integrante_enum = f"Integrante {j+1}"
                datos_poblacion[familia_key].append({integrante_enum: integrante})
        json.dump(datos_poblacion, f, indent=4)
       
def cargar_datos():
    """Carga los datos de la población desde el archivo JSON."""
    global familias, nombre_poblacion, nombre_consultorio
    try:
        with open("poblacion.json", "r") as f:
            data = json.load(f)
            nombre_poblacion = list(data.keys())[0]
            nombre_consultorio = data[nombre_poblacion]
            familias = {key: [integrante[list(integrante.keys())[0]] for integrante in value] for key, value in data.items() if key != nombre_poblacion}
    except FileNotFoundError:
        familias = {}

def mostrar_familias():
    """Muestra la información de todas las familias."""
    global familias
    if not familias:
        print("\nNo hay familias registradas.")
    else:
        print("\nFamilias creadas:")
        total_integrantes = 0
        for i, (numero_familia, familia) in enumerate(familias.items(), start=1): 
            total_integrantes += len(familia)
        print("-" * 20) # Guion como separador
        for i, familia_key in enumerate(familias.keys()):
            print(f"{familia_key}:")
            for j, integrante in enumerate(familias[familia_key]):
                print(f" Integrante {j+1}:")
                for key, value in integrante.items():
                    if key == "Enfermedades":
                        print(f"    {key}: {', '.join(value)}")
                    else:
                        print(f"    {key}: {value}")
                print()
        print(f"Tienes creadas {len(familias)} familias y un total de {total_integrantes} integrantes.") # <-- Total de familias y de integrantes.

def buscar_integrante():
    """Busca un integrante específico por número de familia y número de integrante."""
    global familias

    if not familias:
        print("\nNo hay familias registradas.")
        return

    while True:
        # Mostrar familias organizadas por número
        print("\nFamilias registradas:")
        for i, familia in enumerate(familias.keys()):
            print(f"{i + 1}. {familia}")

        try:
            numero_familia = int(input("Ingrese el número de la familia: "))
            if 1 <= numero_familia <= len(familias):
                break
            else:
                print("Número de familia inválido. Por favor, ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido para la familia.")

    familias_list = list(familias.keys())
    familia_buscada = familias_list[numero_familia - 1]

    while True:
        # Mostrar integrantes organizados por número
        print(f"\nIntegrantes de la familia {familia_buscada}:")
        for i, integrante in enumerate(familias[familia_buscada]):
            print(f"{i + 1}. {integrante['Nombre']}")

        try:
            numero_integrante = int(input(f"Ingrese el número del integrante: "))
            if 1 <= numero_integrante <= len(familias[familia_buscada]):
                break
            else:
                print(f"Número de integrante inválido para la familia {numero_familia}. Por favor, ingrese un número válido.")
        except ValueError:
            print("Por favor, ingrese un número válido para el integrante.")

    integrante_encontrado = familias[familia_buscada][numero_integrante - 1]

    print(f"\nDatos del integrante (familia {numero_familia}, integrante {numero_integrante}):")
    for key, value in integrante_encontrado.items():
        if key == "Enfermedades":
            print(f"    {key}: {', '.join(value)}")
        else:
            print(f"    {key}: {value}")
            
def menu_principal():
    """Muestra el menú principal del programa."""
    global familias
    while True:
        print(f"\n--- Menú Principal - Población: {nombre_poblacion} - Consultorio: {nombre_consultorio} ---")
        print("1. Crear Familia")
        print("2. Editar Familia")
        print("3. Mostrar Familias")
        print("4. Buscar Datos")
        print("5. Buscar Integrante") # Nueva opción
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_familia()
        elif opcion == "2":
            editar_familia()
        elif opcion == "3":
            mostrar_familias()
        elif opcion == "4":
            buscar_datos()
        elif opcion == "5":
            buscar_integrante() # Llamada a la función Buscar Integrante
        elif opcion == "6":
            print("¡Hasta Luego!")
            break
        else:
            print("Opción inválida.")

# Inicialización del programa
familias = {}
cargar_datos()

if os.path.exists("poblacion.json"): # Verifica si existe el archivo JSON
    print("Archivo JSON encontrado. Se cargarán los datos existentes.")
else:
    nombre_poblacion = input("Ingrese el nombre de la población: ")
    nombre_consultorio = input("Ingrese el nombre del consultorio: ")

menu_principal()