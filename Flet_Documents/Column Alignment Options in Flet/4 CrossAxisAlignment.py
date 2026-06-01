import flet as ft

def main(page: ft.Page):
    page.title = "Column Alignment Demo"

    page.add(
        ft.Column(
            width=220,
            height=200,
            spacing=12,
            controls=[
                ft.Text("Daily planning", size=20, weight=ft.FontWeight.W_600),
                ft.Text("Review pull requests"),
                ft.Text("Ship release"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,          # vertical alignment
            horizontal_alignment=ft.CrossAxisAlignment.START  # horizontal alignment
        )
    )

ft.app(target=main)
