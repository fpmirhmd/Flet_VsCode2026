import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=250,
            height=120,
            content=ft.Text("Radial Gradient"),
            gradient=ft.RadialGradient(
                center=ft.Alignment.CENTER,
                radius=1.0,
                colors=["#a1c4fd", "#c2e9fb"]
            ),
            alignment=ft.Alignment.CENTER,
            border_radius=15
        )
    )

ft.app(main)
