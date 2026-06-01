import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text("Left aligned"),
                ft.Text("Still left aligned"),
                ft.Text("All stacked left"),
            ],
            width=300,
            alignment=ft.MainAxisAlignment.CENTER,  # vertical centering
            horizontal_alignment=ft.CrossAxisAlignment.START  # left alignment
        )
    )

ft.app(main)
