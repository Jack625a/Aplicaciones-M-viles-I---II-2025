import flet as ft
#Paso1. Importar sqlite
import sqlite3

#Paso2. FUNCION PARA SQLITE3
def basedatos():
    #Paso 2.1. Crear la conexion a la base de datos
    conexion=sqlite3.connect("dbApp2")
    #Paso 2.2. Inicializar la conexion
    inicializar=conexion.cursor()
    #Paso 2.3. Ejecutar la consulta SQL
    inicializar.execute("" \
    "CREATE TABLE IF NOT EXISTS " \
    "estudiante "
    "(id INTEGER PRIMARY KEY, nombre TEXT, carrera TEXT)")

    inicializar.execute('' \
    'INSERT INTO estudiante '
    '(nombre,carrera) VALUES '
    '("Kevin Arroyo","Ingenieria de Sistemas"),'
    '("Juan","Ingenieria de Sistemas"),' \
    '("Ana","Medicina")')

    #Paso 2.4. Enviar la solicitud
    conexion.commit()
    #Paso 2.5. Cerrar la conexion
    conexion.close()

basedatos()

def main(page: ft.Page):
    
    page.add(
       
    )


ft.app(main)
