from unittest import result

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode. Light
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        text.value = f'Bom dia {input_nome.value} {input_sobrenome.value}'
        page.update()

    def impar_par():
        n1 = int(input_numero.value)
        if n1 % 2 == 0:
            text.value = f'O numero {n1} é um número par'
            page.update()
        else:
            text.value = f'O numero {n1} é um número impar'
            page.update()

    def data_nascimento():
        data_nascimento= int(input_data_nascimento.value)
        resultado_idade = 2026 - data_nascimento
        if resultado_idade >= 18:
            text.value = f'Maior de {resultado_idade}  idade'
            page.update()
        else:
            text.value = f'Menor  de{resultado_idade}  idade'
            page.update()





    # Componentes

    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    input_numero = TextField(label="Número")
    btn_salvar2 = OutlinedButton("Salvar", on_click=impar_par)

    input_data_nascimento= TextField(label="Ano de nascimento")
    btn_salvar3 = OutlinedButton("Salvar", on_click=data_nascimento)
    text = Text()
    # Construção da tela

    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                input_numero,
                btn_salvar2,
                input_data_nascimento,
                btn_salvar3,
                text

            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )


flet.app(main)
