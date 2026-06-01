import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=200,
            height=200,
            border=ft.Border.all(1, ft.Colors.BLACK),
            content=ft.FilledButton("Primary color"),
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.YELLOW))
        )
    )

ft.run(main)