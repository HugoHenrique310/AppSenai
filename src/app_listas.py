import asyncio

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, FloatingActionButton, Icons, Button, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption


class Pessoa:
    def __init__(self, nome, profissao, sexo):
        self.nome = nome
        self.profissao = profissao
        self.sexo = sexo


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

    def montar_lista_texto():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                        Icon(Icons.PERSON),
                        Text(item.nome),
                        Text(item.profissao)
                    ],
                        margin=8
                    ),

                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.MAN, color=Colors.BLUE) if item.sexo == "Masculino" else Icon(Icons.WOMAN,color=Colors.PINK),
                    title=item.nome,
                    subtitle=item.profissao,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),

                )
            )

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value
        profissao = input_profissao.value
        sexo = input_sexo.value

        tem_erro = False

        if nome:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if profissao:
            input_nome.error = None
        else:
            tem_erro = True
            input_profissao.error = "Campo obrigatório"

        if sexo:
            input_sexo.error = None
        else:
            tem_erro = True
            input_sexo.error = "Campo obrigatório"

        if not tem_erro:
            # montar o objeto
            pessoa = Pessoa(
                nome=nome,
                profissao=profissao,
                sexo=sexo,
            )

            # add o objeto na lista
            lista_dados.append(pessoa)
            input_nome.value = ""
            input_profissao.value = ""
            input_sexo.value = ""

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Exemplos de Listas",
                        bgcolor=Colors.AMBER_200
                    ),
                    flet.Button("Lista de texto", on_click=lambda: navegar("/lista_texto")),
                    flet.Button("Lista de Card", on_click=lambda: navegar("/lista_card")),
                    flet.Button("Lista padrão Android", on_click=lambda: navegar("/lista_padrao"))
                ]
            )
        )

        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        flet.AppBar(
                            title="Lista de texto",
                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )
        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        flet.AppBar(
                            title="Lista de Card",
                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )
        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(
                            title="Lista padrão Android",
                        ),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda: navegar("/form_cadastro"),
                    )
                )
            )
        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,
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
    input_nome = TextField(label="Nome", hint_text="Digite seu nome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_dados)
    list_view = ListView(height=500)
    input_profissao = TextField(label="Profissao", hint_text="Digite sua profissao")
    input_sexo = Dropdown(
        label="Gênero",
        editable=True,
        options=[
            DropdownOption("Masculino"),
            DropdownOption("Feminino"),
        ],
    )

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
