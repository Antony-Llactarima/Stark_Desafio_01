
# BUCLE PRINCIPAL ----------------------------------------------------------------
def main_app(lista_heroes):
    # Datos de la altura de heroes ********************************************
    heroe_M_alto = "None"
    heroe_F_alta = "None"
    heroe_M_bajo = "None"
    heroe_F_baja = "None"
    
    # listas de direntes tipos de heroes ********************************
    # Color de Ojos
    color_ojos = "none"
    heroes_color_ojos = "none"
    # Color de pelo
    color_pelo = "none"
    heroes_color_pelo = "none"
    # Inteligencia
    tipo_inte = "none"
    heroes_inte = "none"
    
    
    continuar = True
    while continuar:
        menu_print()
        opcion = ingresar_opcion()
        match opcion:
            case "A":
                nombre_heroe_DV(lista_heroes, "genero", "M")
            case "B":
                nombre_heroe_DV(lista_heroes, "genero", "F")
            case "C":
                heroe_M_alto = fijar_heroe_max_altura(lista_heroes, "genero", "M")
                print("Superheroe masculino mas alto determinado")
            case "D":
                heroe_F_alta = fijar_heroe_max_altura(lista_heroes, "genero", "F")
                print("Superheroina femenina mas alta determinado")
            case "E":
                heroe_M_bajo = fijar_heroe_min_altura(lista_heroes, "genero", "M")
                print("Superheroe masculino mas bajo determinado")
            case "F":
                heroe_F_baja = fijar_heroe_min_altura(lista_heroes, "genero", "F")
                print("Superheroina femenina mas baja determinado")
            case "G":
                fijar_promedio_altura(lista_heroes, "genero", "M")
            case "H":
                fijar_promedio_altura(lista_heroes, "genero", "F")
            case "I":
                mostrar_heores_altura(heroe_M_alto, heroe_F_alta, heroe_M_bajo, heroe_F_baja)
            case "J":
                lista_ojos = fijar_heroes_tipo(lista_heroes, "color_ojos")
                color_ojos = lista_ojos[0]
                heroes_color_ojos = lista_ojos[1]
                print("Colores de ojos de heroes determinado")
            case "K":
                lista_pelo = fijar_heroes_tipo(lista_heroes, "color_pelo")
                color_pelo = lista_pelo[0]
                heroes_color_pelo = lista_pelo[1]
                print("Colores de pelo de heroes determinado")
            case "L":
                lista_inteligencia = fijar_heroes_tipo(lista_heroes, "inteligencia")
                tipo_inte = lista_inteligencia[0]
                heroes_inte = lista_inteligencia[1]
                print("Tipo de inteligencias de heroes determinado.")
            case "M":
                print("Colores de ojos de Superheroes:")
                print_datos_heroes(lista_heroes, color_ojos, "color_ojos")
            case "N":
                print("Colores de pelo de Superheroes:")
                print_datos_heroes(lista_heroes, color_pelo, "color_pelo")
            case "O":
                print("Distintos tipos de inteligencia:")
                print_datos_heroes(lista_heroes, tipo_inte, "inteligencia")
            case "S":
                continuar = False
            case _:
                print("Error... Opcion no valida")

# MENU PRINCIPAL ----------------------------------------------------------------
def menu_print()->None:
    print("""
*************************************************************************************************
Menu Principal

A. Mostrar superheroes masculinos.
B. Mostrar superheroes femeninos.
C. Determinar superheroe masculino mas alto.
D. Determinar superheroe femenino mas alto.
E. Determinar superheroe masculino menos alto.
F. Determinar superheroe femenino menos alto.
G. Determinar la altura promedio de los superheores masculinos.
H. Determinar la altura promedio de lss superheroes femenino.
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores 
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
S. Salir.
************************************************************************************************
""")

# INGRESO OPCION ----------------------------------------------------------------
def ingresar_opcion()->str:
    opcion = input("Ingrese su opcion: ")
    opcion = opcion.upper()
    return opcion

# TAREAS -------------------------------------------------------------------------

# A- Mostrar personajes masculino
# B- Mostrar personajes femeninos
def nombre_heroe_DV(lista_personajes, dato, valor)->None:
    for heroe in lista_personajes:
        if heroe[dato] == valor:
            print(f"Nombre: {heroe['nombre']}")

# C- Determinar personaje mas alto maculino
# D- Determinar personaje mas alto femenino
def fijar_heroe_max_altura(lista_heroes, dato, valor)->dict:
    flag_altura = True
    for heroe in lista_heroes:
        if heroe[dato] == valor:
            if flag_altura:
                max_altura = float(heroe["altura"])
                max_heroe = heroe
                flag_altura = False
            elif max_altura < float(heroe["altura"]):
                max_altura = float(heroe["altura"])
                max_heroe = heroe
    return max_heroe

# E- Determinar personaje mas bajo masculino
# F- Determinar personaje mas bajo femenino
def fijar_heroe_min_altura(lista_heroes, dato, valor)->dict:
    flag_altura = True
    for heroe in lista_heroes:
        if heroe[dato] == valor:
            if flag_altura:
                min_altura = float(heroe["altura"])
                min_heroe = heroe
                flag_altura = False
            elif min_altura > float(heroe["altura"]):
                min_altura = float(heroe["altura"])
                min_heroe = heroe
    return min_heroe

# G- Dterminar la altura promedio de los personajes masculino
# H- Dterminar la altura promedio de los personajes femeninos
def fijar_promedio_altura(lista_heroes, dato, valor):
    contador_heroes = 0
    altura_total = 0
    for heroe in lista_heroes:
        if heroe[dato] == valor:
            contador_heroes += 1
            altura_total += float(heroe["altura"])
    promedio = altura_total / contador_heroes
    print(f"Promedio de altura de genero {valor}: {promedio}")

# I- Informar altura determinada de los superheroes
def mostrar_heores_altura(heroe_M_alto, heroe_F_alta, heroe_M_bajo, heroe_F_baja):
    if type(heroe_M_alto) == dict:
        print("Heroe masculino mas alto:")
        print(heroe_M_alto["nombre"])
    else:
        print("No se determino al superheroe masculino mas alto.")
    
    if type(heroe_F_alta) == dict:
        print("Heroe femenino mas alta:")
        print(heroe_F_alta["nombre"])
    else:
        print("No se determino la superheroe femenino mas alta.")
    
    if type(heroe_M_bajo) == dict:
        print("Heroe masculino mas alto:")
        print(heroe_M_bajo["nombre"])
    else:
        print("No se determino al superheroe masculino mas bajo.")
    
    if type(heroe_F_baja) == dict:
        print("Heroe femenino mas baja:")
        print(heroe_F_baja["nombre"])
    else:
        print("No se determino la superheroe femenino mas baja.")

# J- Determinar cuantos heroes tienen distintos tipos de color de ojos
# K- Determinar cuantos heroes tienen distintos tipos de color de pelo
# L- Determinar cuantos heroes tienen distintos tipos de inteligencia
def fijar_heroes_tipo(lista_heroes, dato)->list:
    lista_datos = []
    lista_contadores = []
    for heroe in lista_heroes:
        flag = True
        if len(lista_datos) == 0:
            valor = heroe[dato].lower()
            if heroe[dato] == "":
                valor = "No tiene"
            lista_datos.append(valor)
            lista_contadores.append(1)
        else:
            for i in range(len(lista_datos)):
                if lista_datos[i] == heroe[dato].lower():
                    lista_contadores[i] += 1
                    flag = False
            if flag:
                valor = heroe[dato].lower()
                if heroe[dato] == "":
                    valor = "No tiene"
                lista_datos.append(valor)
                lista_contadores.append(1)
                flag = False
    lista_main = [lista_datos, lista_contadores]
    return lista_main

# M- listar todos los superhéroes agrupados por color de ojos.
# N- listar todos los superhéroes agrupados por color de pelo.
# O- listar todos los superhéroes agrupados por tipo de inteligencia.
def print_datos_heroes(lista_heroes, lista_datos, dato):
    if type(lista_datos) == str:
        print("Aun no se determino esta caracteristicas.")
    else:
        for valor in lista_datos:
            print(f"\n{valor}:")
            for heroe in lista_heroes:
                if heroe[dato].lower() == valor:
                    print(heroe['nombre'])
                elif valor == "No tiene" and heroe[dato].lower() == "":
                    print(heroe['nombre'])