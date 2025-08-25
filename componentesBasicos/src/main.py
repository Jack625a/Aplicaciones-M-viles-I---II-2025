#IMPORTACION
import flet as ft


    

#FUNCION PRINCIPAL
def main(page: ft.Page):
    #fUNCION ALERTA
    alerta=ft.AlertDialog(
        title=ft.Text("Alerta"),
        content=ft.Text("Mensaje de Prueba"),
        actions=[ft.CupertinoButton(text="Salir")],
        #modal=True
        )
       



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


    #Componentes de la interfaz
    page.add(

        boton,boton2,boton3,boton4, pruebaBoton, nombre,edad,contraseña,
        usuario,opcion1,opcion1ios
    )


ft.app(main)
