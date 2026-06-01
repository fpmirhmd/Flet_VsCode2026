import flet as ft

def main(page: ft.Page):
    page.add(
        ft.IconButton(
            icon=ft.Icons.FAVORITE,
            style=ft.ButtonStyle(
                icon_color=ft.Colors.RED,
                icon_size=40,  # larger icon
            ),
        ),
        ft.IconButton(
            icon=ft.Icons.STAR,
            style=ft.ButtonStyle(
                icon_color=ft.Colors.BLUE,
                icon_size=20,  # smaller icon
            ),
        ),
    )

ft.run(main)
