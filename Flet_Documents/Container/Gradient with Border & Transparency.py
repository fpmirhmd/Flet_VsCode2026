import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=300,
            height=150,
            content=ft.Text("Glassmorphism Style"),
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=["rgba(255,255,255,0.6)", "rgba(255,255,255,0.1)"]
            ),
            # border=ft.border.all(2, "white"),
            border_radius=15,
            shadow=ft.BoxShadow(
                blur_radius=20,
                color="rgba(0,0,0,0.2)",
                offset=ft.Offset(0,6)
            ),
            alignment=ft.Alignment.CENTER
        )
    )

ft.app(main)
