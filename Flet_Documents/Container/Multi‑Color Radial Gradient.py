import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=300,
            height=150,
            content=ft.Text("Radial Glow"),
            gradient=ft.RadialGradient(
                center=ft.Alignment.CENTER,
                radius=1.0,
                colors=["#ffecd2", "#fcb69f", "#ff9a9e", "#fad0c4"]
            ),
            alignment=ft.Alignment.CENTER,
            border_radius=20
        )
    )

ft.app(main)
