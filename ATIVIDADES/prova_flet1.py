"""[PYIA-A09] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. 
A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. 
Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. 
A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado."""

import flet as ft # para rodar baixar a bib flet

def main(page=ft.Page):
    page.title = "Lista de Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def adicionar_item(e):
        page.add(
            ft.Checkbox(label=tarefa.value)
        )
        tarefa.value = ""
        page.update()

    h1 = ft.Text("TO DO LIST", size=72, weight=ft.FontWeight.BOLD)
    tarefa = ft.TextField(label="Tarefa", hint_text="Digite aqui sua tarefa", text_size=18)
    butao_para_adicionar = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=adicionar_item)

    janela = ft.Column(
        width=350,
        controls=[
            ft.Row(
                controls=[
                    tarefa,
                    butao_para_adicionar
                ]
            )
        ]
    )

    page.add(
        h1,
        janela
    )

ft.app(target=main)
