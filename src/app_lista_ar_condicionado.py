import asyncio

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, FloatingActionButton, Icons, Button, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption


class Ar_condicionado:
    def __init__(self, marca, modelo, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.valor = valor


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode. Light
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_padrao():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.RECTANGLE) if item.modelo == "Inverter" else Icon(Icons.RECTANGLE),
                    title=item.marca,
                    subtitle=item.valor,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, ar_condi=item: ver_detalhes(ar_condi)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),

                )
            )



    def ver_detalhes(ar_condicionado):
        text_marca.value = ar_condicionado.marca
        text_valor.value = ar_condicionado.valor
        text_modelo.value = ar_condicionado.modelo
        text_cor.value = ar_condicionado.cor

        navegar("/detalhes")


    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        marca = input_marca.value
        valor = input_valor.value
        modelo = input_modelo.value
        cor = input_cor.value

        tem_erro = False

        if marca:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatório"

        if valor:
            input_valor.error = None
        else:
            tem_erro = True
            input_valor.error = "Campo obrigatório"

        if modelo:
            input_modelo.error = None
        else:
            tem_erro = True
            input_modelo.error = "Campo obrigatório"

        if cor:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatório"


        if not tem_erro:
            # montar o objeto
            ar_condicionado = Ar_condicionado(
                marca=marca,
                valor=valor,
                modelo=modelo,
                cor=cor,
            )

            # add o objeto na lista
            lista_dados.append(ar_condicionado)
            input_marca.value = ""
            input_valor.value = ""
            input_modelo.value = ""
            input_cor.value = ""

        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    flet.AppBar(
                        title="Ar - Condicionado",
                    ),
                    list_view
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_marca,
                        input_valor,
                        input_modelo,
                        input_cor,
                        btn_salvar,
                    ]
                )
            )

        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        text_marca,
                        text_valor,
                        text_modelo,
                        text_cor,
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
    input_marca = TextField(label="Marca", hint_text="Digite o nome da marca")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_dados)
    list_view = ListView(height=500)
    input_valor = TextField(label="Valor", hint_text="Digite o valor")
    input_modelo = Dropdown(
        label="Modelo",
        editable=True,
        options=[
            DropdownOption("Inverter"),
            DropdownOption("Convencional"),
        ],
    )
    input_cor = Dropdown(
        label="Cor",
        editable=True,
        options=[
            DropdownOption("Branco"),
            DropdownOption("Preto"),
        ],
    )

    text_marca = Text(weight=FontWeight.BOLD, size=24)
    text_valor = Text()
    text_modelo = Text()
    text_cor = Text()

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)