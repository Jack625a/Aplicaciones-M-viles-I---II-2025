import flet as ft
#Paso1. Importar sqlite
import sqlite3

#Paso2. FUNCION PARA SQLITE3
def basedatos():
    #Paso 2.1. Crear la conexion a la base de datos
    conexion=sqlite3.connect("dbAppInterfaz")
    #Paso 2.2. Inicializar la conexion
    inicializar=conexion.cursor()
    #Paso 2.3. Ejecutar la consulta SQL
    inicializar.execute("" \
    "CREATE TABLE IF NOT EXISTS " \
    "estudiante "
    "(id INTEGER PRIMARY KEY, nombre TEXT, carrera TEXT, foto TEXT)")

    #inicializar.execute('' \
    #'INSERT INTO estudiante '
    #'(nombre,carrera,foto) VALUES '
    #'("Kevin Arroyo","Ingenieria de Sistemas","https://media.sproutsocial.com/uploads/2022/06/profile-picture.jpeg"),'
    #'("Juan","Ingenieria de Sistemas.","https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGVyZmlsfGVufDB8fDB8fHww"),' \
    #'("Ana","Medicina","https://inmofotos.es/wp-content/uploads/2021/10/imagen-1_Mesa-de-trabajo-1.jpg")')

    #Paso 2.4. Enviar la solicitud
    conexion.commit()
    #Paso 2.5. Cerrar la conexion
    conexion.close()

basedatos()

#funcion para añadir nuevos registros
def añadirRegistros(nombre,carrera,foto):
    conexion=sqlite3.connect("dbAppInterfaz")
    inicializar=conexion.cursor()
    inicializar.execute("INSERT INTO estudiante (nombre,carrera,foto) VALUES (?,?,?)",
                        (nombre,carrera,foto))
    conexion.commit()
    conexion.close()

#Funcion para obtener los datos
def obtenerDatos():
    connexion=sqlite3.connect("dbAppInterfaz")
    selector=connexion.cursor()
    selector.execute(
        "SELECT * FROM estudiante WHERE carrera='Derecho'"
    )
    filas=selector.fetchall()
    connexion.close()
    return filas


#Interfaz
def main(page: ft.Page):
    #Activar el scroll
    page.scroll=ft.ScrollMode.AUTO
    # FORMULARIO PARA AGREGAR NUEVOS REGISTROS
    titulo=ft.Text("Insertar Nuevos Registros",size=20)
    nombre=ft.TextField(label="Ingrese un nombre: " )
    carrera=ft.TextField(label="Ingrese la carrera: ")
    foto=ft.TextField(label="Ingrese una foto: ")
    

    #Funcion para añadir un registro
    def añadir(e):
        nombreObtenido=nombre.value.strip()
        carreraObtenido=carrera.value.strip()
        fotoObtenido=foto.value.strip()
        if not nombreObtenido and not carreraObtenido:
            page.open(ft.SnackBar(ft.Text("Debe completar los campos para continuar...")))
            #page.snack_bar.open()=True
            page.update()
            return
        else:
            añadirRegistros(nombreObtenido,carreraObtenido,fotoObtenido)
            page.open(ft.SnackBar(ft.Text("Se registro correctamente...")))
            nombreObtenido.value=""
            carreraObtenido.value=""
            fotoObtenido.value=""
            page.update()

    #Boton para registrar
    registrar=ft.CupertinoFilledButton("Registrar", on_click=añadir)

    #Mostrar los datos
    datos=obtenerDatos()
    if not datos:
        print("No hay registros que mostrar...")
        estudiantes=[]
    else:
        estudiantes=ft.Text(value=datos)
        

    page.add(
        ft.Column([
        titulo,
        nombre,
        carrera,
        foto,
        registrar,
        estudiantes
        ],
        width=350)
        
       
    )


ft.app(main)
