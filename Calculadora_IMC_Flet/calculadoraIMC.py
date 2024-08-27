import flet as ft

def main(page: ft.Page):
    # configurando a pagina
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text('Calculadora IMC'),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT

    )

    page.window_width = 400
    page.window_height = 550

ft.app(target=main)

