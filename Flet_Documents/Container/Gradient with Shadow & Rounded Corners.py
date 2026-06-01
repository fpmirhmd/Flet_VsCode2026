import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=300,
            height=150,
            content=ft.Text("Layered Gradient Card"),
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=["#ff9a9e", "#fad0c4", "#fbc2eb"]
            ),
            border_radius=20,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color="rgba(0,0,0,0.25)",
                offset=ft.Offset(4,4)
            ),
            alignment=ft.Alignment.CENTER
        )
    )

ft.app(main)
