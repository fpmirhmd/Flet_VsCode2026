import flet as ft

def main(page: ft.Page):
    page.title = "Column Example"
    page.add(
        ft.Column(
            width=220,
            height=120,
            spacing=12,
            controls=[
                ft.Text("Daily planning", size=20, weight=ft.FontWeight.W_600),
                ft.Text("Review pull requests"),
                ft.Text("Ship release"),
            ],
        )
    )

ft.app(target=main)
