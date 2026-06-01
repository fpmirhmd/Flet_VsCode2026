import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text("Top aligned"),
                ft.Text("Centered horizontally"),
                ft.Text("Bottom aligned"),
            ],
            height=300,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,   # vertical alignment
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # horizontal alignment
        )
    )

ft.app(main)
