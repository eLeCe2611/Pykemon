import sqlite3
import csv


#conexión base de datos SQL y tabla
def crear_bdato():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    #crear la tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pokemon (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Type_1 TEXT,
                    Type_2 TEXT,
                    Total INTEGER,
                    HP INTEGER,
                    Attack INTEGER,
                    Defense INTEGER,
                    SP_Atk INTEGER,
                    SP_Def INTEGER,
                    Speed INTEGER,
                    Generation INTEGER,
                    Legendary TEXT
                    )''')
    conn.commit()
    conn.close()


#leer dataset en CSV y insertar registros en tabla
def insertar_datos():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    with open('15_pokemon.csv', 'r', encoding='utf-8') as file:
        next(file, None)  # Saltar la cabecera
        reader = csv.reader(file, delimiter=',')
        
        for row in reader:
            cursor.execute("INSERT INTO Pokemon (Name, Type_1, Type_2, Total, HP, Attack, Defense, SP_Atk, SP_Def, Speed, Generation, Legendary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row[1:])

    conn.commit()
    conn.close()


#sentencia select con where
def seleccionar_where():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Pokemon WHERE Type_1 = 'Fire' AND HP > 80 LIMIT 10''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()


#sentencia uptate con where
def actualizar_datos():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE Pokemon SET Type_1 = 'Electric' WHERE Speed > 100''')

    conn.commit()
    conn.close()


#sentencia select con agrupamiento y agregación
def seleccionar_grupo():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT Type_1, AVG(HP) FROM Pokemon GROUP BY Type_1''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()


#sentencia delete con where
def delete_data():
    conn = sqlite3.connect('pokemon.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM Pokemon WHERE Type_2 = 'Poison' AND Defense < 50''')

    conn.commit()
    conn.close()


#operaciones
crear_bdato()
insertar_datos()
print("Datos insertados.")
seleccionar_where()
actualizar_datos()
print("Datos actualizados.")
seleccionar_grupo()
delete_data()
print("Datos eliminados.")