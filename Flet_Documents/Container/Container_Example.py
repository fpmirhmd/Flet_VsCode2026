import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Hello, Flet!"),
            padding=20,
            margin=10,
            bgcolor="lightblue",
            border_radius=ft.BorderRadius.all(20),
            alignment=ft.Alignment.CENTER
        )
    )

ft.app(main)
