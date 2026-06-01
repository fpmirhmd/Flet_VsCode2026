import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=300,
            height=150,
            content=ft.Text("Rainbow Blend"),
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=["#ff9a9e", "#fad0c4", "#fbc2eb", "#a1c4fd", "#c2e9fb"]
            ),
            alignment=ft.Alignment.CENTER,
            border_radius=20
        )
    )

ft.app(main)
