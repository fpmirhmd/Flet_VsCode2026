import flet as ft

def main(page: ft.Page):
    box = ft.Container(
        content=ft.Text("Hello, Flet!"),
        width=200,
        height=100,
        bgcolor="blue",
        alignment=ft.Alignment.CENTER
    )
    
    page.add(box)

ft.app(main)