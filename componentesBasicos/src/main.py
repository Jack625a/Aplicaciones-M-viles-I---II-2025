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
    #Componentes de la interfaz
    page.add(

        boton,boton2,boton3,boton4, pruebaBoton, nombre,edad,contraseña,
        usuario,opcion1,opcion1ios, opcion2, opcion2Ios,volumen,volumenTexto,
        volumenIos,chip,chip2,fila,columna
    )


ft.app(main)
