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

    page.window.width = 400
    page.window.height = 550

    # Configuração do banner de notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text('Ops, preencha todos os campos?'),
        actions=[
            ft.TextButton('Ok', on_click=close_banner),
        ],
    )


    altura = ft.TextField(label='Altura', hint_text='Por favor insira a sua altura')
    peso = ft.TextField(label='Peso', hint_text='Por favor insira o seu peso')
    genero = ft.Dropdown(
        label='Genero',
        hint_text='Escolha seu genero!',
        options=[
            ft.dropdown.Option('Masculino'),
            ft.dropdown.Option('Feminino'),
        ],
    )

    b_calcular = ft.ElevatedButton(text='Calcular IMC')

    # Exibir o IMC e resultado
    IMC = ft.Text('Seu IMC é ...', size=30)
    detalhes= ft.Text('Insira seus dados', size=20)

    img_capa = ft.Image(
        src=f'capa.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info_app_resultado = ft.Column(
        controls=[
            IMC,
            detalhes,
        ]
    )

    img_resultado = ft.Image(
        src=f'capa.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info = ft.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ]
    )

    # Layout da pagina
    layout = ft.ResponsiveRow(
        [
            ft.Container(
                info,
                padding=5,
                col= {'sm':4, 'md':4, 'xl':4},
                alignment=ft.alignment.center,
        ),
            ft.Container(
                altura,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col= {'sm':12, 'md':3, 'xl':3},
        ),

            ft.Container(
                peso,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col= {'sm':12, 'md':3, 'xl':3},
        ),

            ft.Container(
                genero,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col= {'sm':12, 'md':3, 'xl':3},
        ),

            ft.Container(
                b_calcular,
                padding=5,
                bgcolor=ft.colors.WHITE,
                col= {'sm':12, 'md':3, 'xl':3},
        ),

            ft.Container(
                padding=5,
                bgcolor=ft.colors.WHITE,
                col= {'sm':12, 'md':3, 'xl':3},
        ),
        ]
        
    )

    page.add(layout)

ft.app(target=main)
