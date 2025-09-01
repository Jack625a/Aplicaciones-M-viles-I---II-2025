#IMPORTACION
import flet as ft


    

#FUNCION PRINCIPAL
def main(page: ft.Page):
    #activar el scroll
    page.scroll=ft.ScrollMode.AUTO



    #fUNCION ALERTA
    alerta=ft.AlertDialog(
        title=ft.Text("Alerta"),
        content=ft.Text("Mensaje de Prueba"),
        actions=[ft.CupertinoButton(text="Salir")],
        #modal=True
        )
       
    page.appbar=ft.AppBar(title=ft.Text("Mi aplicacion"))
    

    #Variable de control
    page.floating_action_button=(ft.FloatingActionButton(icon=ft.icons.HOME,bgcolor=ft.colors.PURPLE,on_click=lambda e:page.open(alerta)))
    #BOTONES
    boton=ft.Button(text="Boton 1",bgcolor=ft.colors.BLUE_50,icon=ft.icons.HOME,on_click=lambda e:page.open(alerta) )
    boton2=ft.CupertinoFilledButton(text="Boton 2",
                                    icon=ft.icons.FACE,
                                    icon_color=ft.colors.CYAN_ACCENT_200)
    boton3=ft.FilledButton(text="Boton 3",icon=ft.icons.TIKTOK)

    boton4=ft.IconButton(icon=ft.icons.IMAGE)
    
    pruebaBoton=ft.FloatingActionButton(icon=ft.icons.HOME)

    #ENTRADAS DE TEXTO
    nombre=ft.TextField(
        #keyboard_type=ft.KeyboardType('PHONE'),
        label="Ingrese su nombre ",
        icon=ft.icons.INSTALL_DESKTOP
        
        )
    edad=ft.TextField(
        label="Ingrese su edad",
        icon=ft.icons.PERSON_3
    )
    contraseña=ft.TextField(
        label="Ingrese su contraseña",
        password=True,
        can_reveal_password=True,
        icon=ft.icons.PASSWORD
    )
    
    #Campos de texto para iOS

    usuario=ft.CupertinoTextField(
        placeholder_text="|Ingrese su usuario",
        placeholder_style=ft.TextStyle(color=ft.colors.PURPLE_800),
        )
    
    #CASILLAS DE VERIFICACION

    opcion1=ft.Checkbox(label="Opcion1") #android
    opcion1ios=ft.CupertinoCheckbox(label="Opcion 1 iOS") #ios

    #Selecctor Radio

    opcion2=ft.Radio(label="Opcion2")
    opcion2Ios=ft.CupertinoRadio("Opcion2 iOS")

    def controlVolumen(e):
        volumenTexto.value={e.control.value}
        page.update()

    #Sliders
    volumenTexto=ft.Text()
    volumen=ft.Slider(label="{value}% ",min=0,max=100, on_change=controlVolumen,divisions=10)

    volumenIos=ft.CupertinoSlider(min=0,max=10)

    #Chips
    chip=ft.Chip(label=ft.Text("Prueba chip"), leading=ft.Icon(name="HOME"),
                 bgcolor=ft.Colors.BROWN_900, 
                 color=ft.Colors.WHITE12,
                 on_click=lambda e:page.open(alerta))

    chip2=ft.Chip(label=ft.Text("Prueba chip"), leading=ft.Icon(name="HOME"),
                    bgcolor=ft.Colors.BROWN_900, 
                    color=ft.Colors.WHITE12,
                    on_click=lambda e:page.open(alerta) )
    
    #contenedores
    #CONTENEDOR TIPO FILA (HORIZONTAL) ROW
    fila=ft.Row(controls=[chip,chip2,boton,boton2,boton3,boton4],spacing=15,scroll=ft.ScrollMode.AUTO)
    #contenedo Tipo COLUMNA (VERTICALES) COLUMN
    columna=ft.Column(controls=[chip,chip2,nombre,fila],spacing=20,width=250)
    #Contenedores responsivos
    #Contenedores row (filas responsivas)

    filaResponsivo=ft.ResponsiveRow([
        ft.Row(controls=[ft.Text("Filas Responsivas")],col=6),
        ft.Row(controls=[chip,chip2,nombre],col=6),
        ft.Row(controls=[boton,boton2,boton3],col=6)
    ])

    #Formulario Responsivo
    formularioResponsivo=ft.ResponsiveRow([
        ft.TextField(label="Nombre"),
        ft.TextField(label="Celular"),
        ft.TextField(label="Correo"),
        ft.TextField(label="Carrera"),
    ],
        
        spacing=10
    )

    #Contenedores simples
    contenedorSimple=ft.Container(
        content=ft.Text("Contenedor",size=20),
        margin=10,
        padding=10,
        width=150,
        height=150,
        border_radius=50,
        bgcolor=ft.Colors.BLUE_500,
        alignment=ft.alignment.center
    )

    #dentro de una fila o columna (contenedores)
    contenedoresDentroContenedores=ft.Column([
        contenedorSimple,
        ft.Divider(),
        contenedorSimple,
        ft.Divider(),
        contenedorSimple,
        ft.Divider(),
        contenedorSimple
    ],
    scroll=ft.ScrollMode.ADAPTIVE)

    #Componentes de la interfaz
    page.add(

        boton,boton2,boton3,boton4, pruebaBoton, nombre,edad,contraseña,
        usuario,opcion1,opcion1ios, opcion2, opcion2Ios,volumen,volumenTexto,
        volumenIos,chip,chip2,fila,columna, filaResponsivo, formularioResponsivo,
        contenedorSimple,contenedoresDentroContenedores
    )


ft.app(main)
