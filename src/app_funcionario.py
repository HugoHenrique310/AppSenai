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
    def cadastrar_funcionario():
        text_nome.value = f'Nome:{input_nome.value}'
        text_cpf.value = f'CPF: {input_CPF.value}'
        text_email.value = f'Email: {input_email.value}'
        text_salario.value = f'Salário R$: {input_salario.value}'


        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if input_CPF.value:
            input_CPF.error = None
        else:
            tem_erro = True
            input_CPF.error = "Campo obrigatório"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatório"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatório"

        if not tem_erro:
            input_nome.value = ""
            input_CPF.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                    input_CPF,
                    input_email,
                    input_salario,
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
                        text_nome,
                        text_cpf,
                        text_email,
                        text_salario,
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
    text_nome = Text()
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()
    input_nome = TextField(label="Nome")
    input_CPF = TextField(label="CPF")
    input_email = TextField(label="Email")
    input_salario = TextField(label="Salário")
    btn_salvar = OutlinedButton("Salvar", on_click=cadastrar_funcionario)

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)