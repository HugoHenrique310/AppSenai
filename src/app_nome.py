import asyncio

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View

def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode. Light
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        text1.value = f'Bom dia {input_nome.value}'
        input_nome.value = ""
        navegar(route="/segunda_tela")


    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira página",
                        bgcolor=Colors.AMBER_200
                    ),
                    input_nome,
                    btn_salvar,
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda página",

                        ),
                        text1,
                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text1 = Text()
    input_nome = TextField(label="Nome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)


    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)