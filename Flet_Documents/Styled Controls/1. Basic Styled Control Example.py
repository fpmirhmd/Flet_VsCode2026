import flet as ft

def main(page: ft.Page):
    page.title = "Styled Controls Example"

    card = ft.Container(
        content=ft.Text("Hello Styled Flet UI!", size=20, weight="bold"),
        width=300,
        height=120,
        padding=20,
        alignment=ft.Alignment.CENTER,
        bgcolor="#4CAF50",
        border_radius=15,
        shadow=ft.BoxShadow(
            blur_radius=15,
            color="black26",
            offset=ft.Offset(4, 4)
        )
    )

    page.add(card)

ft.app(target=main)