import flet as ft
import pathpy

def main(page: ft.Page):
    page.title = "Derivar"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    funcao_input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=200)
    funcao_output = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=200)

    def calcular(e):
        funcao_output.value = pathpy.cauculo(funcao_input.value)
        page.update()

    def desenha_derivada(e):
        pathpy.desenhar_grafico(funcao_output.value)
        page.update()

    def desenha_funcao(e):
        pathpy.desenhar_grafico(funcao_input.value)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=calcular),
                funcao_input
                # ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                funcao_output,
                ft.IconButton(ft.icons.REMOVE, on_click=desenha_derivada)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)