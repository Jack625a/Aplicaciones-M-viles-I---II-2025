import flet as ft
import sqlite3

# Paso 2. Función para crear la BD
def basedatos():
    conexion = sqlite3.connect("dbAppInterfaz")
    inicializar = conexion.cursor()
    inicializar.execute(
        "CREATE TABLE IF NOT EXISTS estudiante "
        "(id INTEGER PRIMARY KEY, nombre TEXT, carrera TEXT, foto TEXT)"
    )
    conexion.commit()
    conexion.close()

basedatos()

# Función para añadir registros
def añadirRegistros(nombre, carrera, foto):
    conexion = sqlite3.connect("dbAppInterfaz")
    inicializar = conexion.cursor()
    inicializar.execute(
        "INSERT INTO estudiante (nombre,carrera,foto) VALUES (?,?,?)",
        (nombre, carrera, foto),
    )
    conexion.commit()
    conexion.close()

# Función para obtener datos
def obtenerDatos():
    conexion = sqlite3.connect("dbAppInterfaz")
    selector = conexion.cursor()
    selector.execute("SELECT * FROM estudiante")
    filas = selector.fetchall()
    conexion.close()
    return filas
#FUNCION PARA ELIMINAR UN DATO
def eliminarRegistro(id):
    conexion=sqlite3.connect("dbAppInterfaz")
    selector=conexion.cursor()
    selector.execute("DELETE FROM estudiante WHERE id=?",(id,))
    conexion.commit()
    conexion.close()
    obtenerDatos()

# Interfaz principal
def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text("Insertar Nuevos Registros", size=20)
    nombre = ft.TextField(label="Ingrese un nombre: ")
    carrera = ft.TextField(label="Ingrese la carrera: ")
    foto = ft.TextField(label="Ingrese una foto (URL): ")

    lista = ft.Column()

    # Función para añadir registro
    def añadir(e):
        nombreObtenido = nombre.value.strip()
        carreraObtenido = carrera.value.strip()
        fotoObtenido = foto.value.strip()

        if not nombreObtenido or not carreraObtenido:
            page.snack_bar = ft.SnackBar(ft.Text("Debe completar los campos para continuar..."))
            page.snack_bar.open = True
            page.update()
            return
        else:
            añadirRegistros(nombreObtenido, carreraObtenido, fotoObtenido)
            page.snack_bar = ft.SnackBar(ft.Text("Se registró correctamente..."))
            page.snack_bar.open = True

            # Limpiar campos
            nombre.value = ""
            carrera.value = ""
            foto.value = ""

            page.update()

    # Función para mostrar registros
    def mostrarDatos(e):
        datos = obtenerDatos()
        lista.controls.clear()

        if not datos:
            lista.controls.append(ft.Text("No hay registros que mostrar..."))
        else:
            for id, nombre_est, carrera_est, foto_est in datos:
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Image(src=foto_est, width=80, height=80),
                                ft.Column([ft.Text(nombre_est,size=18,weight=ft.FontWeight.BOLD), ft.Text(carrera_est)]),
                                ft.Row(
                                    [ft.IconButton(icon=ft.Icons.DELETE
                                                   ,on_click=lambda e, id=id:eliminarRegistro(id),
                                                   icon_color=ft.Colors.RED_400)]
                                )
                            ]
                        ),
                        
                        padding=15,
                        bgcolor=ft.colors.WHITE70,
                    )
                )
                lista.controls.append(card)

        page.update()

    registrar = ft.CupertinoFilledButton("Registrar", on_click=añadir)
    botonMostrar = ft.CupertinoFilledButton(text="Mostrar", on_click=mostrarDatos)


    

    page.add(
        ft.Column(
            [
                titulo,
                nombre,
                carrera,
                foto,
                registrar,
                botonMostrar,
                lista,
            ],
            width=350,
        )
    )


ft.app(main)
