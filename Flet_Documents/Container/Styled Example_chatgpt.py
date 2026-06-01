import flet as ft

def main(page: ft.Page):
    box = ft.Container(
    content=ft.Text("Styled Box"),
    width=250,
    height=120,
    bgcolor="green",
    padding=20,
    margin=10,
    border_radius=15,
    alignment=ft.Alignment.CENTER
)
    
    page.add(box)

ft.app(main)