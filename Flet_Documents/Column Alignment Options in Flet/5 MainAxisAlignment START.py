import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text("First item"),
                ft.Text("Second item"),
                ft.Text("Third item"),
            ],
            height=300,
            alignment=ft.MainAxisAlignment.START,  # top alignment
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(main)
