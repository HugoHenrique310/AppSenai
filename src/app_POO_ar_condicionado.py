import asyncio

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, Row, Icon, Icons


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode. Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    def cadastrar_ar_condicionado():
        text_marca.value = f'Marca:{input_marca.value}'
        text_modelo.value = f'Modelo: {input_modelo.value}'
        text_cor.value = f'Cor: {input_cor.value}'
        text_valor.value = f'Valor R$: {input_valor.value}'

        tem_erro = False
        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatório"

        if input_modelo.value:
            input_modelo.error = None
        else:
            tem_erro = True
            input_modelo.error = "Campo obrigatório"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatório"

        if input_valor.value:
            input_valor.error = None
        else:
            tem_erro = True
            input_valor.error = "Campo obrigatório"

        if not tem_erro:
            input_marca.value = ""
            input_modelo.value = ""
            input_cor.value = ""
            input_valor.value = ""
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
                    input_marca,
                    input_modelo,
                    input_cor,
                    input_valor,
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
                        Column([
                            Text(),
                            Row([
                                Icon(Icons.MARKUNREAD, color=Colors.PRIMARY, size=20),
                                text_marca

                            ]),
                            Row([
                                text_modelo
                            ]),
                            Row([
                                Icon(Icons.COLOR_LENS, color=Colors.PRIMARY, size=20),
                                text_cor
                            ]),
                            Row([
                                Icon(Icons.ATTACH_MONEY, color=Colors.PRIMARY, size=20),
                                text_valor
                            ]),
                        ])
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
    text_marca = Text()
    text_modelo = Text()
    text_cor = Text()
    text_valor = Text()
    input_marca = TextField(label="Marca")
    input_modelo = TextField(label="Modelo")
    input_cor = TextField(label="Cor")
    input_valor = TextField(label="Valor")
    btn_salvar = OutlinedButton("Salvar", on_click=cadastrar_ar_condicionado)

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)