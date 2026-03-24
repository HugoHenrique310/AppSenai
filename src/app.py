import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight


def main(page: flet.Page):
    # Configurações
    page.title = "Primeira APP"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode. Light
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        text1.value = f'Bom dia {input_nome.value} {input_sobrenome.value}'
        page.update()

    def impar_par():
        n1 = int(input_numero.value)
        if n1 % 2 == 0:
            text2.value = f'O numero {n1} é um número par'
            page.update()
        else:
            text2.value = f'O numero {n1} é um número impar'
            page.update()

    def data_nascimento():
        data_nascimento= int(input_data_nascimento.value)
        resultado_idade = 2026 - data_nascimento
        if resultado_idade >= 18:
            text3.value = f'Maior de {resultado_idade}  idade'
            page.update()
        else:
            text3.value = f'Menor  de{resultado_idade}  idade'
            page.update()

    # Componentes

    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    text1 = Text()

    input_numero = TextField(label="Número")
    btn_salvar2 = OutlinedButton("Salvar", on_click=impar_par)
    text2 = Text()
    input_data_nascimento= TextField(label="Ano de nascimento")
    btn_salvar3 = OutlinedButton("Salvar", on_click=data_nascimento)
    text3 = Text()
    # Construção da tela

    page.add(
        Column(
            [
                Container(
                    Column(
                        [
                            Text("Atividade 1", weight=FontWeight.BOLD, size=24),
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                            text1,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,

                    ),
                    bgcolor=Colors.BLUE_200,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),

                Container(
                    Column(
                        [
                            Text("Atividade 2", weight=FontWeight.BOLD, size=24),
                            input_numero,
                            btn_salvar2,
                            text2,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,

                    ),
                    bgcolor=Colors.GREEN_200,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),

                Container(
                    Column(
                        [
                            Text("Atividade 3", weight=FontWeight.BOLD, size=24),
                            input_data_nascimento,
                            btn_salvar3,
                            text3,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,

                    ),
                    bgcolor=Colors.WHITE_70,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),



            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )


flet.run(main)
