# La función filtrar_por_tipo toma un diccionario de datos y un tipo de Pokémon como parámetros.
# Filtra los datos por el tipo especificado y devuelve un nuevo diccionario que contiene solo los datos de los Pokémon del tipo dado.
filtrar_por_tipo = lambda data,tipo: {(v[0],v[1]): v for v in list(filter(lambda data: data[2] == tipo, data.values()))}

'''
# También se puede hacer así: 

def filtrar_por_tipo(data, tipo):
    f = lambda data: data[2] == tipo
    filtrados = {(v[0],v[1]): v for v in list(filter(f, data.values()))}

    return filtrados
'''

# La función fillNAN toma un diccionario de datos y reemplaza cualquier cadena vacía "" con "No tiene".
# Devuelve un nuevo diccionario con los valores actualizados.
fillNAN = lambda data: {(v[0], v[1]): v for v in [["No tiene" if v == "" else v for v in value ] for value in [v for v in data.values()]]}

'''
# También se puede hacer así: 

def fillNAN(data):
    values = [v for v in data.values()]
    values = [["No tiene" if v == "" else v for v in value ] for value in values]
    filled = {(v[0], v[1]): v for v in values}
    return filled
'''

# Datos de ejemplo de Pokémon representados como un diccionario.
datos_pokemon = {(1, 'Bulbasaur'): [1, 'Bulbasaur', 'Grass', 'Poison', 318, 45, 49, 49, 65, 65, 45, 1, 'False'],
                 (4, 'Charmander'): [4, 'Charmander', 'Fire', '', 309, 39, 52, 53, 60, 50, 65, 1, 'False'],
                 (7, 'Squirtle'): [7, 'Squirtle', 'Water', '', 314, 44, 48, 65, 50, 64, 43, 1, 'False'],
                 (6, 'Charizard'): [6, 'Charizard', 'Fire', 'Flying', 534, 78, 84, 78, 109, 85, 100, 1, 'False'],
                 (3, 'Venusaur'): [3, 'Venusaur', 'Grass', 'Poison', 525, 80, 82, 83, 100, 100, 80, 1, 'False']
                 }

# Ejemplo de uso de la función filtrar_por_tipo y fillNAN con los datos de ejemplo de Pokémon.
print(filtrar_por_tipo(datos_pokemon, "Fire")) # Filtra y muestra solo los Pokémon de tipo "Fire".
print(fillNAN(datos_pokemon)) # Reemplaza cadenas vacías con "No tiene" en los datos y muestra el resultado.