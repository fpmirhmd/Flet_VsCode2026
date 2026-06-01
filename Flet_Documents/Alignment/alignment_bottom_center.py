import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Hello"),
            alignment=ft.Alignment.BOTTOM_CENTER,  # 👈 alignment here
            width=200,
            height=200,
            bgcolor="blue"
        )
    )

ft.run(main)