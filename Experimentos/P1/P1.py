# Funcion que usamos para actualizar la columna total de un pokemon cuando editamos alguno de los valores de estadistica
def actualizarTotal(lista):
    lista[2]=sum(lista[3:9])

# Opcion 1: Agregar un nuevo pokemon
def agregar():
    # Preguntamos por los datos del nuevo Pokemon
    id_pokemon = int(input('Introduce id: '))
    nombre = input('Introduce nombre: ')
    tipo1 = input('Introduce tipo 1: ')
    t2 = input('Tiene tipo 2?(s/n)')
    tipo2 = input('Introduce tipo 2:') if t2 == 's' else None
    vida = int(input('Introduce vida: '))
    ataque = int(input('Introduce ataque: '))
    defensa = int(input('Introduce defensa: '))
    atEsp = int(input('Introduce ataque especial: '))
    defEsp = int(input('Introduce defensa especial: '))
    velocidad = int(input('Introduce velocidad: '))
    total = vida + ataque + defensa + defEsp + atEsp + velocidad
    generacion = int(input('Introduce generacion: '))
    leg = input('Es legendario?(s/n)')
    legendario = True if leg == 's' else False

    # Creamos una tupla como clave y una lista como valor
    clave = (id_pokemon, nombre)
    valor = [tipo1, tipo2, total, vida, ataque, defensa, atEsp, defEsp, velocidad, generacion, legendario]

    # Almacenamos en el diccionario
    datos_pokemon[clave] = valor


# Opcion 2: Buscar un pokemon por su clave
def buscar(dic, clavePok):
    # Creamos una lista pokemonEncontrado con los nombres que coincidan con la clave clavePok
    pokemonEncontrado = [nombre for id, nombre in dic.keys() if id == clavePok]
    # Comprobamos si la clave existe en el diccionario
    if len(pokemonEncontrado) < 1:  
        # Si no se encuentra ningún Pokemon con esa clave devolvemos None, indicando que no se encontro ningun Pokemon
        return None, None
    elif len(pokemonEncontrado) == 1:  
        # Si solo encontramos Pokemon con esa clave devolvemos la tupla correspondiente al Pokemon encontrado y su nombre
        return dic.get((clavePok, pokemonEncontrado[0])), pokemonEncontrado[0]
    else:  
        # Si encontramos múltiples Pokemon con la misma clave
        while True:
            print(f"Se encontraron múltiples Pokemon para la id: '{clavePok}':")
            # Mostramos los nombres de los Pokemon encontrados con esa clave junto con un número de identificación
            for i, nombre in enumerate(pokemonEncontrado, start=1):
                print(f"{i}. {nombre}")
            # Pedimos al usuario que seleccione el número del Pokemon que desea
            seleccion = int(input("Seleccione el número del Pokemon que deseas: "))
            if 1 <= seleccion <= len(pokemonEncontrado):  
                # Si la selección es válida devolvemos la tupla correspondiente al Pokemon seleccionado y su nombre
                return dic.get((clavePok, pokemonEncontrado[seleccion - 1])), pokemonEncontrado[seleccion - 1]
            else:  
                # Si la selección no es válida se lo indicamos al usuario
                print("Selección no válida.")

# Opcion 3: Buscar un registro por su clave, editarlo y mostrar sus valores
def editar(dic, clavePok):
    # Llamamos a la función buscar para obtener la información del Pokémon asociada al id
    valor, nombrePoke = buscar(dic, clavePok)
    # Verificamos si se encontró información del Pokémon
    if valor:
        # Si encontramos dicho Pokemon mostramos sus datos antes de permitir su edicion
        print(f'Id = {clavePokemon}, Nombre = {nombrePoke}: Tipo1 = {valor[0]}, Tipo 2 = {valor[1]}, Total = {valor[2]}, Vida = {valor[3]}, Ataque = {valor[4]}, '
              f'Defensa = {valor[5]}, Ataque Especial = {valor[6]}, Defensa Especial = {valor[7]}, Velocidad = {valor[8]}, '
              f'Generacion = {valor[9]}, Legendario = {valor[10]}')
        # Comenzamos un bucle infinito para permitir editar mas de un valor
        while True:
            
            print('Indica que valor quieres editar:')
            print('1. Tipo 1')
            print('2. Tipo 2')
            print('3. Vida')
            print('4. Ataque')
            print('5. Defensa')
            print('6. Ataque Especial')
            print('7. Defensa Especial')
            print('8. Velocidad')
            print('9. Generacion')
            print('10. Legendario')
            # Preguntamos al usuario qué valor desea editar
            opcion = int(input("Selecciona una opción (1-10): "))
            
            # Verificamos que la opcion este entre las posibles
            if 1<=opcion<=10:
                lista = dic[(clavePok, nombrePoke)]
                match opcion:
                    case 1:
                        # Editamos tipo 1
                        lista[0]=input('Introduce nuevo tipo 1: ')
                    case 2:
                        # Editamos tipo 2
                        lista[1]=input('Introduce nuevo tipo 2: ')
                    case 3:
                        # Editamos vida
                        lista[3]=int(input('Introduce nueva vida: '))
                        # Llamamos a la funcion actualizarTotal() para que se actualice el total de sus estadisticas
                        actualizarTotal(lista)
                    case 4:
                        # Editamos ataque
                        lista[4] = int(input('Introduce nuevo ataque: '))
                        actualizarTotal(lista)
                        # Llamamos a la funcion actualizarTotal() para que se actualice el total de sus estadisticas
                    case 5:
                        # Editamos defensa
                        lista[5] = int(input('Introduce nueva defensa: '))
                        actualizarTotal(lista)
                        # Llamamos a la funcion actualizarTotal() para que se actualice el total de sus estadisticas
                    case 6:
                        # Editamos ataque especial
                        lista[6] = int(input('Introduce nuevo ataque especial: '))
                        actualizarTotal(lista)
                        # Llamamos a la funcion actualizarTotal() para que se actualice el total de sus estadisticas
                    case 7:
                        # Editamos defensa especial
                        lista[7] = int(input('Introduce nueva defensa especial: '))
                        actualizarTotal(lista)
                        # Llamamos a la funcion actualizarTotal() para que se actualice el total de sus estadisticas
                    case 8:
                        # Editamos velocidad
                        lista[8] = int(input('Introduce nueva velocidad: '))
                        actualizarTotal(lista)
                        # Llamamos a la funcion actualizarTotal() para que se actualice el total de sus estadisticas
                    case 9:
                        # Editamos generacion
                        lista[9] = int(input('Introduce nueva generacion: '))
                    case 10:
                        # Editamos valor legendario
                        leg = input('Es legendario?(s/n)')
                        lista[10] = True if leg == 's' else False
                # Abrimos otro bucle infinito para asegurarnos que el usuario responde correctmente a la pregunta de que si quiere realizar mas ediciones
                while True:
                    opcion = input('Desea editar otro dato?(s/n) ')
                    # En caso de que sea correcta la respuesta salimos del bucle
                    if opcion == 's' or opcion == 'n':
                        break
                    else:
                        print('Opcion incorrecta. Introduzca s o n.')
                # Si la respuesta del usuario era que no queria realizar mas ediciones salimos del bucle con un break
                if opcion == 'n':
                    break
            else:
                # En caso de que la opcion no sea correcta informamos y volvemos a preguntar
                print("Opcion incorrecta, introduzca valor entre 1 y 10.")
        # Finalmente devolvemos la tupla correspondiente al Pokemon seleccionado y su nombre con los valores editados
        return dic[(clavePok, nombrePoke)], nombrePoke
    else:
        # Si no se encuentra ningún Pokemon con esa clave devolvemos None, indicando que no se encontro ningun Pokemon
        return None, None

# Opcion 4: Eliminar un registro a partir de su clave
def eliminar(dic, clavePok):
    # Llamamos a la función buscar para obtener la información del Pokémon asociada al id
    infoPoke, nombre = buscar(dic, clavePok)
    # Verificamos si se encontró información del Pokémon
    if infoPoke:
        # Si encontramos información, eliminamos la entrada correspondiente en el diccionario usando su id y el nombre
        del dic[(clavePok, nombre)]
        # Devolvemos True para indicar que la eliminación fue realizada
        return True
    else:
        # Si no encontramos información devolvemos False para indicar que no se pudo realizar la eliminación
        return False


# Opcion 5: Listar todos los registros en forma de tabla
def listar(dic):
    # Usamos un for que recorre todos los items del diccionario datos_pokemon
    for clave, valor in datos_pokemon.items():
        print(f'Id = {clave[0]}, Nombre = {clave[1]}: Tipo1 = {valor[0]}, Tipo 2 = {valor[1]}, Total = {valor[2]}, Vida = {valor[3]}, Ataque = {valor[4]}, '
              f'Defensa = {valor[5]}, Ataque Especial = {valor[6]}, Defensa Especial = {valor[7]}, Velocidad = {valor[8]}, '
              f'Generacion = {valor[9]}, Legendario = {valor[10]}')


# Importamos csv para usar sus métodos
import csv
from math import atan

# Nombre del archivo CSV
archivo_csv ="../15_pokemon.csv"

# Diccionario para almacenar los datos
datos_pokemon = {}

# Abrimos el archivo en formato lectura 'r' y lo almacena en archivo.
# Con with nos aseguramos que al salir del mismo, el archivo se cerrará automáticamente
with open(archivo_csv, 'r') as archivo:
    # Clase de python que se encarga de leer archivos csv.
    # Almacenamos esta función en lector_csv
    lector_csv = csv.reader(archivo)

    # Saltamos la primera fila que contiene los encabezados
    next(lector_csv)

    # Iteramos sobre las filas del archivo CSV
    for fila in lector_csv:
        # Obtenemos los valores de cada columna
        id_pokemon = int(fila[0])
        nombre = fila[1]
        tipo1 = fila[2]
        tipo2 = fila[3] if fila[3] else None
        total = int(fila[4])
        vida = int(fila[5])
        ataque = int(fila[6])
        defensa = int(fila[7])
        atEsp = int(fila[8])
        defEsp = int(fila[9])
        velocidad = int(fila[10])
        generacion = int(fila[11])
        # Convierte el valor a un booleano
        legendario = fila[12] == 'True'

        # Creamos una tupla como clave y una lista como valor
        clave = (id_pokemon, nombre)
        valor = [tipo1, tipo2, total, vida, ataque, defensa, atEsp, defEsp, velocidad, generacion, legendario]

        # Almacenamos en el diccionario
        datos_pokemon[clave] = valor

# Bucle infinito para usar menu hasta que el usuario decida salir
while True:
    print('')
    print('MENU')
    print('---------------------')
    print('1. Agregar un nuevo registro')
    print('2. Buscar un registro por su clave y mostrar sus valores')
    print('3. Buscar un registro por su clave, editarlo y mostrar sus valores')
    print('4. Borrar un registro a partir de su clave')
    print('5. Listar todos los registros en forma de tabla')
    print('6. Salir')
    print('---------------------')
    # Almacenamos en opcion la eleccion del usuario
    opcion = input("Selecciona una opción (1-6): ")

    # Llamamos a la funcion elegida por usuario (match=switch)
    match opcion:
        case "1":
            # Opcion 1: Agregar un nuevo pokemon
            print('Opcion 1:')
            #Llamamos a la funcion correspondiente
            agregar()
        case "2":
            # Opcion 2: Buscar un pokemon por su clave
            print('Opcion 2: ')
            # Pedimos al usuario la clave que quiere buscar
            clavePokemon = int(input('Introduce id: '))
            #Llamamos a la funcion correspondiente, la cual nos devuelve el nombre del pokemon y una lista de los valores
            valor, nombrePoke = buscar(datos_pokemon, clavePokemon)
            #Si se encuentra dicho pokemon mostramos por pantalla sus valores
            if valor:
                print('Pokemon encontrado: ')
                print(f'Id = {clavePokemon}, Nombre = {nombrePoke}: Tipo1 = {valor[0]}, Tipo 2 = {valor[1]}, Total = {valor[2]}, Vida = {valor[3]}, Ataque = {valor[4]}, '
                      f'Defensa = {valor[5]}, Ataque Especial = {valor[6]}, Defensa Especial = {valor[7]}, Velocidad = {valor[8]}, '
                      f'Generacion = {valor[9]}, Legendario = {valor[10]}')
            #En caso contrario indicamos el error
            else:
                print('Pokemon no encontrado')
        case "3":
            # Opcion 3: Buscar un registro por su clave, editarlo y mostrar sus valores
            print('Opcion 3: ')
            # Pedimos al usuario la clave que quiere editar
            clavePokemon = int(input('Introduce id: '))
            #Llamamos a la funcion correspondiente, la cual nos devuelve el nombre del pokemon y una lista de los valores
            valor, nombrePoke = editar(datos_pokemon, clavePokemon)
            #Si se encuentra dicho pokemon mostramos por pantalla sus valores editados
            if valor:
                print('Pokemon encontrado: ')
                print(f'Id = {clavePokemon}, Nombre = {nombrePoke}: Tipo1 = {valor[0]}, Tipo 2 = {valor[1]}, Total = {valor[2]}, Vida = {valor[3]}, Ataque = {valor[4]}, '
                      f'Defensa = {valor[5]}, Ataque Especial = {valor[6]}, Defensa Especial = {valor[7]}, Velocidad = {valor[8]}, '
                      f'Generacion = {valor[9]}, Legendario = {valor[10]}')
            #En caso contrario indicamos el error
            else:
                print('Pokemon no encontrado')
        case "4":
            # Opcion 4: Eliminar un registro a partir de su clave
            print('Opcion 4: ')
            # Pedimos al usuario la clave que quiere eliminar
            clavePokemon = int(input('Introduce id: '))
            #Llamamos a la funcion correspondiente, la cual nos devuelve un booleano segun si se ha completado la accion o no
            #Esto nos sirve para informar al usuario de si su peticion se ha realizadi
            if eliminar(datos_pokemon, clavePokemon):
                print('Pokemon eliminado correctamente')
            else:
                print('El Pokemon no existe')
        case "5":
            # Opcion 5: Listar todos los registros en forma de tabla
            print('Opcion 5: ')
            # Llamamos a la funcion correspondiente
            listar(datos_pokemon)
        case "6":
            #Opcion 6: Salir
            print('ADIOS')
            #break para salir del bucle
            break
        case _:
            #Opcion incorrecta
            print("Opcion incorrecta, introduzca valor entre 1 y 6.")