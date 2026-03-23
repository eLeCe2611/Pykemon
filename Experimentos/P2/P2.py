# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:06:18 2024

@author: clovi
"""
import pandas as pd
import csv
import statistics
class Pokemon:
    def __init__(self, **args):
        """
        :param args: es un parámetro opcional, si usado, los valores pasados estarán dentro de un diccionario asociado
        a las claves.
        """
        if len(args) > 0:
            # Inicialización de atributos desde el diccionario (si se proporciona)
            self.__pokemonID = args["pokemonID"]
            self.__name = args["name"]
            self.__type1 = args["type1"]
            self.__type2 = args["type2"]
            self.__total = args["total"]
            self.__hp = args["hp"]
            self.__attack = args["attack"]
            self.__defense = args["defense"]
            self.__sp_attack = args["sp_attack"]
            self.__sp_defense = args["sp_defense"]
            self.__speed = args["speed"]
            self.__generation = args["generation"]
            self.__legendary = args["legendary"]
        else:
            # Solicita atributos manualmente al usuario si no se proporciona el diccionario
            self.__pokemonID = (int(input("ID: ")))
            self.__name = input("Name: ")
            self.__type1 = input("Type 1: ")
            self.__type2 = input("Type 2: ") if int(input("¿El Pokèmon tiene más algun tipo?\n1. Sí\n2. No\n")) == 1 else "No tiene"
            self.__hp = int(input("HP: "))
            self.__attack = int(input("Attack: "))
            self.__defense = int(input("Defense: "))
            self.__sp_attack = int(input("Sp. Atk: "))
            self.__sp_defense = int(input("Sp. Def: "))
            self.__speed = int(input("Speed: "))
            self.__total = sum([self.hp, self.attack, self.defense, self.sp_defense, self.sp_attack, self.speed])
            self.__generation = input("Generation: ")
            self.__legendary = True if int(input("¿El Pokèmon es legendario?\n1. Sí\n2. No\n")) == 1 else False

    def __str__(self):
        """
        Método para representar un objeto Pokemon como una cadena de texto formateada.

        Divide el nombre en dos líneas si es muy largo.

        :return: Cadena de texto que representa el Pokémon.
        """
        ancho = 15
        # para nombres mayores que el ancho de la columna, lo dividimos en dos líneas...
        if len(self.name) <= ancho:
            name = self.name.center(ancho)
        else:
            name = ("\n"+ancho*" ").join([n.center(ancho) for n in self.name.split()])
        return  f"{str(self.pokemonID).center(ancho)}{name}{self.type1.center(ancho)}{self.type2.center(ancho)}{str(self.total).center(ancho)}{str(self.hp).center(ancho)}{str(self.attack).center(ancho)}{str(self.defense).center(ancho)}{str(self.sp_attack).center(ancho)}{str(self.sp_defense).center(ancho)}{str(self.speed).center(ancho)}{str(self.generation).center(ancho)}{str(self.legendary).center(ancho)}"


    # Setters y Getters para todos los atributos de la clase
    @property
    def pokemonID(self):
        return self.__pokemonID

    @pokemonID.setter
    def pokemonID(self, pokemonID):
        self.__pokemonID = pokemonID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type1(self):
        return self.__type1

    @type1.setter
    def type1(self, type1):
        self.__type1 = type1

    @property
    def type2(self):
        return self.__type2

    @type2.setter
    def type2(self,type2):
        self.__type2 = type2

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack
    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    @property
    def sp_attack(self):
        return self.__sp_attack

    @sp_attack.setter
    def sp_attack(self, sp_attack):
        self.__sp_attack = sp_attack

    @property
    def sp_defense(self):
        return self.__sp_defense

    @sp_defense.setter
    def sp_defense(self, sp_defense):
        self.__sp_defense = sp_defense
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def generation(self):
        return self.__generation

    @generation.setter
    def generation(self, generation):
        self.__generation = generation

    @property
    def legendary(self):
        return self.__legendary

    @legendary.setter
    def legendary(self, legendary):
        self.__legendary = legendary


class Almacen:
    def __init__(self):
        """
        Constructor de la clase Almacen, inicializa una lista vacía para almacenar Pokémon.
        """
        self.__pokemon_data = list()

    def altaPokemon(self, pokemon):
        """
        Añade un Pokémon a la lista de Pokémon del almacén.

        :param pokemon: El Pokémon a agregar.
        :return: "DUPLICADO" si el Pokémon ya está en la lista, "OK" si se agrega correctamente.
        """
        if pokemon in self.__pokemon_data:
            return "DUPLICADO"
        else:
            self.__pokemon_data.append(pokemon)
            return "OK"

    def buscarPokemon(self, pokemonID):
        """
        Busca un Pokémon por su ID y lo muestra.

        :param pokemonID: La ID del Pokémon a buscar.
        """
        for pokemon in self.pokemon_data:
            if pokemon.pokemonID == pokemonID:
                ancho = 15
                columnas = [atributo[len("_Pokemon__"):] for atributo, valor in vars(self.pokemon_data[0]).items()]
                for columna in columnas:
                    print(columna.center(ancho), end="")
                print("\n")
                print(pokemon)
                break
        else:
            print(f"{pokemonID} no está en los registros.")

    def bajaPokemon(self, pokemonID):
        """
        Elimina un Pokémon de la lista por su ID.

        :param pokemonID: La ID del Pokémon a eliminar.
        """
        for pokemon in self.pokemon_data:
            if pokemon.pokemonID == pokemonID:
                self.pokemon_data.remove(pokemon)
                print("OK")
                break
        else:
            # si el for encerra su ejecución sin pasar por el break, este else se ejecuta
            print("NO LOCALIZADO")

    def listadoPokemon(self):
        """
        Muestra un listado de todos los Pokémon almacenados en el almacén.
        """
        ancho = 15
        # la linea abajo sirve para dinamicamente definir el nombre de cada columna
        columnas = [atributo[len("_Pokemon__"):] for atributo, valor in vars(self.pokemon_data[0]).items()] if len(self.pokemon_data) > 0 else "Colección Vacía."

        if columnas=="Colección Vacía.":
            print(columnas)
        else:
            for columna in columnas:
                print(columna.center(ancho), end="")
            print("\n")
            for pokemon in self.pokemon_data:
                print(pokemon)

    @property
    def pokemon_data(self):
        return self.__pokemon_data

    def agruparPorCampo(self):
        """
        Agrupa Pokémon por un campo específico y calcula estadísticas sobre ellos.

        :return: Lista de tuplas que contienen la media de varios atributos y el tipo más frecuente.
        """
        atributos = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]

        # la función lambda abajo sirve para calcular la media aritmetica de un atributo de los valores de una coleccion de objetos
        calcula_media = lambda atributo: [atributo+" (media): ", statistics.mean([getattr(pokemon, atributo) for pokemon in self.pokemon_data])]
        agrupado = list(map(calcula_media, atributos))
        agrupado.insert(0,self.frecuencia_tipos(1))
        agrupado.insert(1, self.frecuencia_tipos(2))
        return agrupado

    def frecuencia_tipos(self, t:int):
        """
        Calcula la frecuencia de los tipos de Pokémon.

        :param t: Tipo de Pokémon (1 o 2).
        :return: Lista que contiene el tipo más frecuente y su frecuencia.
        """
        if t == 1:
            types1 = [pokemon.type1 for pokemon in self.pokemon_data if pokemon.type1 != "No tiene"]
            types = list(set(types1))
            type_frequency = {t: types1.count(t) for t in types}
            most_frequent_type = types[0]
        elif t == 2:
            types2 = [pokemon.type2 for pokemon in self.pokemon_data if pokemon.type2 != "No tiene"]
            types = list(set(types2))
            type_frequency = {t: types2.count(t) for t in types}
            most_frequent_type = types[0]

        else:
            print("INVALIDO: t =",t)
            return None

        for tipo, cantidad in type_frequency.items():
            if cantidad > type_frequency[most_frequent_type]:
                most_frequent_type = tipo

        return [f"Tipo{t} (más frecuente): ", f"{most_frequent_type}: {type_frequency[most_frequent_type]}"]

    def fromCSV(self, csv_path):
        """
        Lee los datos de Pokémon desde un archivo CSV y los carga en el almacén.

        :param csv_path: La ruta del archivo CSV.
        """
        df = pd.read_csv(csv_path)
        df = df.fillna("No tiene")

        for i in range(len(df)):
            pokemon = Pokemon(
                pokemonID=df.iloc[i]["pokemonID"],
                name=df.iloc[i]["Name"],
                type1=df.iloc[i]["Type 1"],
                type2=df.iloc[i]["Type 2"],
                total=df.iloc[i]["Total"],
                hp=df.iloc[i]["HP"],
                attack=df.iloc[i]["Attack"],
                defense=df.iloc[i]["Defense"],
                sp_attack=df.iloc[i]["Sp. Atk"],
                sp_defense=df.iloc[i]["Sp. Def"],
                speed=df.iloc[i]["Speed"],
                generation=df.iloc[i]["Generation"],
                legendary=df.iloc[i]["Legendary"]
            )

            self.altaPokemon(pokemon)


    def toCSV(self, ruta):
        """
        Guarda los datos de Pokémon en un archivo CSV.

        :param ruta: La ruta del archivo CSV.
        """
        with open(ruta, mode="w", newline='', encoding='utf-8') as f:
            archivo = csv.writer(f)

            archivo.writerow(["pokemonID", "Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"])

            for pokemon in self.pokemon_data:
                archivo.writerow([pokemon.pokemonID,
                                  pokemon.name,
                                  pokemon.type1,
                                  pokemon.type2,
                                  pokemon.total,
                                  pokemon.hp,
                                  pokemon.attack,
                                  pokemon.defense,
                                  pokemon.sp_attack,
                                  pokemon.sp_defense,
                                  pokemon.speed,
                                  pokemon.generation,
                                  pokemon.legendary])

def menu():
    """
    Muestra el menú de opciones y solicita al usuario una opción válida.

    :return: La opción elegida por el usuario.
    """
    texto = """
        1. Agregar un nuevo registro 
        2. Buscar un registro por su clave y mostrar sus valores 
        3. Borrar un registro a partir de su clave 
        4. Listar todos los registros en formato de tabla 
        5. Salir 
        """
    opcion = int(input(texto))
    while not (1 <= opcion <= 5):
        print("Opción inválida.")
        opcion = int(input(texto))

    return opcion

csv_path = "../15_pokemon.csv"
pokemon_collection = Almacen()

# probando la función fromCSV
pokemon_collection.fromCSV(csv_path)

switch = {1: lambda: pokemon_collection.altaPokemon(Pokemon()),
          2: lambda: pokemon_collection.buscarPokemon(int(input("Indique la ID del Pokèmon: "))),
          3: lambda: pokemon_collection.bajaPokemon(int(input("¿Cuál la ID del Pokèmon deseas borrar de los registros? "))),
          4: lambda: pokemon_collection.listadoPokemon()}

opcion = menu()
while opcion != 5:
    switch[opcion]()
    opcion = menu()

# probando la funcion toCSV
pokemon_collection.toCSV("../test.csv")

# probando la función para agruparPorCampo
print("Valores agrupados por campo: ")
agrupado = pokemon_collection.agruparPorCampo()
for campo in agrupado:
    print(campo)