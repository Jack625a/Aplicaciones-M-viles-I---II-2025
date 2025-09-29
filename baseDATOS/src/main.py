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

#FUNCION PARA ACTULIZAR LOS DATOS
def actualizarRegistro(id,nombre,carrera,foto):
    #PASO1. ESTABLECER LA CONEXION
    conexion=sqlite3.connect("dbAppInterfaz")
    selector=conexion.cursor()
    selector.execute("UPDATE estudiante SET nombre?,carrera=?, foto=? WHERE id=?",(nombre,carrera,foto,id),)
    conexion.commit()
    conexion.close()

def mostrarDatoActulizar(id):
    conexion = sqlite3.connect("dbAppInterfaz")
    selector = conexion.cursor()
    selector.execute("SELECT * FROM estudiante WHERE id=?",(id,))
    filas = selector.fetchone()
    conexion.close()
    return filas

# Interfaz principal
def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text("Insertar Nuevos Registros", size=20)
    nombre = ft.TextField(label="Ingrese un nombre: ")
    carrera = ft.TextField(label="Ingrese la carrera: ")
    foto = ft.TextField(label="Ingrese una foto (URL): ")

    lista = ft.Column()

    #Variable para almacenar el id en la seccion de editar
    idEditar={"id":None}

    #Configurar el formulario de actualizacion
    tituloActualizar=ft.Text("Actualizar datos", size=20, visible=False)
    nombreActulizar=ft.TextField(label="Nombre: ",visible=False)
    carreraActualizar=ft.TextField(label="Carrera", visible=False)
    fotoActualizar=ft.TextField("Foto", visible=False)

    def guardarActualizacion(e):
        if idEditar["id"] is not None:
            actualizarRegistro(idEditar["id"],
            nombreActulizar.value.strip(),
            carreraActualizar.value.strip(),
            fotoActualizar.value.strip()                              
                               )
            #Ocultamos y limpiamos el formulario
            tituloActualizar.visible=False
            nombreActulizar.visible=False
            carreraActualizar.visible=False
            fotoActualizar.visible=False
            botonActualizar.visible=False


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
    def mostrarFormulario(e):
            ft.Column([
                            tituloActualizar,
                            nombreActulizar,
                            carreraActualizar,
                            fotoActualizar,
                            botonActualizar
                            
                        ],visible=True)
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
                                ft.Text(id),
                                ft.Image(src=foto_est, width=100, height=100,border_radius=30),
                                ft.Column([ft.Text(nombre_est,size=18,weight=ft.FontWeight.BOLD), ft.Text(carrera_est)]),
                                ft.Row(
                                    [ft.IconButton(icon=ft.Icons.DELETE
                                                   ,on_click=lambda e, id=id:eliminarRegistro(id),
                                                   icon_color=ft.Colors.RED_400,
                                                   tooltip="Eliminar"),
                                    ft.IconButton(icon=ft.Icons.SYSTEM_UPDATE,
                                                  on_click=lambda e:mostrarFormulario(),
                                                  tooltip="Actualizar",
                                                  icon_color=ft.Colors.GREEN_600,),
                                    ]
                                )
                            ]
                        ),
                        
                        padding=15,
                        bgcolor=ft.Colors.WHITE70,
                    )
                )
                lista.controls.append(card)

        page.update()

    registrar = ft.CupertinoFilledButton("Registrar", on_click=añadir)
    botonMostrar = ft.CupertinoFilledButton(text="Mostrar", on_click=mostrarDatos)

    #formulario para actualizar 
    tituloActualizar=ft.Text("Actualizar datos" , size=20,visible=True)
    nombreActulizar=ft.TextField(label="Nombre",visible=True)
    carreraActualizar=ft.TextField(label="Carrera",visible=True)
    fotoActualizar=ft.TextField(label="Foto",visible=True)
    botonActualizar=ft.CupertinoFilledButton(text="Actualizar",visible=True)

    idEditar={"id":None}

    #def añadirDatos(e):
    def mostrarDatosParaActulizar():
        datos = mostrarDatoActulizar()
        lista.controls.clear()

        if not datos:
            lista.controls.append(ft.Text("No hay registros que mostrar..."))
        else:
            for id, nombre_est, carrera_est, foto_est in datos:
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(id),
                                ft.Image(src=foto_est, width=100, height=100,border_radius=30),
                                ft.Column([ft.Text(nombre_est,size=18,weight=ft.FontWeight.BOLD), ft.Text(carrera_est)]),
                                ft.Row(
                                    [ft.IconButton(icon=ft.Icons.DELETE
                                                   ,on_click=lambda e, id=id:eliminarRegistro(id),
                                                   icon_color=ft.Colors.RED_400,
                                                   tooltip="Eliminar"),
                                    ft.IconButton(icon=ft.Icons.SYSTEM_UPDATE,
                                                  on_click=lambda e, id=id:actualizarRegistro(id)
                                                  ,tooltip="Actualizar",
                                                  icon_color=ft.Colors.GREEN_600)
                                    ]
                                )
                            ]
                        ),
                        
                        padding=15,
                        bgcolor=ft.Colors.WHITE70,
                    )
                )
                lista.controls.append(card)

        page.update()
   
    
    

    

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
                ft.Column([
                            tituloActualizar,
                            nombreActulizar,
                            carreraActualizar,
                            fotoActualizar,
                            botonActualizar
                            
                        ],visible=True)
                
                
                
            ],
            width=450,
        )
    )


ft.app(main)
