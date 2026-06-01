import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Stylish Container"),
            width=200,
            height=100,
            border_radius=20,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_LEFT,
                end=ft.Alignment.BOTTOM_RIGHT,
                colors=["#ff9a9e", "#fad0c4"]
            ),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=8,
                color="rgba(0,0,0,0.3)",
                offset=ft.Offset(4,4)
            ),
            alignment=ft.Alignment.CENTER
        )
    )

ft.app(main)
