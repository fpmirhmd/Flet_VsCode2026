import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=300,
            height=300,
            bgcolor="lightgrey",
            alignment=ft.Alignment.CENTER,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Aligned Text")
                ]
            )
        )
    )

ft.run(main)