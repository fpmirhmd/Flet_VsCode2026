import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=250,
            height=120,
            content=ft.Text("Linear Gradient"),
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=["#ff9a9e", "#fad0c4", "#fbc2eb"]
            ),
            alignment=ft.Alignment.CENTER,
            border_radius=15
        )
    )

ft.app(main)
