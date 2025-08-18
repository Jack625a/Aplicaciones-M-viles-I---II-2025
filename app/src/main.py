#Importacion del framework
import flet as ft

#funcion principal
def main(page: ft.Page):
    #Barra de navegacion
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                label='Inicio',
                icon=ft.icons.HOME
            ),
            ft.NavigationBarDestination(
                label='Productos',
                icon=ft.icons.STORE
            ),
            ft.NavigationBarDestination(
                label='Servicios',
                icon=ft.icons.STORE
            )
        ],
        bgcolor=ft.Colors.CYAN_900,
        
    )
    #AppBar (cabecera ANDROID)
    page.appbar=ft.AppBar(
        leading=ft.Icon(ft.icons.MENU,color=ft.colors.WHITE),
        title=ft.Text('Primera App'),
        bgcolor=ft.colors.CYAN_900

    )

    #Componentes de la interfaz
    page.add(
        
    )

ft.app(main)
