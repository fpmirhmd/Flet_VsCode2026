import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Hello"),
            alignment=ft.Alignment.CENTER_RIGHT,  # 👈 alignment here
            width=200,
            height=200,
            bgcolor="blue"
        )
    )

ft.run(main)