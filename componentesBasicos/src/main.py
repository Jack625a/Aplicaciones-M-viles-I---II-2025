#IMPORTACION
import flet as ft

#FUNCION PRINCIPAL
def main(page: ft.Page):
    
    #BOTONES
    boton=ft.Button(text="Boton 1",bgcolor=ft.colors.BLUE_50,icon=ft.icons.HOME,)
    boton2=ft.CupertinoFilledButton(text="Boton 2",
                                    icon=ft.icons.FACE,
                                    icon_color=ft.colors.CYAN_ACCENT_200)
    boton3=ft.FilledButton(text="Boton 3",icon=ft.icons.TIKTOK)
    #Componentes de la interfaz
    page.add(
        boton,boton2,boton3   
    )


ft.app(main)
