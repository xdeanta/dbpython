import sqlite3 as dbapi
"""
print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)
"""

try:
    bbdd=dbapi.connect("mibasededatos.dat")
    print(bbdd)

except dbapi.StandardError as e:
    print(e)
else:
    print("Conexion abierta")

try:
    cursor = bbdd.cursor()

except dbapi.StandardError as e:
    print(e)
else:
    print("Cursor preparado")

try:

    #cursor.execute(""" create table usuarios(dni text, nome text, direccion text)""")

    #cursor.execute("""insert into usuarios values('12345X', 'Jose', 'Garcian Barbon 50')""")

    #cursor.execute("""insert into usuarios values('6789A', 'Maria', 'Garcian Barbon 35')""")

    #cursor.execute("""insert into usuarios values('34567X', 'Juan', 'Urzaiz 50')""")

    bbdd.commit()

except dbapi.StandardError as e:
    print(e)
else:
    print("Base de datos creada")

try:
    cursor.execute("select * from usuarios")

    #fetchone a la siguiente tupla
    #fetchall devuelve un objeto iterable con todas las tuplas
    #fetchmany numero de tuplas pasado por parametro

    for fila in cursor.fetchall():
        print("Nombre: " + fila[1])
        print("DNI: " + fila[0])
        print("Direccion: " + fila[2])

except dbapi.DatabaseError as e:
    print("Error en la consulta")
else:
    print("Consulta ejecutada")
finally:
    cursor.close()
    bbdd.close()