import flet as ft

def main(page: ft.Page):

    def close_banner(e):
        page.banner.open = False
        page.update()


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

    # Configuração do banner de notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text('Ops, preencha todos os campos?'),
        actions=[
            ft.TextButton('Ok', on_click=close_banner),
        ],
    )

ft.app(target=main)
